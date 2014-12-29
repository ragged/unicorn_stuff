unicorn_stuff
=============

Some small scripts for the Unicorn HAT of Pimoroni

unicorn_binary.py
=================
This script, if put in rc.local will show you for a specified time the IP Address of wlan0 (red) and eth0 (green) as binary code on your Unicorn HAT.

It shows all LEDs if this address is not yet available.

Just add it to a Directory of your choise and add following line to the end of your /etc/init.d/rc.local

sudo /home/pi/unicorn_binary.py &


