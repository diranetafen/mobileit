#!/bin/bash

cd /home/pi/custum_desktop/logs
echo " $(date) ----------   Stop_Odoo : Stoping Process" >>  stop_desktop.log

if [ -f /tmp/odoo_pid ]; then
    echo "$(date) ----------   Stop_Odoo : Trying to stop Odoo instance" >>  stop_odoo.log
    kill $(cat /tmp/odoo_pid) || true
    echo "$(date) ----------   Stop_Odoo : Removing A pid file" >>  stop_odoo.log
    rm /tmp/odoo_pid
fi

