#!/bin/bash

if [ -f /tmp/openvpn_pid ]; then
    echo "Trying to stop previous instance of proces Customize Desktop"
    echo " $(date) ----------    Stop-VPN : Trying to stop previous instance of proces Customize Desktop" >> /home/pi/custum_desktop/logs/stop-vpn.log
    sudo kill $(cat /tmp/openvpn_pid) || true
    echo " $(date) ----------    Stop-VPN : Removing A pid file " >> /home/pi/custum_desktop/logs/stop-vpn.log
    sudo rm /tmp/openvpn_pid
    sudo ifdown gprs 
fi

