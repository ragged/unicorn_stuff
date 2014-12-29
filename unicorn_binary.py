#!/usr/bin/env python

import unicornhat as unicorn
import binascii
import socket
import fcntl
import struct
import time
unicorn.brightness(0.1)

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
        )[20:24])

def main():
    count = 0
    while True:
        count += 1
        try:
            wlan = get_ip_address('wlan0')
        except IOError:
            wlan = "255.255.255.255"
        try: 
            eth0 = get_ip_address('eth0')
        except IOError:
            eth0 = "255.255.255.255"

        #show wlan ip in red
        row = 0
        for octett in wlan.split("."):
            print octett
            column = 7
            tmp_binary = bin(int(octett)).split("b")[1]
            print tmp_binary
            for i in tmp_binary[::-1]:
                if int(i) > 0:
                    unicorn.set_pixel(column, row, 255, 0, 0)
                else:
                    unicorn.set_pixel(column, row, 0, 0, 0)
                column -= 1
            row += 1 
        #show eth0 ip address
        for octett in eth0.split("."):
            print octett
            column = 7
            tmp_binary = bin(int(octett)).split("b")[1]
            print tmp_binary
            for i in tmp_binary[::-1]:
                if int(i) > 0:
                    unicorn.set_pixel(column, row, 0, 255, 0)
                else:
                    unicorn.set_pixel(column, row, 0, 0, 0)
                column -= 1
            row += 1 

        unicorn.show()

        time.sleep(1)
        if count > 120:
            break


if __name__ == "__main__":
    main()
