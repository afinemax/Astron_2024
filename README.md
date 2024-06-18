
# Hunting for Fast Radio Bursts (FRBs) with the 25-m Dwingeloo radio telescope at ASTRON, the Netherlands 🇳🇱 📡
## Advisors: Dr. Tammo Jan Dijkema & Co-advisor Proffesor Jason Hessels
In summer 2024, I am a researcher at The Netherlands Institute for Radio Astronomy (ASTRON) with their Summer Research Programme. For my project, I will be using and operating the 25-m Dwingeloo radio telescope. I will study bright repeating Fast Radio Bursts (FRBs) to understand the potential connections between repeating and apparently non-repeating FRBs. As FRBs are hard to catch, I will also observe pulsars to both test the methodology and learn the relevant techniques.




### This repo contains:
Important scripts, notebooks, notes, and flow charts + any presentations for my summer research. 

* [example_pipeline_h5_output](https://github.com/afinemax/Astron_2024/tree/main/example_pipeline__h5_output) contains a notebook that opens a `.h5` file, makes a waterfall plot for practice. Using a `.h5` file made from the pipeline
* [frb_example_data_june_2024](https://github.com/afinemax/Astron_2024/tree/main/frb_example_data_june_2024) contains a notebook making a waterfile plot from CHIME data stored as `~.npy` files
## Roadmap 

- [x] Understand how FRB signal from space turns into dynamic spectra IE how telescope records data, and analysis pipelines work, see [flowchart](https://github.com/afinemax/Astron_2024/blob/main/flow_charts/frb_to_dynamic_spectra.pdf)
	* [ ] fill in blackboxes in flowchart

- [x] Learn how to operate the 25-m Dwingeloo Radio Telescope 

- [x] Learn how to use [Presto](https://github.com/scottransom/presto) to conduct a single pulse search, and remove RFI

- [x] learn how the current pipeline works: `check_frb.py`, see [flowchart](https://github.com/afinemax/Astron_2024/blob/main/flow_charts/fil_to_dynamic_spectra.pdf) 
	* pipeline gitlab repo is [here](https://gitlab.camras.nl/dijkema/frbscripts)
	* [ ] create a file of known bad frequency channels from observed data to mask out using `-ignorechan' option in pipeline
	* [ ] modify the `start_frb.sh` script to record observations on uranus & mercurius computers

- [ ] learn how [Fetch](https://github.com/devanshkv/fetch) & [Transientx](https://github.com/ypmen/TransientX) work, implement into pipeline

- [ ] Observe FRBs, but more likely pulsars 

- And beyond!


## License

[GPL-3.0](https://github.com/afinemax/Astron_2024/blob/main/LICENSE)
