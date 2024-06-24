# imports
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from os.path import basename, dirname
import glob
import subprocess
import os
from tqdm import tqdm
from multiprocessing import Pool

# data dir
datadir = '/media/camrasdemo/3f3a1b8a-f7dc-4dad-97f4-7b3f0ffa6cbf'

# function to execute presto commands in terminal
def run_command(command):
    process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate(input='\n')  # Simulate pressing 'enter'
    return stdout, stderr

def process_directory(dir):
    # list all *.stats files
    command = f"ls {datadir}/{dir}/process/*.stats"
    stdout, stderr = run_command(command)
    mask_files = stdout.split('\n')

    for mask in tqdm(mask_files, desc=f"Processing {dir}"):
        command = f"rfifind_stats.py {mask}"
        stdout, stderr = run_command(command)
        # print any output or error if needed

if __name__ == '__main__':
    # collect all directories in the data dir
    stdout, stderr = run_command(f"ls {datadir}")
    dirs = stdout.split('\n')

    # using multiprocessing pool to parallelize the execution
    with Pool(processes=4) as pool:  # specify number of processes
        pool.map(process_directory, dirs)

    print("All processes completed.")
