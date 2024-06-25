 docker run -it --name presto_tut -v /home/afinemax/afinemax/khazad-dum/research/astron_2024/presto_and_tut/:/data c7897abba927 /bin/bash
# this runs my docker image iteractively, and adds my files to /data
# -it for interactively
# --name for name of image 


camrasdemo@mercurius:/media/camrasdemo/3f3a1b8a-f7dc-4dad-97f4-7b3f0ffa6cbf/2024-03-24$
# this is the pwd for the external hardrive holding data on mercurius


xhost +local:root # I think you only need to do this once

docker run -it --name noise_new_channels \
  -v /home/afinemax/afinemax/khazad-dum/research/astron_2024/noise_channels/data/:/data \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  c7897abba927 /bin/bash
  
# this is docker +x11 forwarding

ssh camrasdemo "find /media/camrasdemo/3*/ -name '*.mask'" > files_to_copy.txt
# makes list of files on my local machine in the .txt file

# rsync -avz --include '*/' --include '*.mask' --exclude '*' camrasdemo:/media/camrasdemo/3f3a1b8a-f7dc-4dad-97f4-7b3f0ffa6cbf/ .
# copies


# become frb user on uranus
# sudo -u frb -i 


scp -r camrasdemo@mercurius:/media/camrasdemo/3f3a1b8a-f7dc-4dad-97f4-7b3f0ffa6cbf /data_tmp/delete_me_max

# copy data dir files from merc to uranus to make the .weights with



# du -sh /path/to/directory

# list out how big the dirctory is in storage


screen #cmd here
# then press crtl +a, this runs a terminal session that still runs when you leave!
# screen ls to list screens and screen -r to reattach -S to name screen when making
