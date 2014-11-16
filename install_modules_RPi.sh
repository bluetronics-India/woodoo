#!/bin/bash
JasperLoc=`find / 2>/dev/null -type d -name 'jasper'`/client/modules
cp RPI_Modules/*  $JasperLoc
echo Installed files in $JasperLoc
