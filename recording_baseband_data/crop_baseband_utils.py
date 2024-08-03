# Maxwell A. Fine
# 2024-08-01
# Contact: https://afinemax.github.io/afinemax1/

# imports
from crop_sigmf import crop_sigmf
import os
import h5py
import numpy as np
import subprocess
import sigmf
from datetime import datetime, timedelta
import subprocess
from datetime import datetime, timedelta
from astropy.time import Time
from your.formats.pysigproc import SigprocFile
fromisoformat = datetime.fromisoformat
import json
import os
from datetime import datetime
from astropy.time import Time
import time
import pytz  # time zone management 
import traceback


def read_baseband_data(ram_data_dir, orig_file_name, return_data=False, data_slice=False):
    """
    Reads metadata from a baseband data file and extracts key information.

    Parameters:
    ram_data_dir (str): Directory where the baseband data file is stored.
    orig_file_name (str): Name of the baseband data file including the `.sigmf-meta` extension. 
    return_data (bool, optional): If True, additional data will be returned. Defaults to False.
    data_slice (bool, optional): If True, a slice of the data will be returned. Defaults to False.

    Returns:
    tuple: Contains the sample rate (float), highest frequency (float, in MHz), 
           start time (str, in ISO format), and version (str, dummy value).
    """
    with open(os.path.join(ram_data_dir, orig_file_name), "r") as f:
        metadata = json.load(f)
        
    sample_rate = metadata["global"]["core:sample_rate"]

    start_time_str = metadata["captures"][0]["core:datetime"] # iso 
    start_time = start_time_str #iso
    version = '1' # dummy 
    highest_freq  = metadata['captures'][0]['core:frequency']* 1e-6 # mhz#: 

    return sample_rate, highest_freq, start_time, version


def get_number_of_samples_from_sigmf(filepath, sample_dtype=np.complex64, file_extension='.sigmf-data', ram_data_dir='/data_tmp'):
    """
    Calculate the number of samples in a SigMF binary data file.

    This function reads the size of the binary data file associated with the given
    SigMF filepath and calculates the number of samples based on the specified
    sample data type.

    Parameters:
    ----------
    filepath : str
        The base filepath (without the extension) of the SigMF file. The function
        expects the binary data file to have a '.sigmf-data' extension.
    sample_dtype : numpy.dtype, optional
        The data type of the samples in the binary file. Default is np.complex64.
    file_extension : str, optional 
        File extension to add, default is '.sigmf-data'

    Returns:
    -------
    int
        The number of samples in the binary data file.
    """
    base, ext = os.path.splitext(filepath)
    data_file = base + file_extension
    data_file = os.path.join(ram_data_dir, data_file)
    file_size = os.path.getsize(data_file)
    sample_size = np.dtype(sample_dtype).itemsize
    num_samples = file_size // sample_size
    return num_samples

def delta_t(DM, freq1, freq2, time1, time2, constant=4.149e-3):
    """
    Calculates the time delay between two frequencies due to dispersion.

    Parameters:
    DM (float): Dispersion measure in pc/cm^3.
    freq1 (float): First frequency in GHz.
    freq2 (float): Second frequency in GHz.
    time1 (float): Time at first frequency (not used in calculation).
    time2 (float): Time at second frequency (not used in calculation).
    constant (float, optional): Constant used in the dispersion formula, defaults to 4.149e-3

    Returns:
    float: Arrival Time delay in seconds between the freq1 and freq2.
    """
    DM = float(DM)

    delta_t = constant*DM* ((1/freq1)**2 - (1/freq2)**2) 
    print(f'Correction in seconds: {delta_t}')


def mjd_from_iso(iso_time):
    'Convert ISO time to MJD using astropy time'
    
    t = Time(iso_time, format='isot', scale='utc')
    return t.mjd


def compute_time_offset(sigmf_file1, sigmf_file2, dm, time_candidate, ram_data_dir):
    """
    Computes the time offset between two signals due to dispersion measure (DM),
    and returns an adjusted time_candidate (in mjd) for sigmf_file2

    Parameters:
    sigmf_file1 (str): The first SigMF file name (without extension).
    sigmf_file2 (str): The second SigMF file name (without extension).
    dm (float): Dispersion measure in pc/cm^3.
    time_candidate (tuple): Candidate time tuple containing (stuff, MJD time) for sigmf_file1.
    ram_data_dir (str): Directory where the SigMF files are stored.

    Returns:
    tuple: Adjusted time candidate tuple for sigmf_file2 and the time offset in seconds.
    """
    # Read metadata from both SigMF files
    ext = '.sigmf-meta'
    sample_rate1, center_freq1, start_time1, version1 = read_baseband_data(ram_data_dir, sigmf_file1 + ext)
    sample_rate2, center_freq2, start_time2, version2 = read_baseband_data(ram_data_dir, sigmf_file2 + ext)
    
    # Compute the time offset due to dispersion measure
    freq1 = center_freq1 * 1e-3  # Convert MHz to GHz
    freq2 = center_freq2 * 1e-3  # Convert MHz to GHz
    time_offset = delta_t(dm, center_freq1, center_freq2, start_time1, start_time2,)
    
    # Convert the start times to MJD
    mjd_start1 = mjd_from_iso(start_time1)
    mjd_start2 = mjd_from_iso(start_time2)
    
    # Adjust the time candidate
    stuff, mjd_start1 = time_candidate
    mjd_start2 = mjd_start1 + (time_offset / 86400.0)  # Convert seconds to days for MJD adjustment
    
    return (stuff, mjd_start2), time_offset
    

