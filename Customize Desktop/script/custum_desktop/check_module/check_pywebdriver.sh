#cd /home/pi/custum_desktop/check_module

#./stop_pywebdriver.sh
#./start_pywebdriver.sh

#sleep 5

pyweb=`curl --write-out "%{http_code}\n" --silent --output /dev/null "http://127.0.0.1:8065/usb_devices.html"`


if [ $pyweb = 200 ]; then
        echo "$(date) ----------   check_Pyweb : Pyweb up" >>  /home/pi/custum_desktop/logs/check_pyweb.log
        echo "OK" > /home/pi/custum_desktop/logs/check_pyweb.txt
else
        echo "$(date) ----------   check_Pyweb : Pyweb down" >>  /home/pi/custum_desktop/logs/check_pyweb.log
        echo "KO" > /home/pi/custum_desktop/logs/check_pyweb.txt
fi

