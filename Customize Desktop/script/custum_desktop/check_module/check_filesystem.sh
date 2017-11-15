usage_filesystem=`df -h / | tail -1 | tr -s ' ' | cut -d' ' -f5 | cut -d'%' -f1`

if [ $usage_filesystem >80 ] ; then
	echo "$(date) ----------   check_Filesystem : File system usage less that 80%, all is fine" >>  /home/pi/custum_desktop/logs/check_filesystem.log
	echo "OK" > /home/pi/custum_desktop/logs/check_filesystem.txt
else
	echo "$(date) ----------   check_Filesystem : File system usage greater that 80%, please free space" >>  /home/pi/custum_desktop/logs/check_filesystem.log
	echo "KO" > /home/pi/custum_desktop/logs/check_filesystem.txt
fi
