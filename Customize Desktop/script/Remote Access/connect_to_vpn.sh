#cd /home/pi/custum_desktop/remote_access #Changing directory to your working directory
detected_usb=`gammu-detect | grep ttyUSB | sed -n 1p | cut -d'=' -f2 |  cut -c2- | cut -d'/' -f3`
sudo sed -i "s/ttyUSB.*/$detected_usb/g" /home/pi/.gammurc
usb_device=`gammu --identify | sed -n 1p | cut -d':' -f2 | cut -c2- | cut -d'/' -f3`

cd /home/pi/custum_desktop/logs/

# Update USB deveice in PPP file to make it correspond to reality
sudo cp /etc/ppp/peers/gprs-bkp /etc/ppp/peers/gprs
sudo sed -i "s/ttyUSB.*/$usb_device/g" /etc/ppp/peers/gprs

# Starting PPP connection to 3G
sudo ifdown gprs
sudo ifup gprs

# Test connection to internet
if [ "`ping -c 1 8.8.8.8`" ]
then
  echo " $(date) ----------   VPN-connection : Could ping google" >> vpn_answer.log
  internet="OK" # This $internet variable help to check internet connection before activate VPN server
  echo "OK" > vpn_answer.txt
else
  echo " $(date) ----------   VPN-connection : Could not ping google" >> vpn_answer.log
  internet="KO"
  echo "KO" > vpn_answer.txt
fi


# Test VPN connection
if [ "$internet" == "OK" ]
then
	sudo openvpn client.ovpn & echo $! > /tmp/openvpn_pid
	sleep 15
	if [ "`ping -c 1 192.168.255.1`" ]
	then
		echo " $(date) ----------   VPN-connection : Could ping VPN Server" >> vpn_answer.log
		VPN="OK" # This $internet variable help to check internet connection before activate VPN server
		echo "OK" > vpn_answer.txt
	else
		echo " $(date) ----------   VPN-connection : Could not ping VPN Server" >> vpn_answer.log
		VPN="KO"
		echo "KO" > vpn_answer.txt
	fi
fi
