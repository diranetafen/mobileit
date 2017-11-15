directory="/media/pi/USB_POS"
drive=`sudo blkid | grep USB_POS | cut -d':' -f1`
if [ -d $directory ] ; then
        echo "$(date) ----------   check_usb_key : usb_key up" >>  /home/pi/custum_desktop/logs/check_usb_key.log
        echo "OK" > /home/pi/custum_desktop/logs/check_usb_key.txt
else
        echo "$(date) ----------   check_usb_key : USB Key not already mounted, we are trying to do it now ..." >>  /home/pi/custum_desktop/logs/check_usb_key.log
        if [ $drive == "/dev/sda4" ] ; then
                sudo mkdir $directory
                sudo mount -t ntfs-3g /dev/sda4 $directory
                echo "$(date) ----------   check_usb_key : Mounting USB Key ..." >>  /home/pi/custum_desktop/logs/check_usb_key.log
                if [ -d $directory ] ; then
                        echo "$(date) ----------   check_usb_key : usb_key UP" >>  /home/pi/custum_desktop/logs/check_usb_key.log
                        echo "OK" > /home/pi/custum_desktop/logs/check_usb_key.txt
                else
                        echo "$(date) ----------   check_usb_key : usb_key down" >>  /home/pi/custum_desktop/logs/check_usb_key.log
                        echo "KO" > /home/pi/custum_desktop/logs/check_usb_key.txt
                fi
        else
                echo "$(date) ----------   check_usb_key : Not Plugged please plug it" >>  /home/pi/custum_desktop/logs/check_usb_key.log
                echo "KO" > /home/pi/custum_desktop/logs/check_usb_key.txt
        fi
fi

