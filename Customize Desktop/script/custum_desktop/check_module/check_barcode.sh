if [ -c /dev/ttyAMA0 ] ; then
	echo "$(date) ----------   check_Barcode : Barcode up" >>  /home/pi/custum_desktop/logs/check_barcode.log
	echo "OK" > /home/pi/custum_desktop/logs/check_barcode.txt
else
	echo "$(date) ----------   check_Barcode : Barcode down" >>  /home/pi/custum_desktop/logs/check_barcode.log
	echo "KO" > /home/pi/custum_desktop/logs/check_barcode.txt
fi
