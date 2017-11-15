pos_container=`docker ps -a --format '{{.Names}}' | sed -n 1p`
db_container=`docker ps -a --format '{{.Names}}' | sed -n 2p`


#sleep 20

cd /home/pi/custum_desktop/logs

if [ `sudo docker inspect -f {{.State.Status}} $pos_container` = "running" ] && [ `sudo docker inspect -f {{.State.Status}} $db_container` = "running" ] ; then
    echo " $(date) ----------   Start-Odoo : The two container are up" >> /home/pi/custum_desktop/logs/start_odoo.log
	echo  "OK" > /home/pi/custum_desktop/logs/start_odoo.txt
	cd /home/pi/nativefier/MobileIT/
	./mobile-it & echo $! > /tmp/odoo_pid
	echo " $(date) ----------   Start-Odoo : Nativefier Started" >> /home/pi/custum_desktop/logs/start_odoo.log
else
    cd /home/pi/odoo/pos_demo_full
    sudo docker-compose restart
    echo " $(date) ----------   Tablet-Startup : container are not started, there may an issue" >> /home/pi/custum_desktop/logs/start_odoo.log
	if [ `sudo docker inspect -f {{.State.Status}} $pos_container` = "running" ] && [ `sudo docker inspect -f {{.State.Status}} $db_container` = "running" ] ; then
		echo " $(date) ----------   Start-Odoo : The two container are up" >> /home/pi/custum_desktop/logs/start_odoo.log
		echo  "OK" /home/pi/custum_desktop/logs/start_odoo.txt
		cd /home/pi/nativefier/MobileIT/
		./mobile-it & echo $! > /tmp/odoo_pid
		echo " $(date) ----------   Start-Odoo : Nativefier Started" >> /home/pi/custum_desktop/logs/start_odoo.log
	else
		echo " $(date) ----------   Start-Odoo : start container fail" >> /home/pi/custum_desktop/logs/start_odoo.log
		echo  "KO" > /home/pi/custum_desktop/logs/start_odoo.txt
	fi
fi