def extract_snr_and_dm_from_hdf5(file_path):
    """
    Extract the Signal-to-Noise Ratio (SNR) and Dispersion Measure (DM) from the root attributes of an HDF5 file.

    Parameters:
    -----------
    file_path : str
        The path to the HDF5 file from which to extract the SNR and DM values.

    Returns:
    --------
    snr : float
        The Signal-to-Noise Ratio (SNR) value extracted from the root attributes of the HDF5 file.
    dm : float
        The optimal Dispersion Measure (DM) value extracted from the root attributes of the HDF5 file.

    Raises:
    -------
    KeyError
        If the 'snr' or 'dm_opt' attributes are not found in the root attributes of the HDF5 file.
    """
    
    # Open the HDF5 file
    with h5py.File(file_path, 'r') as hdf:
        # Extract and store root attributes
        root_attrs_dict = {attr: hdf.attrs[attr] for attr in hdf.attrs.keys()}

        snr = root_attrs_dict['snr']
        dm = root_attrs_dict['dm_opt']

    return snr, dm


def parse_h5_filename(file_names):
    """
    Extracts metadata from a list of HDF5 file names.

    This function processes each file name in the input list to extract and return the directory, 
    basename, tcand, dm components, band, and fil_file path.
    
    Parameters:
    file_names (list of str): List of full path to HDF5 file names. Each file name is expected to follow the pattern
                              '/data/frb/date/good/basename_tcand_<tcand>_dm_<dm>_snr_<snr>.h5'.
    
    Returns:
    tuple: A tuple containing: file_names, (dir_name, basename, tcand, dm, band, fil_file)
           - file_names (list of str): The original list of file names.
           - results (list of tuples): A list of tuples where each tuple contains:
             - dir_name (str): The directory of the file (empty string if no directory is specified).
             - basename (str): The base name of the file up to `_tcand`.
             - tcand (str): The tcand value extracted from the file name.
             - dm (str): The dm value extracted from the file name.
             - band (str): The band value extracted from the file name.
             - fil_file (str): The corresponding fil_file path based on the extracted band.
             - fil_start, when the fil file started in local time
    """
    results = []
    for file_name in file_names:
        # Extract directory and base file name
        dir_name = os.path.dirname(file_name) # the /data/frb/date/good dir
        date_dir = os.path.dirname(dir_name) # the /data/frb/date dir
        base_file_name = os.path.basename(file_name)
        
        parts = base_file_name.split('_')
        if len(parts) >= 10 and parts[-1].endswith('.h5'):
            basename = parts[0]
            band = '_'.join(parts[1:3])
            fil_start = '_'.join(parts[3:9])
            tcand = parts[-5]
            dm = parts[-3]

            # Construct fil_file path
            path_to_fil_file = os.path.join(date_dir, band,  f"{basename}_{band}_{fil_start}.fil")
            results.append((dir_name, basename, tcand, dm, band, path_to_fil_file, fil_start))
    
    return file_names, results


def read_fil_metadata(file_path):
    """
    Reads metadata from a .fil file and returns it as a tuple.

    # TODO Max Fine, I want to calculate the duration of the .fil file and return it 
    
    Args:
    file_path (str): The path to the .fil file.
    
    Returns:
    tuple: A tuple containing (tstart_mjd, basename, fch1, foff, nchans, tsamp,)

    fch1 = fil.fch1  # Frequency of the first channel
    foff = fil.foff  # Frequency offset between channels
    nchans = fil.nchans  # Number of channels
    tsamp = fil.tsamp  # sampling interval (seconds)
    nbits = fil.nbits # Number of bits the data are recorded in.
    tstart_mjd = fil.tstart  # Start time in MJD
    """
    fil = SigprocFile(file_path)
    
    basename = os.path.basename(file_path)  # Extracting the basename of the file
    fch1 = fil.fch1  # Frequency of the first channel
    foff = fil.foff  # Frequency offset between channels
    nchans = fil.nchans  # Number of channels
    tsamp = fil.tsamp  # sampling interval (seconds)
    nbits = fil.nbits # Number of bits the data are recorded in.
    tstart_mjd = fil.tstart  # Start time in MJD

    # Assuming fil.data is a numpy array containing the data, its size divided by nchans gives the number of samples
    nsamples = np.shape(fil.get_data) # // nchans
    
    return (tstart_mjd, basename, fch1, foff, nchans, tsamp, nbits, nsamples)
    

