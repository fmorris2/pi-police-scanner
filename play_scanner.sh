#!/bin/bash
while true; do
	mplayer -nocache http://broadcastify.cdnstream1.com/31719 | sudo /home/ubuntu/pi-police-scanner/parse_scanner.py
done
