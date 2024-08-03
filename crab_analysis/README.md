## Last Updated 2024-08-03
## Maxwell A. Fine 

### Goals:
* Make plots of SNR, Fluence, $E_{\nu}$ for the crab over many hours of observations
* Compare to 2019, 2024 Crab paper, and Jason Hessels Paper
* Addtionaly make some stastical plots of the Crab in the different Bands



### My Plots:
![Alt Text](https://github.com/afinemax/Astron_2024/blob/main/crab_analysis/crab_dm.png "Histograms of Measured DM from Crab with the telescope")
![Alt Text}(https://github.com/afinemax/Astron_2024/blob/main/crab_analysis/snr_freq.png)
	

### TODO:
* [] Add line for known DM of Crab
* [] Add fancy telephone number for crab 
* [] Add Power Laws from papers, and add hyperlinks to papers
* [ ] Fit both a broken, and simple power law to our data
* [] Force rebinning, so Poission error holds
* [ ] Convert SNR to Fluence, and $E_{\nu}$
        - For Fluence, would need burst width - maybe I can integrate in SNR and then convert
        - Are the `.h5` files good enough - they were made for fetch so 250x250? or do I need to make higher qualilty ones?


### Assumptions:
* SNR ~ Fluence ~ $E_{\nu}$
    - SNR ~ Fluence, works if the width of the burst does not depend on its brightness 
    - Not sure about $E_{\nu}$

