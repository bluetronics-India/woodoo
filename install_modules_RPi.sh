#!/bin/bash
JasperLoc = `find -maxdepth 1 -type d -name 'jasper'| head -n1`/client/module
cp /RPI_Modules/*  JasperLoc