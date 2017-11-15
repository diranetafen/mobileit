#!/bin/bash
#
# login.sh $USERNAME $PASSWORD

cd /home/pi/custum_desktop/logs/
echo " $(date) ----------   Authentication-Admin_Access : Try authentication" >> authentication.log

/bin/bash /home/pi/custum_desktop/acces_admin/login.sh $1 $2

result=$?
# Now we test the retuned code by the previous command
if [ $result = "0" ]
then
    
	echo " $(date) ----------   Authentication-Admin_Access : Authentication OK" >> authentication.log
    echo "OK" > authentication.txt
else
    
    echo " $(date) ----------   Authentication-Admin_Access : Authentication KO" >> authentication.log
	echo "KO" > authentication.txt
fi

