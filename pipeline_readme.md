#  25m Dwingeloo Radio Telescope (DRT) real time Fast Radio Burst (FRB) Detection Pipeline

See [Observation Instructions] for how to use this pipeline to look for FRBs



## Overview:

![FRB Pipeline](https://raw.githubusercontent.com/afinemax/Astron_2024/main/FRB%20Pipeline.png)


The pipeline records data in 4 bands: PH, PV, L1, L2, - as `.fil` files. After the `.fil` is finished being written a search over the `.fil` is performed by `check_frb.py`. This program cuts out a lot of RFI, and searches a dedispersed time series for single pulses. This is all done with `presto`. After the single pulse search is performed, we cluster candidates. Clustering reduces the number of candiates seend multiple times. `fetch` then sorts the candidates into "good" and "bad". If there are any "good" candidates, we save baseband data - not only for the band where the candidate was found; but, also all the other bands. 


## Search Parameters:
	- SNR detection threshold of 6 is used
	- 30s integration time used for `rfifind` 
	- boxcar sizes are [1, 2, 3, 4, 6, 9, 14, 20, 30] for `single_pulse_search.py`
	- DBscan clustering uses ddm=0.0001, eps=0.01, min_samples=3
	- If there are more than 800 candidates _after_ clustering, the file is skipped
	- Fetch uses model "m", and 50% as the probabililty threshold
	- 2s of baseband data is recorded for each "good" detection by fetch
## `start_frb.sh`

This is the start up script. By default it alots 12 CPU cores to each _instance_ of `check_frb`

This program does 5 things:

- Runs `/get_frb_from_pointing.py` to check that we are on target
- Cheks if we are already recording data, and if so does nothing else
- Starts the recording of filterbank data `screen` sessions named "filterbank_*band"
	- the `screen` sessions themselves run the `filterbank-*band.sh` programs
- Starts `clear_ram_dir` program. This deletes all files older than 15 minutes from `/data_tmp`  .   `/data_tmp` is a ram buffer, that we write baseband data to
- Starts `usrp-lband.sh` in a nammed `screen` 
- SSH's into `camrasdemo@mercurius` and starts `usrp-pband.sh` in a named screen
- Starts the `frb_dashboard.py` program

## `check_frb.py`

This is the *primary script*. This program searches for FRBs in the `.fil` data, saves baseband data, and produces diagnostic plots.

Outline:

	Presto Calls:
	It is reconmended to look over the presto tutorial located [here](https://github.com/afinemax/Astron_2024/blob/main/important_docs_and_papers/PRESTO_search_tutorial.pdf). The presto calls are done with the subprocess module.  
	- `DDplan.py` is used to come up with the dedispersion plan
		- `DDplan.py -d {high_dm} -l {low_dm} -n {numchan} -b {BW} -t {dt} -f {fctr}`
		- high and low dm are +/- 10% of target dm listed in `frb.cat`, info about observation is read in from `.fil`
	        - Used to find `n_DMS` - the number of DM trials to use between our high and low DM for dedispersesing the data 
	
	- `rfifind` is used to cutout RFI
		- `rfifind -ncpus {ncpu} -o {outname} {filterbankfile} -time {time}`
                - optionally also `"rfifindoption = "-mask " + outname + "_rfifind.mask"`
		- 30s is used by default for RFI find

	- `prepsubband` dedisperses the data
		- `"prepsubband -ncpus {ncpu} {noclip_option} {zerodmoption} {ignorechanoption} {rfifindoption} -nsub {nchan} -lodm {low_dm} -dmstep {str(dDM)} -numdms {n_DMS} -o {outname} -nobary {filterbankfile} "`
		- produces the `*.dat` files
	- `single_pulse_search.py` is used to search the dedispersed data
		- `"single_pulse_search.py -b -t {threshold} {outname}*.dat`
		- "The search attempts to find pulses by matched-filtering the data with
                  a series of different width boxcar functions.  The possible boxcar
                  sizes are [1, 2, 3, 4, 6, 9, 14, 20, 30, 45, 70, 100, 150, 220, 300]
                  bins.  By default the boxcars <= 30 are used." - single_pulse_search.py 
		- writes output to "{basename}_DM*.singlepulse" (1 per DM trial)
		
	Clustering of Candidates:
	Bright RFI, and FRBs will appear in multiple DM trails of `single_pulse_search.py`, we can (attempt) to cluster the candidates over all the trails instead of looking at all of them. 
	- see `dbscan_clustering.py` file 
	- we load and concatenate all of the trials together, and do a DBscan 2d clustering across time and DM space. 
	- We rescale the DM range to be ~ an order of magnitude closer together than the time samples - this helps force candiadtes from multiple DM trails to be seen as one cluster
	- eps of 0.01 (in time space, so seconds) is used. 
	- ddm=0.0001, eps=0.01, min_samples=3
	- *Important* after clustering if there are more than 800 candidates the file is ignored. It is not processed further 
	- if there are less then 800 candidates, the `.h5` candidate files are produced
	- A log file is written with the `.fil` name and how many candidates before and after clustering.  

	Sorting with fetch:
	Fetch is a machine learning program that inSee [Fetch](https://github.com/devanshkv/fetch). It sorts candidate `.h5` files into "good" and "bad".
	- See `run_predict_and_move` function
	- model 'm' is used, and the default threshold of 50%
	- The `fetch` call itself uses a lockfile to insure that only one instance is running at a time. This the GPU from causing a crash
	- This function also moves the files into the "good" and "bad" dirs, and saves baseband data, and produces diagnostic plots 


	Saving Baseband Data:
	- located in the `run_predict_and_move` function
	- if there are "good" candidates found by fetch runs
	- See `process_baseband_h5_files` function and `crop_sigmf_utils` file 
	- Saves 2 seconds worth of data centered on the found candidate, attemps to slice out and save corresponding data in the other bands  
	- snr threshold of 6 hardcoded for all targets except CRAB which uses an SNR of 190

	Diagnostic Plotting:
	- runs _after_ saving the baseband data to save time 
	- if there are "good" candidates, produces diagnostic `.pngs` of the contents of the `.h5` file for human review
	
	Logging:

## `stop_frb.sh`
This is the end script. This program kills all the top level screen sessions started by `start_frb.sh`
- Does not kill any screen sessions running 'check_frb'
- Does not kill the screen session writing baseband data (but it does kill the one deleting data from `/data_tmp`)

## Suggestions for Future Improvement:
- Have the camras mastodon bot post "good" candidates from fetch
	- Send as an email to Max, and Tammo, others as well
- Add a poster outside of the Camras Telescope to include its FRB research (With a QR code to an engaging video!)
- Try 3d DBscan clustering, taking into account the brightness of the detection (right now its time, and DM)
    - Probably not a substaintial improvement
- Try out Transientx over PRESTO for the pipeline for speed
- Have Desktop application to click to start program on Mercurius for ease of use
- Auto stop when storage has less then 20Gb left
- update FRB.cat file to be in .key format
- Write a comprehensive observation log, including durations, headers, and clustering info
- When there is a 'hyper-active' FRB, have a camras team try to take many hours of data - I will commute from Amsterdam for this.
    - Maybe make a post asking for extra volunteers
- Inject Simulations into .fil files to test how many FRBs the pipeline recovers
- Concern that bright FRB's might be marked as RFI, see unexpectedly low Crab pulses in the bottom right of this plot


## Known issues & Limitations:

## Installation:

In order to use this, you will need to have installed [Fetch](https://github.com/devanshkv/fetch), and [Presto](https://github.com/scottransom/presto). Our version of `presto` uses a modified version of `ddplan.py` to supress plotting.  
    
## Authors:

- [@@thomas](https://gitlab.camras.nl/thomas)
- [@dijkema](https://gitlab.camras.nl/dijkema)
- [@afinemax](https://www.github.com/afinemax)


## Contributing:

Contributions are always welcome!

Reach out to [@dijkema](https://gitlab.camras.nl/dijkema) 

## Feedback:

If you have any feedback, please reach out to us. This could be bugs, suggestions for features etc. 


## Acknowledgements:

A big thank you to Astron & Jive, who hired [Max Fine](https://www.github.com/afinemax) under the advisors of Dr. Dr. Tammo Jan Dijkema & Co-advisor Proffesor Jason Hessels to work on this pipeline as a summer 2024 project. 


![Logo](https://www.camras.nl/wp-content/themes/camras-enfold-child/images/camras-footer-logo.png)

