#!/bin/bash

cd /home/pi/custum_desktop/logs
echo " $(date) ----------   Stop_PyWebDirver : Stoping Process" >>  stop_pywebdriver.log

if [ -f /tmp/pydriver_pid.txt ]; then
    echo "$(date) ----------   Stop_PyWebDirver : Trying to stop previous instance of proces Customize Desktop" >>  stop_pywebdriver.log
    sudo kill $(cat /tmp/pydriver_pid.txt) || true
    echo "$(date) ----------   Stop_PyWebDirver : Removing A pid file" >>  stop_pywebdriver.log
    rm /tmp/pydriver_pid.txt
fi

