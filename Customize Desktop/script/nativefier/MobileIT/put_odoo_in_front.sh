xdotool windowactivate $(echo $((`wmctrl -l | grep 'Odoo' | cut -d' ' -f1`)))
