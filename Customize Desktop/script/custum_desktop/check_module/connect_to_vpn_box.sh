cd /home/pi/openvpn

sudo openvpn --config client.ovpn --askpass certificate_password.txt  & echo $! > /tmp/openvpn_pid
                sleep 30
cd /home/pi/custum_desktop/logs
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


