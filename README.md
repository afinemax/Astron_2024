# Hunting for Fast Radio Bursts (FRBs) with the 25-m Dwingeloo Radio Telescope (DRT) at ASTRON, the Netherlands 🇳🇱 📡
## Advisors: Dr. Tammo Jan Dijkema & Co-advisor Proffesor Jason Hessels

> "We look to the stars, but all we find is RFI." - Found on the back of a poster at ASTRON

Over summer 2024, I am a researcher at The Netherlands Institute for Radio Astronomy (ASTRON) with their Summer Research Programme. For my project, I am using and operating the 25-m Dwingeloo radio telescope. I am studing bright repeating Fast Radio Bursts (FRBs) to understand the potential connections between repeating and apparently non-repeating FRBs. As FRBs are hard to catch, I will also observe pulsars to both test the methodology and learn the relevant techniques.

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

### [Pipeline GitLab Repo:](https://gitlab.camras.nl/dijkema/frbscripts)


### Big Picture Outline:

The Big Picture of my project is to learn & apply radio astronomy techniques for detecting FRBs. This entails understanding how the radio telescope turns radio signals into 'raw' data (in our case voltages), and then how the 'raw' data is further reduced by a data pipeline. The data pipeline searchs for and cuts out Radio Frequency Interference (RFI), and searchs for possible extragalactic radio signals, at present this is done with the `presto` package.  Part of the Big Idea is to make a series of minor to moderate (or even major) improvements to the search pipeline. If I am very lucky, we will be able to detect a Repeating FRB over summer. However, in the more likely case we will be looking at a bright Pulsar to test as a final 'proof of concept' that the DRT can be used in dedicated campaigns to observe bright repeating FRBs.     

### Currently Observing:

#### FRB20240209A:

- See [ATel#16670 by Vishwangi Shah (McGill University) on behalf of the CHIME/FRB Collaboration](https://www.astronomerstelegram.org/?read=16670).
- Expected DM: 176 (pc/cm^3)
- Expected RA, Dec: 289.91, 86.06 (deg)
- Observing Cadence: Typically ~07:00-10:00, 11:00-15:00 (UTC) Monday to Friday (I have to be physically in the telescope hut) 

  

### Table of Contents:
* [example_pipeline_h5_output](https://github.com/afinemax/Astron_2024/tree/main/example_pipeline__h5_output) contains a notebook that opens a `.h5` file, makes a waterfall plot for practice. Using a `.h5` file made from the pipeline
* [frb_example_data_june_2024](https://github.com/afinemax/Astron_2024/tree/main/frb_example_data_june_2024) contains a notebook making waterfall plots from CHIME `.npy` files, and two notebooks trying out `fitburst` on CHIME data, a simulation and a possible detection of an FRB
* [noise_channels](https://github.com/afinemax/Astron_2024/tree/main/noise_channels) contains several notebooks, and a script that looks at past observations taken and calculutes bad frequency channels to mask
* [inject_sims_into_fil](https://github.com/afinemax/Astron_2024/tree/main/inject_sims_into_fil), contains notebooks and scripts for injecting simulated bursts into `.fil` data for injection testing the pipeline
* [dbcan_clustering](https://github.com/afinemax/Astron_2024/tree/main/dbscan_clustering), contains a notebook for trying out dbscan for clustering candidates in 2d (DM, Time), contains rough code to edit `check_frb.py` to cluster
* [calling_fetch](https://github.com/afinemax/Astron_2024/tree/main/calling_fetch), contains a notebook and a few modified scripts from the gitlab repo. This enables fetch to be called from within `check_frb.py`, as well as moving the candidate `.h5` files into good or bad directors and making dir plots for ones in the good dir
## TODO list:

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
  - [x] Modify the scrits to record observations on Uranus (instead of Mercurius)
	- Paul, and Tammo did this, plugging in some cabels and running a data stream from mercurius to uranus
	- can record L and P bands directly onto Uranus

  ### In Progress:
  - [ ] Implement [TransientX](https://github.com/ypmen/TransientX) into the pipeline.
	- Waiting for it to be installed on Uranus.
  - [ ] Fix `if` statments for `--ignorechan` option in `check_frb.py` 
  - [x] Look into making simulated, injecting simulations into `.fil` files for testing.
	- `fitburst` has a cool `simulate_burst.py` script that can simulate dedispersed or dispersed dynamic spectrums
	- [will](https://github.com/josephwkania/will/tree/master) is a simulator that can be used to inject (and extract!) simulated pulses into `.fil` files!
        - Struggling on controlling the amplitude (SNR) of the injected signal  
  - [ ] Use `ddplan` from `presto` to dynamically select how many DM trials the pipeline needs 
  - [x] Modify `check_frb.py` to run `fetch`, and move the files into the good and bad dirs, make diagnostic `.png`s
	- Just waiting for my previous merge request to go through, and then I can make a new one
	- running `predict.py` while recording data to uranus causes the data recording to crash
	- Need to fancy fancy way of moving to the unique `/process/good` dirs
 - [ ] Add back log file for candidates
 - [ ] Work on making the pipeline run in real time
	- Figure out how many CPUs I can use before I cause the IQ stuff to crash
	- Modify storage location of `*.h5` candidate files from `/process` to `/process/>bandname<` for runnning `fetch`
        - storage managment
                - delete older data to make space for new data
                - keep data corresponding to good candidates 
                - have option to save all the `fil` files
        - record raw voltages
 
  ### To Do: 
  - [ ] Understand what Paul and Tammo did to have the data record on Uranus
  - [ ] write an introduction section on `FRBS`, the DRT, and our observational parameters (bandwidth, devices, data points per second etc)
  - [ ] Fill in black boxes in the flowcharts.
	- Look into how `presto` actually removes RFI and finds pulses.
        - Look into how candidates are extracted from the `.fil` file.
  - [ ] Make a 'hip' mastodon bot to display the pngs from the good candidates
	- [ ] maybe make the pngs nan out detected RFI  
  - [ ] Make a script to make `.h5` files with full resolution for a good fetch candidate.
  - [ ] Injection testing the pipeline.
  - [ ] Make a script that can looks for detection parameters of other radio telescopes over the same time we were observing 
  - [ ] Test the pipeline on Crab or Pulsar and compare the number of recovered vs. missed bursts.
  	- This would be a good test for our clustering methodology as well. 
  - [ ] Combine data with other telescopes to measure fringes/localization.
  - [ ] Maybe make a docker container version of the pipeline.
  - [ ] Understand Red vs White Noise.
</details>



## License

[GPL-3.0](https://github.com/afinemax/Astron_2024/blob/main/LICENSE)
