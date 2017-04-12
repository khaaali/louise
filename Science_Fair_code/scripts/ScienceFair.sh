#!/bin/sh
#This the shell scrip for auotmating the sciencefair.py on reboot, can be found in using command"sudo crontab -l/-e" command is shown below
#@reboot sh /home/pi/scripts/ScienceFair.sh >/home/pi/scripts/logs/cronlog 2>&1


sleep 10
cd /
cd /home/pi/scripts
sudo python sciencefairevent.py

