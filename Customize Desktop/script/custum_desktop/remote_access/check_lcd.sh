if [ -c /dev/ttyACM0 ] ; then
	echo "$(date) ----------   check_LCD : LCD up" >>  /home/pi/custum_desktop/logs/check_lcd.log
	echo "OK" > /home/pi/custum_desktop/logs/check_lcd.txt
else
	echo "$(date) ----------   check_LCD : LCD down" >>  /home/pi/custum_desktop/logs/check_lcd.log
	echo "KO" > /home/pi/custum_desktop/logs/check_lcd.txt
fi
