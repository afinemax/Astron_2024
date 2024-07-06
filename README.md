
# Hunting for Fast Radio Bursts (FRBs) with the 25-m Dwingeloo Radio Telescope (DRT) at ASTRON, the Netherlands 🇳🇱 📡
## Advisors: Dr. Tammo Jan Dijkema & Co-advisor Proffesor Jason Hessels

> "We look to the stars, but all we find is RFI." - Found on the back of a poster at ASTRON

In summer 2024, I am a researcher at The Netherlands Institute for Radio Astronomy (ASTRON) with their Summer Research Programme. For my project, I will be using and operating the 25-m Dwingeloo radio telescope. I will study bright repeating Fast Radio Bursts (FRBs) to understand the potential connections between repeating and apparently non-repeating FRBs. As FRBs are hard to catch, I will also observe pulsars to both test the methodology and learn the relevant techniques.

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


### This Repo Contains:
Important scripts, notebooks, notes, and flow charts + any presentations for my summer research. 

* [example_pipeline_h5_output](https://github.com/afinemax/Astron_2024/tree/main/example_pipeline__h5_output) contains a notebook that opens a `.h5` file, makes a waterfall plot for practice. Using a `.h5` file made from the pipeline
* [frb_example_data_june_2024](https://github.com/afinemax/Astron_2024/tree/main/frb_example_data_june_2024) contains a notebook making waterfall plots from CHIME `.npy` files, and two notebooks trying out `fitburst` on CHIME data, a simulation and a possible detection of an FRB
* [noise_channels](https://github.com/afinemax/Astron_2024/tree/main/noise_channels) contains several notebooks, and a script that looks at past observations taken and calculutes bad frequency channels to mask
* [inject_sims_into_fil](https://github.com/afinemax/Astron_2024/tree/main/inject_sims_into_fil) , contains notebooks and scripts for injecting simulated bursts into `.fil` data for injection testing the pipeline
## Big Picture Outline:

The primary goal of my project is to learn and apply radio astronomy techniques for detecting Fast Radio Bursts (FRBs). This involves understanding how radio telescopes convert radio signals into 'raw' data and how this raw data is processed through a data pipeline into science ready products. The pipeline is responsible for identifying and removing Radio Frequency Interference (RFI) and searching for potential extragalactic radio signals (currently using  `presto`, and `fetch`). A key objective is to implement a series of improvements, ranging from minor to major, in the search pipeline to increase its speed, and detection ability. Another objective is to test the pipeline so we can quantify how well it works. Ideally, we aim to detect a Repeating FRB over the summer. However, it is more likely that we will observe a bright pulsar as a final proof of concept that the DRT can be used to observe bright repeating FRBs.

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
  - [x] Try using `fitburst` on the CHIME data I have, simulated data, and my possible detection of FRB20240209A.

  ### In Progress:
  - [ ] Modify the `start_frb.sh` script to record observations on Uranus & Mercurius computers.
	- Awaiting help from Paul & CAMRAS for cables connecting Uranus to Mercurius.
  - [ ] Implement [TransientX](https://github.com/ypmen/TransientX) into the pipeline.
	- Waiting for it to be installed on Uranus.
  - [x] Compare pipeline outputs when using the `--ignorechan` flag.
  - [x] Look into making simulated, injecting simulations into `.fil` files for testing.
	- `fitburst` has a cool `simulate_burst.py` script that can simulate dedispersed or dispersed dynamic spectrums, not sure how to inject those into `.fil` files.
	- [will](https://github.com/josephwkania/will/tree/master) is a simulator that can be used to inject (and extract!) simulated pulses into `.fil` files!
  - [x] Observe FRBs, and likely pulsars. Observing repeating FRB20240209A. See [ATel#16670 by Vishwangi Shah (McGill University) on behalf of the CHIME/FRB Collaboration](https://www.astronomerstelegram.org/?read=16670).
  - [x] Try a clustering algorithm for reducing the total number of candidates (e.g. DBSCAN).
  ### To Do:
  - [ ] Fill in black boxes in the flowcharts.
	- Look into how `presto` actually removes RFI and finds pulses.
        - Look into how candidates are extracted from the `.fil` file.
  - [ ] Maybe make `.h5` files with full resolution instead of modified for fetch.
  - [ ] Injection testing the pipeline.
  - [ ] Test the pipeline on Crab or Pulsar and compare the number of recovered vs. missed bursts.
  - [ ] Combine data with other telescopes to measure fringes/localization.
</details>



## License

[GPL-3.0](https://github.com/afinemax/Astron_2024/blob/main/LICENSE)