def find_candidate_time_in_mjd_get_meta(h5_file_names):
    """
    Finds the time of the candidate in MJD using metadata from both .h5 and .fil files.
    
    Parameters:
    h5_file_names (list of str): List of full path to HDF5 file names.
    
    Returns:
    list of tuples: Each tuple contains the file name and the candidate time in MJD.
    """

    _, h5_metadata = parse_h5_filename(h5_file_names)

    # Read metadata from .h5 header 
    snr_list = []
    dm_list = []
    for h5_file in h5_file_names:
        snr, dm = extract_snr_and_dm_from_hdf5(h5_file)
        snr_list.append(snr)
        dm_list.append(dm)

    candidate_times_mjd = []
    for metadata in h5_metadata:
        # Read metadata from the corresponding .fil file
        dir_name, basename, tcand, dm, band, fil_file, fil_start = metadata  
        tstart_mjd, fil_basename, fch1, foff, nchans, tsamp, nbits, nsamples = read_fil_metadata(fil_file)

        # Calculate the time of the candidate
        tcand = float(tcand)
        candidate_time_mjd = tstart_mjd + (tcand ) / (24 * 3600)  # Convert seconds to days
        candidate_times_mjd.append((fil_file, candidate_time_mjd))

    return h5_file_names, h5_metadata, candidate_times_mjd, snr_list, dm_list, fil_start



def mjd_to_datetime(mjd_tuple):
    """
    Converts a Modified Julian Date (MJD) tuple to a datetime object.

    Parameters:
    mjd_tuple (tuple): Tuple containing (stuff, MJD value).

    Returns:
    datetime: Corresponding datetime object for the given MJD.
    """
    mjd = mjd_tuple[1]
    
    return Time(mjd, format='mjd').datetime


