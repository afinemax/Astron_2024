#!/usr/bin/env python3
# Author Maxwell Fine Jul 9th 2024
# Contact https://afinemax.github.io/afinemax1/#contact

# imports
import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score # metric for how well dbscan worked
import pandas as pd
from sklearn.preprocessing import StandardScaler
from matplotlib.colors import ListedColormap
from your.candidate import Candidate


def load_and_concat_single_pulse_files(single_pulse_files_list):
    '''
    Load multiple single pulse files into a single pandas DataFrame.

    Parameters:
    - single_pulse_files_list (list): List of Paths to single pulse files.

    Returns:
    - pd.DataFrame: A concatenated DataFrame containing data from all single pulse files.
    '''
    # Create a list of DataFrames using a list comprehension
    dfs = [pd.read_csv(pulse_file, comment='#', sep='\s+', 
                       names=['DM', 'Sigma', 'Time (s)', 'Sample', 'Downfact']) 
           for pulse_file in single_pulse_files_list]

    # Concatenate all DataFrames
    master_df = pd.concat(dfs, ignore_index=True)
    
    return master_df


def rescale_dm(master_df, ddm=1/1500):
    '''
    Rescale the 'DM' column in a pandas DataFrame according to a specified differential DM (ddm) value.

    Parameters:
    master_df (pd.DataFrame): A pandas DataFrame containing 'DM' and 'Time (s)' columns of all the candiates.
    ddm (float): The desired separation in dm units (pc/cm^3) after rescaling. Default is 1/1500.

    Returns:
    pd.DataFrame: The DataFrame with an additional column 'rescaled_DM' containing the rescaled DM values.
    '''
    
    if master_df.empty:
        raise ValueError("The input DataFrame is empty")
        
    if 'DM' not in master_df.columns or 'Time (s)' not in master_df.columns:
        raise ValueError("The input DataFrame must contain 'DM' and 'Time (s)' columns")

    raw_data = np.asarray(master_df[['DM', 'Time (s)']])

    # Estimate separation in dm
    raw_ddm = (np.max(raw_data[:, 0]) - np.min(raw_data[:, 0])) / (np.size(raw_data[:, 0]) - 1)

    if raw_ddm == 0:
        raise ValueError("The 'DM' values are constant, cannot rescale")

    # Calculate the scaling factor
    scaling_factor = ddm / raw_ddm

    # Find Time range, and center
    time_center = 0.5* (np.max(raw_data[:,1]) + np.min(raw_data[:,1]) )
    time_range = np.max(raw_data[:,1]) - np.min(raw_data[:,1])

    # Find Dm range, and center
    dm_center = 0.5* (np.max(raw_data[:,0]) + np.min(raw_data[:,0]) )
    dm_range = np.max(raw_data[:,0]) - np.min(raw_data[:,0])


    # Center DM on 0
    # rescale the range of DM to be the range of time * scaling_factor
    # Add rescaled_dm back into pandas df
    raw_data[:,0] = ((raw_data[:,0] - dm_center ))/ dm_range
 
    master_df['rescaled_DM'] = scaling_factor * raw_data[:, 0]

    return master_df


def dbscan_clustering(master_df, ddm=1/1500, eps=1/1000, min_samples=3, silhouette=False):
    """
    Perform DBSCAN clustering on a given DataFrame and optionally compute the silhouette score, performs the rescaling of dm. 

    Parameters:
    master_df (pd.DataFrame): A pandas DataFrame containing the data to be clustered. Must include 'rescaled_DM' and 'Time (s)' columns.
    ddm (float): The desired separation in dm units (pc/cm^3) after rescaling. Default is 1/1500.
    eps (float): The maximum distance between two samples for one to be considered as in the neighborhood of the other. Default is 1/1000.
    minsamples (int): The number of samples (or total weight) in a neighborhood for a point to be considered as a core point. Default is 3.
    silhouette (bool): If True, compute and return the silhouette score. Default is False. See 
    https://en.wikipedia.org/wiki/Silhouette_(clustering), a score of ~0.7> means good. 

    Returns:
    pd.DataFrame: The original DataFrame with an added column 'cluster_labels' indicating the cluster assignment for each sample.
    float (optiin
    """

    master_df = rescale_dm(master_df, ddm=ddm) # rescale dm

    data = np.asarray(master_df[['rescaled_DM', 'Time (s)']])
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    clustering = dbscan.fit(data)
    cluster_labels = clustering.labels_

    # Add labels back into pandas df
    # -1 is noise
    master_df['cluster_labels'] = cluster_labels

    # Compute the silhouette score
    if silhouette:
        if len(set(cluster_labels)) > 1:
            silhouette_avg = silhouette_score(data, cluster_labels)
        else:
            silhouette_avg = -1  # Silhouette score is not defined for a single cluster
        return master_df, silhouette_avg
    else:
        return master_df


def get_candidates(master_df, ddm=1/1500, eps=1/1000, min_samples=3, silhouette=False, include_outliers=True):
    """
    Perform DBSCAN clustering on the given DataFrame and return candidates with the highest 'Sigma' values 
    from each cluster.

    Parameters:
    - master_df (pd.DataFrame): A pandas DataFrame containing the data to be clustered. Must include 'DM', 'Sigma', 
      and 'Time (s)' columns.
    - ddm (float): The desired separation in DM units (pc/cm^3) after rescaling. Default is 1/1500.
    - eps (float): The maximum distance between two samples for one to be considered as in the neighborhood 
      of the other. Default is 1/1000.
    - min_samples (int): The number of samples (or total weight) in a neighborhood for a point to be considered 
      as a core point. Default is 3.
    - silhouette (bool): If True, compute and return the silhouette score. Default is False.
    - include_outliers (bool): If True, include outliers (cluster label -1) in the result. Default is True.

    Returns:
    - pd.DataFrame: A DataFrame containing the candidates with the highest 'Sigma' values from each cluster.
    - float (optional): The silhouette score of the clustering if `silhouette` is True.

    Notes:
    - The function first performs rescaling of the 'DM' column using the specified `ddm` value.
    - DBSCAN clustering is applied to the rescaled data.
    - The row with the highest 'Sigma' value is selected from each cluster.
    - If `include_outliers` is False, rows labeled as outliers by DBSCAN (label -1) are excluded from the result.
    - If `silhouette` is True and the number of clusters is greater than one, the silhouette score is computed 
      and returned along with the DataFrame.
    """
    
    master_df = dbscan_clustering(master_df, ddm=ddm, eps=eps, min_samples=min_samples, silhouette=silhouette)

    # Group by 'cluster_labels' and find the row with the max 'Sigma' for each group
    cluster_labels = master_df['cluster_labels'].to_numpy()
    sigmas = master_df['Sigma'].to_numpy()
    unique_labels = np.unique(cluster_labels)
    print(len(unique_labels))

    indices = []
    for label in unique_labels:
        if label == -1 and not include_outliers:
            continue
        mask = cluster_labels == label
        max_sigma_index = np.argmax(sigmas[mask])
        indices.append(np.where(mask)[0][max_sigma_index])

    result = master_df.iloc[indices].reset_index(drop=True)

    return result
