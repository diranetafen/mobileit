# Test connection to internet
url_response=`curl -s -o /dev/null -w "%{http_code}"  https://www.google.fr/`

if [ $url_response == 200 ]
then
  echo " $(date) ----------   Internet-Test : Could ping google" >> /home/pi/custum_desktop/logs/internet_test.log
  internet="OK" # This $internet variable help to check internet connection before activate VPN server
  echo "OK" > /home/pi/custum_desktop/logs/internet_test.txt
else
  echo " $(date) ----------   Internet-Test : Could not ping google" >> /home/pi/custum_desktop/logs/internet_test.log
  internet="KO"
  echo "KO" > /home/pi/custum_desktop/logs/internet_test.txt
fi


