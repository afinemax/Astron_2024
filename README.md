
# Hunting for Fast Radio Bursts (FRBs) with the 25-m Dwingeloo radio telescope at ASTRON, the Netherlands 🇳🇱 📡
## Advisors: Dr. Tammo Jan Dijkema & Co-advisor Proffesor Jason Hessels
In summer 2024, I am a researcher at The Netherlands Institute for Radio Astronomy (ASTRON) with their Summer Research Programme. For my project, I will be using and operating the 25-m Dwingeloo radio telescope. I will study bright repeating Fast Radio Bursts (FRBs) to understand the potential connections between repeating and apparently non-repeating FRBs. As FRBs are hard to catch, I will also observe pulsars to both test the methodology and learn the relevant techniques.

This is me inside the control room, observing with the 25-m Dwingeloo Radio Telescope.
![Max Fine Observing with the 25-m Dwingeloo Radio Telescope](https://afinemax.github.io/afinemax1/images/max_25m_2.jpg)

This is a diagnostic plot showing the dynamic spectrum, and some meta data of possible detection of FRB20240209A Observed on June 26 2024
![Diagnostic Plot of a possible detection of FRB20240209A Observed on June 26 2024 by Max Fine](https://afinemax.github.io/afinemax1/images/FRB20240209A_L1_Band_2024_06_26_10_33_18_tcand_297.8789500_dm_183.0_snr_6.1bandpass_corr.png)


### This repo contains:
Important scripts, notebooks, notes, and flow charts + any presentations for my summer research. 

* [example_pipeline_h5_output](https://github.com/afinemax/Astron_2024/tree/main/example_pipeline__h5_output) contains a notebook that opens a `.h5` file, makes a waterfall plot for practice. Using a `.h5` file made from the pipeline
* [frb_example_data_june_2024](https://github.com/afinemax/Astron_2024/tree/main/frb_example_data_june_2024) contains a notebook making a waterfile plot from CHIME data stored as `.npy` files
* [noise_channels](https://github.com/afinemax/Astron_2024/tree/main/noise_channels) contains several notebooks, and a script that looks at past observations taken and calculutes bad frequency channels to mask
## Roadmap 

- [x] Understand how FRB signals from space turn into dynamic spectra (i.e., how telescopes record data and how analysis pipelines work). See [flowchart](https://github.com/afinemax/Astron_2024/blob/main/flow_charts/frb_to_dynamic_spectra.pdf).
  - [ ] Fill in black boxes in the flowchart.

- [x] Learn how to operate the 25-m Dwingeloo Radio Telescope.

- [x] Learn how to use [Presto](https://github.com/scottransom/presto) to conduct a single pulse search and remove RFI.

- [x] Learn how the current pipeline works (`check_frb.py`). See [flowchart](https://github.com/afinemax/Astron_2024/blob/main/flow_charts/fil_to_dynamic_spectra.pdf).
  - The pipeline GitLab repo is [here](https://gitlab.camras.nl/dijkema/frbscripts).
  - My version of of the pipeline is [here](https://github.com/afinemax/frbscripts)
  - [x] Create a file of known bad frequency channels from observed data to mask out using the `-ignorechan` option in the pipeline.
  - [x] Modify the `start_frb.sh` & `check_frb.py` scripts to load in a catalog file instead of using hardcoded known sources
  - [ ] Modify the `start_frb.sh` script to record observations on the Uranus & Mercurius computers.

- [x] Learn how [Fetch](https://github.com/devanshkv/fetch) works and implement into the pipeline.
	- Fetch is already installed and working on uranus!
 
- [x] Learn how [TransientX](https://github.com/ypmen/TransientX) works
	- [ ] implement them into the pipeline.

- [ ] Understand what Burst Parameters we can observe & measure directly, and which ones we can infer

- [ ] Understand how to use [fitburst](https://github.com/CHIMEFRB/fitburst)
  - [ ] Try using [fitburst](https://github.com/CHIMEFRB/fitburst) on the CHIME data I have

- [ ] Try a Clustering algorithim for candidiates? Look into Db scan

- [ ] Test pipeline on Crab or Pulsar and see how many Bursts we recover vs miss

- [ ] Injection Testing the pipeline 

- [ ] Try combining data with those from other telescopes to measure fringes / localization

- [x] Observe FRBs, but more likely pulsars.
	- Observing repeating FRB20240209A which is active see [ATel#16670 by Vishwangi Shah (McGill University) on behalf of the CHIME/FRB Collaboration](https://www.astronomerstelegram.org/?read=16670)

- And beyond!


## License

[GPL-3.0](https://github.com/afinemax/Astron_2024/blob/main/LICENSE)
