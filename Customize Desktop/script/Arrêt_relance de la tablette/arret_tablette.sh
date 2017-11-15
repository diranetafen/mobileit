pos_container=`docker ps -a --format '{{.Names}}' | sed -n 1p`
db_container=`docker ps -a --format '{{.Names}}' | sed -n 2p`

cd /home/pi/odoo/pos_demo_full
sudo docker-compose stop

cd /home/pi/custum_desktop/logs

if [ `sudo docker inspect -f {{.State.Status}} $pos_container` = "exited" ] && [ `sudo docker inspect -f {{.State.Status}} $db_container` = "exited" ] ; then
    echo " $(date) ----------   Tablet-Stop : Stopping the tablet" >> arret_tablet.log
    sudo shutdown -h now
else
    echo " $(date) ----------   Tablet-Stop : Stopping the tablet with no all container stopped, there may an issue" >> arret_tablet.log
    sudo shutdown -h now
fi

