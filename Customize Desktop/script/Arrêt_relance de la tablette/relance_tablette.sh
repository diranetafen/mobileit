pos_container=`docker ps -a --format '{{.Names}}' | sed -n 1p`
db_container=`docker ps -a --format '{{.Names}}' | sed -n 2p`

cd /home/pi/odoo/pos_demo_full
sudo docker-compose stop
#sleep 20

cd /home/pi/custum_desktop/logs


if [ `sudo docker inspect -f {{.State.Status}} $pos_container` = "exited" ] && [ `sudo docker inspect -f {{.State.Status}} $db_container` = "exited" ] ; then
    echo " $(date) ----------   Tablet-Stop : Stopping the tablet" >> relance_tablette.log
    sudo reboot 
else
    echo " $(date) ----------   Tablet-Stop : Stopping the tablet with no all container stopped, there may an issue" >> relance_tablette.log 
    sudo reboot 
fi

