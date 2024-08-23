# Observing FRBS Procedure

Created by Tammo Jan, 2024-03-20

Maxwell Fine, 2024-08-23

## Setup:

Connect the 23cm connection from the antenna panel (labeled '3') to the X310 via the top left connection in the rack. Turn on the X310, located at the top of the Faraday cage.

## SSH into Uranus:

**NOTE** - you need a personal camras account to get into uranus, contact ict if you don't have one.

Become the frb user on Uranus: run ```sudo -u frb -i``` 

This account on Uranus has all of the observation scripts loaded into the path. 

## Point the Telescope to the FRB you want to observe:
Now point the telescope to the FRB you want to observe:

Run: 
``` cat /home_local/frb/git/frbscripts/frb.cat```

This will print out the FRB catalog on the telescope, the output should look something like this. Pick an FRB and move the telescope.  


| Name         | DM (pc/cm³) | RA (deg) | Dec (deg) |
|--------------|-------------|----------|-----------|
| FRB20201124A | 411         | 77.01    | 26.06     |
| FRB20220912A | 219         | 347.27   | 48.71     |




## Starting the Observation: 
Once the telescope is pointed at the FRB, **start** the observation with:
```start_frb.sh```

This program starts the observation, and the real-time pipeline scripts.

It also starts a dashboard, which runs in the terminal. Be sure that the terminal is the full-size of the screen. 

- If you get a message saying a observation is already running, run ```stop_frb.sh```, and then run ```start_frb.sh``` again. 

- The terminal needs to be the full-size of the screen, otherwise the dashboard fails to start

## About the Dashboard:

![FRB Dashboard](https://github.com/afinemax/Astron_2024/raw/main/frb_dashboard.png)


This is what the dashboard looks like when running. Note this is for an observation of the Crab Pulsar - FRBs are much harder to detect. 

The Dashboard displays usefull information during the observation. 
- space on `/data`, **this number is important to watch. Stop Observing when this is low (less then 20)**
- When the `.fil` files are green - we are recording data!
	- We record the data in chunks of 10 minutes
	- Every 10 minutes or so you will see `check_frb` sessions running
- space on `/data_tmp`, this is where the baseband data is recorded. It is deleted if no "good" candidates are made  
- If the pipeline produces a "good" candidate, it's Signal-To-Noise Ratio (SNR) is displayed. This tells us how bright the detection is. 

You can also start the dashboard by running ```frb_dashboard.py```



## If you make a "good" detection:
Continue Observing! Notify Tammo & Max. This is not a confirmed FRB - it is still a candidate and needs human review.  
 

## Stopping Observations:

To stop the observation scripts, run ```stop_frb.sh```. Closing the dashboard does not stop recording data!

**Important** Stop observing if the space on `/data` is less than 20 Gb 

## Shutdown:

After you have stopped the observation:

* Turn off the X310 in the Faraday cage.
* Reconnect the antenna to the astronomy panel, i.e., connect antenna port 3 to the port below labeled '23cm'.


## Data Management:
If the space on `/data` is low message Tammo, and Max. We do not automaticaly delete files. 
