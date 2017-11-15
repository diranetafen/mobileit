if ls /dev/ttyACM* > /dev/null 2>&1; then 
   cd /dev/
   usb_lcd=`find . -name "ttyACM*" -print |  cut -d'/' -f2`
   if [ $usb_lcd != "ttyACM0" ]; then
		sudo mv $usb_lcd ttyACM0
		echo "$(date) ----------   check_LCD : Change LCD device name" >>  /home/pi/custum_desktop/logs/check_lcd.log
   fi
   
   echo "$(date) ----------   check_LCD : LCD up" >>  /home/pi/custum_desktop/logs/check_lcd.log
   echo "OK" > /home/pi/custum_desktop/logs/check_lcd.txt
else
   echo "$(date) ----------   check_LCD : LCD down" >>  /home/pi/custum_desktop/logs/check_lcd.log
   echo "KO" > /home/pi/custum_desktop/logs/check_lcd.txt
   
fi
