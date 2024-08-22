# Utilizing the 25m Dwingeloo Radio Telescope (DRT) to Study Fast Radio Bursts (FRBs) at ASTRON, the Netherlands 🇳🇱 📡
## Advisors: Dr. Tammo Jan Dijkema & Co-advisor Proffesor Jason Hessels
### This github repo is no longer active, for updates about the pipeline see the [gitlab repo](https://gitlab.camras.nl/dijkema/frbscripts)

> "We look to the stars, but all we find is RFI." - Found on the back of a poster at ASTRON

Over summer 2024, I was a researcher at The Netherlands Institute for Radio Astronomy (ASTRON) with their Summer Research Programme. For my project, I was using and operating the 25-m Dwingeloo radio telescope. I am studing bright repeating Fast Radio Bursts (FRBs) to understand the potential connections between repeating and apparently non-repeating FRBs. As FRBs are hard to catch, I will also observe pulsars to both test the methodology and learn the relevant techniques.

This is me inside the control room, observing with the 25-m Dwingeloo Radio Telescope, and this is a diagnostic plot showing the dynamic spectrum, and some meta data of a possible detection of FRB20240209A I observed on June 26 2024.
<table>
  <tr>
    <td style="text-align: center;">
      <img src="https://afinemax.github.io/afinemax1/images/max_25m_1.jpg" alt="Max Fine Observing with the 25-m Dwingeloo Radio Telescope" width="500">
    </td>
    <td style="text-align: center;">
      <img src="https://afinemax.github.io/afinemax1/images/FRB20240209A_L1_Band_2024_06_26_10_33_18_tcand_297.8789500_dm_183.0_snr_6.1bandpass_corr.png" alt="Diagnostic Plot of a possible detection of FRB20240209A Observed on June 26 2024 by Max Fine" width="500">
    </td>
  </tr>
</table>

### Pipeline GitLab Repo: [Here](https://gitlab.camras.nl/dijkema/frbscripts)

### Big Picture Outline:

The Big Picture of my project is to learn & apply radio astronomy techniques for detecting FRBs. This entails understanding how the radio telescope turns radio signals into 'raw' data (in our case voltages), and then how the 'raw' data is further reduced by a data pipeline. The data pipeline searchs for and cuts out Radio Frequency Interference (RFI), and searchs for possible extragalactic radio signals, at present this is done with the `presto` package.  Part of the Big Idea is to make a series of minor to moderate (or even major) improvements to the search pipeline. If I am very lucky, we will be able to detect a Repeating FRB over summer. However, in the more likely case we will be looking at a bright Pulsar to test as a final 'proof of concept' that the DRT can be used in dedicated campaigns to observe bright repeating FRBs.     

