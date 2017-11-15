cd /home/pi/custum_desktop/check_module
printer=`python check_printer.py | grep usb  | cut -d' ' -f1`
cd /home/pi/custum_desktop/logs
if [ $printer == "ZJ-58" ] 
then
	echo "$(date) ----------   check_printer : Printer UP" >>  /home/pi/custum_desktop/logs/check_printer.log
	echo "OK" > /home/pi/custum_desktop/logs/check_printer.txt
else
	echo "$(date) ----------   check_printer : Printer Down" >>  /home/pi/custum_desktop/logs/check_printer.log
	echo "KO" > /home/pi/custum_desktop/logs/check_printer.txt
fi
