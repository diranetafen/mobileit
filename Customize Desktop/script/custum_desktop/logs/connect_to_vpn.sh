cd /home/pi/custum_desktop/remote_access #Changing directory to your working directory

# Update USB deveice in PPP file to make it correspond to reality
sudo cp /etc/ppp/peers/gprs-bkp /etc/ppp/peers/gprs

# Starting PPP connection to 3G
sudo ifdown gprs
sudo ifup gprs

sleep 20

cd /home/pi/custum_desktop/logs/


# Test connection to internet
url_response=`curl -s -o /dev/null -w "%{http_code}"  https://www.google.fr/`
echo 1
if [ $url_response == 200 ]
then
  echo " $(date) ----------   VPN-connection : Could ping google" >> vpn_answer.log
  internet="OK" # This $internet variable help to check internet connection before activate VPN server
  echo "OK" > vpn_answer.txt
else
  echo " $(date) ----------   VPN-connection : Could not ping google" >> vpn_answer.log
  internet="KO"
  echo "KO" > vpn_answer.txt
fi
sleep 20

# Test VPN connection
if [ "$internet" == "OK" ]
then
		
		gateway_gsm=`ip addr show ppp0 | grep peer | awk ' { print $4 } ' | sed 's/\/32//'`
		sudo ip route replace default via $gateway_gsm dev ppp0
		sleep 10
		sudo openvpn --config client.ovpn --askpass certificate_password.txt & echo $! > /tmp/openvpn_pid
		sleep 30
		
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

