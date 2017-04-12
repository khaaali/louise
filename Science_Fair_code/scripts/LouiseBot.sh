#!/bin/sh
#This the shell scrip for auotmating the telegram_bot(Louise) on reboot, can be found in using command"sudo crontab -l/-e" command is shown below
#@reboot sh /home/pi/scripts/LouiseBot.sh >/home/pi/scripts/logs/cronlog 2>&1


sleep 10
cd /
cd /home/pi/telegram_bot
sudo python main.py
