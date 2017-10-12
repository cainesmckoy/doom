#!/bin/bash
clear
cd 115
sudo rm info
cd
sudo rm -rf 115
sudo mkdir 115
sudo chmod 700 115
sudo chown caine:caine 115
echo "THESE FILES HAVE BEEN EDITED" > 115/info
sudo find /etc /mnt /home . -mmin -30 -type f -print >> 115/info
sudo cat 115/info
sleep 60
sudo ./log4.sh 

