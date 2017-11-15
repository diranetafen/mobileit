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


