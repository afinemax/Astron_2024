# Maxwell A. Fine 2024-07-10

This notebook is trying out running `predict.py` from [fetch](https://github.com/devanshkv/fetch/tree/tf2) within a python script, as well as moving the 'good' candidates into another dir and making diagnostic `.png` files. 

### Fetch
`Fetch` is a machine learning approach to identifying real and RFI pulse candidates, see the paper [here](https://arxiv.org/abs/1902.06343).

The `Fetch` package on github comes all set with a script `predict.py` that works on `.h5` files of a predetermined shape.It needs a `--datadir`, and a `--model` key flag argument to run. The output is a `.csv` file containg if the candidate file with the labeles as classified by fetch (1=good, 0=bad).

`Fetch` runs on a GPU, using CUDA. 


### Task:
I want to run `fetch` from inside another python script. This gives us two possibiltiies:
- write a simple `subprocess` command to execute the script
- import the required functions to run the `main` function in `predict.py` and use it natively in python


### Notes From my use of `fetch` so far:
- There is a comparably long start up time when running, I think its involved in setting up the GPU and moving over the data? 
- Fetch runs pretty fast per itertation, ~800-1000 candidates / minute. 


### Idea:
- It is probablly more **pythonic** to import the functions to run `fetch` inside of another script, but running it via a `subprocess` call is faster to implement, and will perform about the same. Since the pipeline already is making `subprocess` calls, I will do it with this method. 
    - using a `subproccess` call might be better for other users for future improvements, as it would use all the same commands as `predict.py`

- We could cut out much of the start up time, by running `fetch` just once per observation (as opposed to once per `.fil` file). But then we couldn't run the pipeline in **real** time. I favor running it in real time, so we will run it once per `.fil` file.
    - The pipeline is running parallel, how does our GPU handle it?

- there already exists a `move_candidates.py` script in [pipeline gitlab repo code](https://gitlab.camras.nl/dijkema/frbscripts)
    - I can maybe make a wrapper function around this, and then just import it in the `check_frb.py` script
- similariy, use the `plot_h5` code (more of a call to another function) to do the plotting of diagnostic plots



