#!/bin/bash

cd /home/pi/custum_desktop/logs
echo " $(date) ----------   Stop_Desktop : Stoping Process" >>  stop_desktop.log

if [ -f /tmp/desktop_pid ]; then
    echo "$(date) ----------   Stop_Desktop : Trying to stop previous instance of proces Customize Desktop" >>  stop_desktop.log 
    sudo kill $(cat /tmp/desktop_pid) || true
    echo "$(date) ----------   Stop_Desktop : Removing A pid file" >>  stop_desktop.log
    rm /tmp/desktop_pid 
fi