def save_baseband_from_h5(h5_file_paths, output_dir, ram_data_dir, delta_t=1, snr_threshold=6):
    """
    Processes HDF5 files to extract and save baseband data, applying time offsets
    based on dispersion measures (DM) and signal-to-noise ratio (SNR) thresholds.

    Parameters:
    h5_file_paths (list): List of paths to the HDF5 files.
    output_dir (str): Directory to save the output baseband data.
    ram_data_dir (str): Directory containing the SigMF metadata files.
    delta_t (float, optional): Duration for the cropped data in seconds. Defaults to 1 second.
    snr_threshold (float, optional): SNR threshold to filter candidates. Defaults to 6.

    """
    bands = ["PH_Band", "L1_Band"]
    ext = ".sigmf-meta"
    # Find candidate times in MJD and get metadata from HDF5 files
    h5_file_names, h5_metadata, candidate_times_mjd, snr_list, dm_list, fil_start = find_candidate_time_in_mjd_get_meta(h5_file_paths)
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for idx in range(len(h5_file_names)):
        cand_time_mjd = candidate_times_mjd[idx]
        snr = snr_list[idx]
        dm = dm_list[idx]
        metadata = h5_metadata[idx]
        file_name = h5_file_names[idx]
        dir_name, basename, tcand, dm, band, fil_file, fil_start = metadata

        
        print(f"Processing h5 file: {file_name}")
        print(f"Candidate time (MJD): {cand_time_mjd[1]} in band {band}, SNR: {snr}, DM: {dm}")


        if snr >= snr_threshold:
            
            for band_i in bands:
                orig_files_primary = [f for f in os.listdir(ram_data_dir) if f.startswith(f"{basename}_{band}") and fil_start in f and f.endswith('.sigmf-meta')]
                orig_files_secondary  = [f for f in os.listdir(ram_data_dir) if f.startswith(f"{basename}_{band_i}") and f.endswith('.sigmf-meta')]
                
                print(f'processing band {band_i}')
                if band_i == band:
                    # Processing the primary band
                    for orig_file in orig_files_primary:
                        orig_file_name = orig_file.replace(".sigmf-meta", "")
                        new_file_name = f"{basename}_{band_i}_{fil_start}_mjd_{cand_time_mjd[1]}_tcand_{tcand}_dm_{dm}_snr_{snr}.sigmf-meta"
                        input_metafilename = os.path.join(ram_data_dir, orig_file)
                        output_metafilename = os.path.join(output_dir, new_file_name)

                        # Read meta info from .sigmf
                        sample_rate, center_freq, start_time, version = read_baseband_data(ram_data_dir, orig_file_name + ext)
                        file_start_time_s = fromisoformat(start_time)  # datetime object
                        
                        # Ensure file_start_time_s is timezone-aware
                        file_start_time_s = file_start_time_s.replace(tzinfo=pytz.UTC)
                        
                        candidate_dt = Time(cand_time_mjd[1], format='mjd').to_datetime()
                        
                        # Ensure candidate_dt is timezone-aware
                        candidate_dt = candidate_dt.replace(tzinfo=pytz.UTC)
                        
                        time_difference = candidate_dt - file_start_time_s

                        # Calculate start and duration for cropping
                        seconds_difference = time_difference.total_seconds()
                        start_s = seconds_difference - 0.5 * delta_t
                        duration_s = delta_t

                        print(f"Cropping SigMF:\n{input_metafilename} -> {output_metafilename}")
                        print(f"Start: {start_s}s, Duration: {duration_s}s")
                        crop_sigmf(input_metafilename, output_metafilename, start_s, duration_s)

                else:
                    # Processing the secondary bands
                    
                    for j, orig_file in enumerate(orig_files_secondary):
                        sigmf_file1 = f"{basename}_{band}_{fil_start}"
                        sigmf_file2 = orig_file.replace(".sigmf-meta", "")
    
                        mjd_start2, time_offset = compute_time_offset(sigmf_file1, sigmf_file2, dm, cand_time_mjd, ram_data_dir)

                        new_file_name = f"{basename}_{band_i}_mjd_{mjd_start2[1]}_tcand_{float(tcand)+time_offset}_dm_{dm}_snr_{snr}" 
                        input_metafilename = os.path.join(ram_data_dir, orig_file)
                        output_metafilename = os.path.join(output_dir, new_file_name)

                        # Read meta info from .sigmf
                        sample_rate, center_freq, start_time, version = read_baseband_data(ram_data_dir, sigmf_file2 + ext)
                        file_start_time_s = fromisoformat(start_time)  # datetime object
                        
                        # Ensure file_start_time_s is timezone-aware
                        file_start_time_s = file_start_time_s.replace(tzinfo=pytz.UTC)
                        
                        candidate_dt = Time(cand_time_mjd[1], format='mjd').to_datetime()
                        
                        # Ensure candidate_dt is timezone-aware
                        candidate_dt = candidate_dt.replace(tzinfo=pytz.UTC)
                        
                        time_difference = candidate_dt - file_start_time_s

                        # Calculate start and duration for cropping
                        seconds_difference = time_difference.total_seconds()
                        start_s = seconds_difference - 0.5 * delta_t
                        duration_s = delta_t

                        output_metafilename += ext 

                        print(f"Cropping SigMF:\n{input_metafilename} -> {output_metafilename}")
                        print(f"Start: {start_s}s, Duration: {duration_s}s")
                        crop_sigmf(input_metafilename, output_metafilename, start_s, duration_s)

            print('\n\n\n')

        else:
            print(f"Rejected h5 file: {file_name} snr {snr} is less then baseband record threshold of {snr_threshold}")

def delete_old_files(directory, time_del):
    """
    Deletes files in the specified directory that are older than the given time delta.
    
    Parameters:
    directory (str): Directory containing the files to delete.
    time_del (timedelta): Time delta to determine the age of files to delete.
    """
    current_time = time.time()
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_age = current_time - os.path.getmtime(file_path)
            if file_age > time_del.total_seconds():
                print(f"Deleting old file: {file_path}")
               # os.remove(file_path)

def process_baseband_h5_files(h5_file_paths, output_dir, ram_data_dir, delta_t=1, snr_threshold=6, time_del=timedelta(minutes=15)):
    """
    Wrapper function to process HDF5 files and manage old files in RAM data directory.

    Parameters:
    h5_file_paths (list): List of paths to the HDF5 files.
    output_dir (str): Directory to save the output baseband data.
    ram_data_dir (str): Directory containing the SigMF metadata files.
    delta_t (float, optional): Duration for the cropped data in seconds. Defaults to 1 second.
    snr_threshold (float, optional): SNR threshold to filter candidates. Defaults to 6.
    time_del (timedelta, optional): Time delta to determine the age of files to delete. Defaults to 5 min.
    """
    try:
        save_baseband_from_h5(h5_file_paths, output_dir, ram_data_dir, delta_t, snr_threshold)
    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()
    finally:
        delete_old_files(ram_data_dir, time_del)
    
