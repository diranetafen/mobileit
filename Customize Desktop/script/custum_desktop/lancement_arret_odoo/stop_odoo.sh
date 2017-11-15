#!/bin/bash

cd /home/pi/custum_desktop/logs
echo " $(date) ----------   Stop_Odoo : Stoping Process nativefier" >>  stop_odoo.log

if [ -f /tmp/odoo_pid ]; then
    echo "$(date) ----------   Stop_Odoo : Trying to stop previous instance of process Nativefier" >>  stop_odoo.log
    kill $(cat /tmp/odoo_pid) || true
    echo "$(date) ----------   Stop_Odoo : Removing odoo_pid pid file" >>  stop_odoo.log
    rm /tmp/odoo_pid
fi

