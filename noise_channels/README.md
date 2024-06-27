### About this Directory

This directory contains several notebooks and scripts necessary for managing observational data and analysis to create `.weights` files with Presto, and `.ignorechans` files:

- **`.png Files`**: Plots illustrating channels flagged as RFI across multiple observations.
- **`.ignorechans Files`**: Configuration files for the `ignorechans` key option in the pipeline.
- **`Noise Channels Notebook`**: Designed for single observations, requiring Docker and a local copy of the entire `/process` directory.
- **`create_weight_files.py` Script**: Automates the generation of `.weights` files from processed observations, ensuring the integrity of resulting data products.
- **`Bad Channels Notebook`**: Facilitates analysis across multiple observations, leveraging Docker for environment consistency. After setup, this notebook allows for the creation of master weights, `ignorechans` files, and corresponding plots.

These are plots of the bad channels, note the freq axis might be flipped I'll know for sure next week (July 1) when I test this

![p band](https://github.com/afinemax/Astron_2024/blob/main/noise_channels/p_band_bad_channels.png)

![l1 band](https://github.com/afinemax/Astron_2024/blob/main/noise_channels/l1_band_bad_channels.png)

![l2 band](https://github.com/afinemax/Astron_2024/blob/main/noise_channels/l2_band_bad_channels.png)


