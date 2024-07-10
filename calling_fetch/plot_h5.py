#!/usr/bin/env python

import sys
from tqdm import tqdm
import matplotlib.pyplot as plt
from multiprocessing import Pool, cpu_count
from your.utils.plotter import plot_h5

def process_file(h5file):
    plot_h5(h5file, detrend_ft=True, save=True)
    plt.close('all')

def process_files_in_parallel(h5files):
    num_workers = min(cpu_count(), len(h5files))
    with Pool(num_workers) as pool:
        list(tqdm(pool.imap_unordered(process_file, h5files), total=len(h5files)))

if __name__ == "__main__":
    h5files = sys.argv[1:]
    process_files_in_parallel(h5files)


