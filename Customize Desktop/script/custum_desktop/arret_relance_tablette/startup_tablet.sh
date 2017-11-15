pos_container=`docker ps -a --format '{{.Names}}' | sed -n 1p`
db_container=`docker ps -a --format '{{.Names}}' | sed -n 2p`

cd /home/pi/odoo/pos_demo_full
sudo docker-compose start
#sleep 20

cd /home/pi/custum_desktop/logs

if [ `sudo docker inspect -f {{.State.Status}} $pos_container` = "running" ] && [ `sudo docker inspect -f {{.State.Status}} $db_container` = "running" ] ; then
    echo " $(date) ----------   Tablet-Startup : The two container are up" >> startup_tablet.log
else
    echo " $(date) ----------   Tablet-Startup : container are not started, there may an issue" >> startup_tablet.log
fi

echo " $(date) ----------   Tablet-Startup : Start PyWeb display webservice" >> startup_tablet.log
cd /home/pi/odoo/pywebdriver
nohup sudo python pywebdriverd >> pywebdriver.log 2>&1 &
echo $! > pydriver_pid.txt



# Remove all pid and answer txt file
cd /home/pi/custum_desktop/logs
echo " $(date) ----------   Tablet-Startup : Delete logs" >> startup_tablet.log

cd /home/pi/custum_desktop/logs
find . -name '*.txt' -delete

cd /tmp/
find . -name '*pid*' -delete
find . -name '*wid*' -delete

# Remove Task bar
echo " $(date) ----------   Tablet-Startup : Remove TaskBar " >> startup_tablet.log
killall lxpanel

# copy base gammu config
cp /home/pi/.gammurc-base /home/pi/.gammurc

# Disable GSM PPP0 interface
sudo ifdown gprs
