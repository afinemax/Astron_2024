## Docker Commands

### Running Docker Image Interactively

`docker run -it --name presto_tut -v /home/afinemax/afinemax/khazad-dum/research/astron_2024/presto_and_tut/:/data c7897abba927 /bin/bash`
- This runs my Docker image interactively and mounts my files to `/data`.
- `-it` for interactive mode.
- `--name` for naming the container.

### Running Docker with X11 Forwarding

`xhost +local:root` 
- I think you only need to do this once.

`docker run -it --name noise_new_channels -v /home/afinemax/afinemax/khazad-dum/research/astron_2024/noise_channels/data/:/data -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix c7897abba927 /bin/bash`
- This sets up Docker with X11 forwarding.

## SSH and File Management

### Have SSH remember login password 

`ssh-copy-id maxfine@access.camras.nl`
- This moves your local ssh public key? to the host computer

`~/.ssh/config`
- location of ssh config file so you can do fancy graphic forwarding, always open a port, ssh nickname etc

`jupyter-notebook --no-browser --port=8888 --ip=0.0.0.0`
- portforward in my ssh config file, and run this command on host computer to start a jupyter-notebook session via ssh

`ssh -N -f -L localhost:8888:localhost:8888 maxfine@uranus`
- does the local portforwarding to the host computer

- run `sudo lsof -i :8888` to see process using port 8888 on my local, I might need to kill it
### External Hard Drive Path

`camrasdemo@mercurius:/media/camrasdemo/3f3a1b8a-f7dc-4dad-97f4-7b3f0ffa6cbf/2024-03-24$`
- This is the `pwd` for the external hard drive holding data on Mercurius.

### Make a List of Files on My Local Machine in the `.txt` File

`ssh camrasdemo "find /media/camrasdemo/3*/ -name '*.mask'" > files_to_copy.txt`

### Copy Files Using `rsync`

`rsync -avz --include '*/' --include '*.mask' --exclude '*' camrasdemo:/media/camrasdemo/3f3a1b8a-f7dc-4dad-97f4-7b3f0ffa6cbf/ .`
- Copies files based on the list.

### Become `frb` User on Uranus

`sudo -u frb -i`

### Copy Data Directory Files from Mercurius to Uranus to Make the `.weights` With

`scp -r camrasdemo@mercurius:/media/camrasdemo/3f3a1b8a-f7dc-4dad-97f4-7b3f0ffa6cbf /data_tmp/delete_me_max`

### Check Directory Size

`du -sh /path/to/directory`
- Lists out how big the directory is in storage.

### Using `screen` for Persistent Terminal Sessions

`screen` 
- Then press `Ctrl + A`, this runs a terminal session that still runs when you leave!
- `screen ls` to list screens and `screen -r` to reattach, `-S` to name screen when making.

### Counting lines in `$BASH`

`wc -l example.txt`

-wordcount (wc), the -l gives lines

`ls *.singlepulse | wc -l > file.txt`
- this would first, list out all the files that match `*.singlepulse`, and then count all of the lines in all the files and write the number to `file.txt`
