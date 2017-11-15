sudo /usr/sbin/usb_modeswitch -W -v 05c6 -p 1000 -K
sleep 10
if [ -c /dev/ttyUSB0 ] ; then
        echo "$(date) ----------   check_GSM : GSM up" >>  /home/pi/custum_desktop/logs/gammu_answer.log
        echo "OK" > /home/pi/custum_desktop/logs/gammu_answer.txt
else
        echo "$(date) ----------   check_GSM : GSM down" >>  /home/pi/custum_desktop/logs/gammu_answer.log
        echo "KO" > /home/pi/custum_desktop/logs/gammu_answer.txt
fi