### Final Presentation:
[![YouTube Video](https://img.youtube.com/vi/MA0wCurdQSo/0.jpg)](https://www.youtube.com/watch?v=MA0wCurdQSo&t=1s)


### Table of Contents:
* [reading material](https://github.com/afinemax/Astron_2024/tree/main/important_docs_and_papers)
* [ref sheet of usefull cmds](https://github.com/afinemax/Astron_2024/blob/main/ref_cmds.md)
* [software requirements and versions](https://github.com/afinemax/Astron_2024/blob/main/astron_research_2024.yml)
* [example_pipeline_h5_output](https://github.com/afinemax/Astron_2024/tree/main/example_pipeline__h5_output) contains a notebook that opens a `.h5` file, makes a waterfall plot for practice. Using a `.h5` file made from the pipeline
* [frb_example_data_june_2024](https://github.com/afinemax/Astron_2024/tree/main/frb_example_data_june_2024) contains a notebook making waterfall plots from CHIME `.npy` files, and two notebooks trying out `fitburst` on CHIME data, a simulation and a possible detection of an FRB
* [noise_channels](https://github.com/afinemax/Astron_2024/tree/main/noise_channels) contains several notebooks, and a script that looks at past observations taken and calculutes bad frequency channels to mask
* [inject_sims_into_fil](https://github.com/afinemax/Astron_2024/tree/main/inject_sims_into_fil), contains notebooks and scripts for injecting simulated bursts into `.fil` data for injection testing the pipeline
* [dbcan_clustering](https://github.com/afinemax/Astron_2024/tree/main/dbscan_clustering), contains a notebook for trying out dbscan for clustering candidates in 2d (DM, Time), contains rough code to edit `check_frb.py` to cluster
* [calling_fetch](https://github.com/afinemax/Astron_2024/tree/main/calling_fetch), contains a notebook and a few modified scripts from the gitlab repo. This enables fetch to be called from within `check_frb.py`, as well as moving the candidate `.h5` files into good or bad directors and making dir plots for ones in the good dir
* [ddplan](https://github.com/afinemax/Astron_2024/tree/main/ddplan), contains a notebook trying out `DDplan.py` from presto on my laptop, and the new function that has been incorporated into the pipeline 
* [presto_with_docker](https://github.com/afinemax/Astron_2024/tree/main/running_presto_with_docker), contains a notebook for running, and executing presto commands - with presto running in a docker container 
* [recording_baseband_data](https://github.com/afinemax/Astron_2024/tree/main/recording_baseband_data), contains a notebook for trying to record baseband data, take slices for good candidates, and slices for good candidates in other bands
* [Crab analysis](https://github.com/afinemax/Astron_2024/tree/main/crab_analysis), contains notebooks, and work for analysing the pulses from the crab
* [Final Presentation Slides](https://github.com/afinemax/Astron_2024/blob/main/astron_2024_frb_presentation_1.pdf)
 
### Data Releases:
* If you want any data, just contact me
* [Crab giant pulse detected with the Dwingeloo radio telescope on 2024-07-30](https://zenodo.org/records/13143544)


### Observing (FRBs)
<details>
  <summary><strong>Details:</strong></summary>

####  FRB20240619D:
- See [ATel #16690, detected by MeerKat](https://www.astronomerstelegram.org/?read=16690) and [ATel #16732, detected by Westerbork](https://www.astronomerstelegram.org/?read=16732)
- Expected DM: 465 (pc/cm^3)
- Expected Ra, Dec: 297.37, -25.21 (deg)
- We have limited observation time, typically its up ~23:00 - 04:00, I have to be physically in the telescope to take data...
- I have done a few nights, but no luck yet :((


#### FRB20240316A
- See [ATel #16737 , detected by CHIME](https://www.astronomerstelegram.org/?read=16734)
- Expected DM: 351 (pc/cm^3)
- Expected Ra, Dec: 354.58, 32.38


#### FRB20240209A:

- See [ATel#16670 by Vishwangi Shah (McGill University) on behalf of the CHIME/FRB Collaboration](https://www.astronomerstelegram.org/?findmsg)
- Expected DM: 176 (pc/cm^3)
- Expected RA, Dec: 289.91, 86.06 (deg)
- Observing Cadence: Typically ~07:00-10:00, 11:00-15:00 (UTC) Monday to Friday (I have to be physically in the telescope
- Total of around 200 hours on target. Stopped observing around the 16th of July.
</details>


### Suggestions For Future Work:
- Have the camras mastodon bot post "good" candidates from fetch
	- Send as an email to myself, and Tammo, others as well 
- Add a poster outside of the Camras Telescope to include its FRB research (With a QR code to an engaging video!)
- Try 3d DBscan clustering, taking into account the brightness of the detection (right now its time, and DM)
	- Probably not a substaintial improvement
- Try out Transientx over PRESTO for the pipeline for speed 
- Have Desktop application to click to start program on Mercurius for ease of use 
- Auto stop when storage has less then 20Gb left 
- update FRB.cat file to be in `.key` format 
- Write a comprehensive observation log, including durations, headers, and clustering info 
- When there is a 'hyper-active' FRB, have a camras team try to take many hours of data - I will commute from Amsterdam for this. 
	- Maybe make a post asking for extra volunteers 
- Inject Simulations into `.fil` files to test how many FRBs the pipeline recovers
	- Concern that bright FRB's might be marked as RFI, see unexpectedly low Crab pulses in the bottom right of [this plot](https://github.com/afinemax/Astron_2024/blob/main/crab_analysis/cumulative_snr.png)

### TODO list:
<details>
  <summary><strong>Tasks:</strong></summary>

  ### Completed:
  - [x] Understand how FRB signals from space turn into dynamic spectra. See [flowchart](https://github.com/afinemax/Astron_2024/blob/main/flow_charts/frb_to_dynamic_spectra.pdf).
  - [x] Learn how to operate the 25-m Dwingeloo Radio Telescope.
  - [x] Learn how to use [Presto](https://github.com/scottransom/presto) for single pulse searches and RFI removal.
  - [x] Learn how the current pipeline works (`check_frb.py`). See [flowchart](https://github.com/afinemax/Astron_2024/blob/main/flow_charts/fil_to_dynamic_spectra.pdf).
    - Pipeline GitLab repo: [here](https://gitlab.camras.nl/dijkema/frbscripts)
    - My version of the pipeline: [here](https://github.com/afinemax/frbscripts)
    - [x] Create a file of known bad frequency channels to mask.
    - [x] Modify `start_frb.sh` & `check_frb.py` scripts to load from a catalog file instead of hardcoded sources.
  - [x] Learn how [Fetch](https://github.com/devanshkv/fetch) works and implement it into the pipeline.
    - Fetch is installed and working on Uranus!
  - [x] Learn how [TransientX](https://github.com/ypmen/TransientX) works.
  - [x] Understand what Burst Parameters can be observed & measured directly, and which ones can be inferred.
	- List out model components from FITBURST, polarization, fluence, etc.
  - [x] Understand how to use [fitburst](https://github.com/CHIMEFRB/fitburst).
  - [x] Compare pipeline outputs when using the `--ignorechan` flag in  `check_frb.py`
  - [x] Try using `fitburst` on the CHIME data I have, simulated data, and my possible detection of FRB20240209A.
  - [x] Try a clustering algorithm for reducing the total number of candidates (e.g. DBSCAN).
  - [x] Implement dbscan clustering into `check_frb.py`
	- Reduces number of candidates by ~ the number of DM trials
  - [x] Modify the scrits to record observations on Uranus (instead of Mercurius)
	- Paul, and Tammo did this, plugging in some cabels and running a data stream from mercurius to uranus
	- can record L and P bands directly onto Uranus
  - [x] Modify `check_frb.py` to run `fetch`, and move the files into the good and bad dirs, make diagnostic `.png`s
  - [x] Add back log file for candidates
	- Added a `#header`
  - [x] Added a log file for pipeline crashes
  - [x] Added observing time, and number of good candidates to `frb_dashboard.py`
  - [x] Work on making the pipeline run in real time
        - [x] Modify storage location of `.fil` files from `/date` to `/date/>bandname<` for runnning the pipeline in real time
                - [x] Modify `frb_dashboard.py` for the new file organization
        - [x] Make a `good` dir to hold all the good `.h5` and `.png` files located at `/date/good`
- [x] Figure out what causes the pipeline to crash, and adjust the number of CPU cores as needed 
        - [x] `dashboard.py` was using all the CPUS... fixed
        - [x] Limit GPU to one call of `fetch`
        - Good CPU limit seems around 12 per band?, No noticable increase after this
        - Still crashes, L1 and L2 recording seems unstable
  - [x] Double Check `if` statments for `--ignorechan` option in `check_frb.py` 
  - [x] Look into making simulated, injecting simulations into `.fil` files for testing.
	- `fitburst` has a cool `simulate_burst.py` script that can simulate dedispersed or dispersed dynamic spectrums
	- [will](https://github.com/josephwkania/will/tree/master) is a simulator that can be used to inject (and extract!) simulated pulses into `.fil` files!
        - [ ] Struggling on controlling the amplitude (SNR) of the injected signal, talked to Dirk who offered advice but haven't worked on this in a while  
- [x] record raw voltages
	- [x] Understand how to record raw voltages aka baseband data
	- [x] Wrote function to slice a small chunk of data into a new file for a candidate 
	- [x] Write a function to convert arrival times for different frequency bands based on the DM
	- [x] Write function to loop through candidates, and then delete the big baseband files
        - [x] Implement into pipeline
	- [x] Added storage on ram disk to `frb_dashboard.py`
	- [x] Test
  - [x] Read how the `single_pulse_search` works in `presto`, and how it determines the SNR
        - How it determines SNR
        - what time it uses for the time of the candidate (it is topocentric, top of band)
        - How many, and what size time boxcars in the search

- [x] Analysis of the Crab Pulsar (see [Crab analysis](https://github.com/afinemax/Astron_2024/tree/main/crab_analysis):
	- Make plots of SNR, Fluence, $E_{\nu}$ for the crab over many hours of observations
	- Compare to 2019, 2024 Crab paper, and Nature Paper
	- Addtionaly make some stastical plots of the Crab in the different Bands
	
 
  ### To Do: 
  - [ ]Implement [TransientX](https://github.com/ypmen/TransientX) into the pipeline.
        - Waiting for it to be installed on Uranus.

  - [ ] Write documenation for pipelines, new flowcharts
  - [ ] Understand what Paul and Tammo did to have the data record on Uranus
  - [ ] write an introduction section on `FRBS`, the DRT, and our observational parameters (bandwidth, devices, data points per second etc)
  - [ ] Fill in black boxes in the flowcharts.
	- Look into how `presto` actually removes RFI and finds pulses.
        - Look into how candidates are extracted from the `.fil` file.
  - [ ] Make a 'hip' mastodon bot to display the pngs from the good candidates
	- [ ] maybe make the pngs nan out detected RFI  
  - [ ] Make a script to make `.h5` files with full resolution for a good fetch candidate.
  - [ ] Injection testing the pipeline.
  - [ ] Test the pipeline on Crab or Pulsar and compare the number of recovered vs. missed bursts.
  	- This would be a good test for our clustering methodology as well. 
  - [ ] Combine data with other telescopes to measure fringes/localization.
  - [ ] Maybe make a docker container version of the pipeline.
  - [ ] Read more FRB papers.
  - [ ] Make nicely formatted documentation for the pipeline. 
  - [ ] Understand what happens when intra-channel Dispersion is dominate. 
  - [ ] Understand how our FRB search and CHIME's differ, IE with many antennas .
  - [ ] Make 'hip' popular science videos on research
  - [ ] Understand Red vs White Noise.
</details>


## License

[GPL-3.0](https://github.com/afinemax/Astron_2024/blob/main/LICENSE)
