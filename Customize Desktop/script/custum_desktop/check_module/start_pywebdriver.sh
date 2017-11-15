cd /home/pi/custum_desktop/logs
echo " $(date) ----------   Start-PyWebDriver : Start PyWeb display webservice" >> startup_pywebdriver.log
cd /home/pi/odoo/pywebdriver
nohup sudo python pywebdriverd >> pywebdriver.log 2>&1 &
echo $! > /tmp/pydriver_pid.txt

