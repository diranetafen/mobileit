usage_filesystem=`df -h | cut -d' ' -f15 | sed -n 2p | cut -d'%' -f1`

if [ $usage_filesystem >80 ] ; then
	echo "$(date) ----------   check_Filesystem : File system usage less that 80%, all is fine" >>  /home/pi/custum_desktop/logs/check_filesystem.log
	echo "OK" > /home/pi/custum_desktop/logs/check_filesystem.txt
else
	echo "$(date) ----------   check_Filesystem : File system usage greater that 80%, please free space" >>  /home/pi/custum_desktop/logs/check_filesystem.log
	echo "KO" > /home/pi/custum_desktop/logs/check_filesystem.txt
fi
