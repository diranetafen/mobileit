#!/bin/bash

cd /home/pi/custum_desktop/logs
echo " $(date) ----------   Stop_OpenVPN : Stoping Process" >>  stop_openvpn.log

if [ -f /tmp/openvpn_pid ]; then
    echo "$(date) ----------   Stop_Desktop : Trying to stop previous instance of proces Customize Desktop" >>  stop_desktop.log
    sudo kill $(cat /tmp/openvpn_pid) || true
    echo "$(date) ----------   Stop_OpenVPN : Removing A pid file" >>  stop_openpvn.log
    rm /tmp/openvpn_pid
fi

sudo ifdown gprs
