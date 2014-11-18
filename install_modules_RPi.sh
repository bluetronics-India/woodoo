#!/bin/bash
JasperLoc=`find / 2>/dev/null -type d -name 'jasper'`/client/modules
cp RPI_Modules/*  $JasperLoc
cp Shared_Modules/*  $JasperLoc
echo Installed files in $JasperLoc
sudo apt-get install python-serial
sudo wget https://raw.githubusercontent.com/lurch/rpi-serial-console/master/rpi-serial-console -O /usr/bin/rpi-serial-console && sudo chmod +x /usr/bin/rpi-serial-console
sudo rpi-serial-console disable
echo Configured serial
