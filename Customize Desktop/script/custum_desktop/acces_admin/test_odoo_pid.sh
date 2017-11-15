PID=`cat /tmp/odoo_pid`
if ps -p $PID > /dev/null
then
   echo "OK" > /home/pi/custum_desktop/logs/odoo.txt
   # Do something knowing the pid exists, i.e. the process with $PID is running
else
	echo "KO" > /home/pi/custum_desktop/logs/odoo.txt
fi
