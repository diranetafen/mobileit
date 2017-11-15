cd /home/pi/custum_desktop/remote_access #Changing directory to your working directory

# First delete all default route
sudo route del default

# Update USB deveice in PPP file to make it correspond to reality
sudo cp /etc/ppp/peers/gprs-bkp /etc/ppp/peers/gprs
#/bin/bash /home/pi/custum_desktop/remote_access/stop_openvpn.sh
# Starting PPP connection to 3G
sudo ifdown gprs
sudo ifup gprs

sleep 20

cd /home/pi/custum_desktop/logs/


# Test connection to internet
url_response=`curl -s -o /dev/null -w "%{http_code}"  https://www.google.fr/`

if [ $url_response == 200 ]
then
  echo " $(date) ----------   BACKUP-connection : Could ping google" >> backup_answer.log
  internet="OK" # This $internet variable help to check internet connection before activate VPN server
  echo "OK" > vpn_answer.txt
else
  echo " $(date) ----------   BACKUP-connection : Could not ping google" >> backup_answer.log
  internet="KO"
  echo "KO" > backup_answer.txt
fi
sleep 30

# Test VPN connection
if [ "$internet" == "OK" ]
then
    cd /home/pi/odoo/pos_demo_full/backup/
	find -name "* *" -type f | rename 's/ /_/g'
    filename=$(ls -dt MobileIT* | head -1)
	cd /home/pi/custum_desktop/logs/
	scp /home/pi/odoo/pos_demo_full/backup/$filename  pi@2.7.57.86:/tmp/backup/
	result=$?
	if [ $result = "0" ]
	then
		backup="OK"
		echo $backup > backup_answer.txt
		echo " $(date) ----------   BACKUP-connection : Backup done" >> backup_answer.log
	else
		backup="KO"
		echo $backup > backup_answer.txt
		echo " $(date) ----------   BACKUP-connection : Backup error" >> backup_answer.log
	fi
	sudo ifdown gprs
	
fi

