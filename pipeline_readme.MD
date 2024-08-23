#  25m Dwingeloo Radio Telescope (DRT) real time Fast Radio Burst (FRB) Detection Pipeline




## Suggestions For Future Work:
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


## Installation:

In order to use this, you will need to have installed [Fetch](https://github.com/devanshkv/fetch), and [Presto](https://github.com/scottransom/presto). Our version of `presto` uses a modified for `ddplan.py` to supress plotting.  
    
## Authors:

- [@@thomas](https://gitlab.camras.nl/thomas)
- [@dijkema](https://gitlab.camras.nl/dijkema)
- [@afinemax](https://www.github.com/afinemax)


## Contributing:

Contributions are always welcome!

Reach out to [@dijkema](https://gitlab.camras.nl/dijkema) 

## Suggestions for Future Improvement:

## Feedback:

If you have any feedback, please reach out to us.


## Acknowledgements:

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)


![Logo](https://www.camras.nl/wp-content/themes/camras-enfold-child/images/camras-footer-logo.png)

