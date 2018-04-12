#!/bin/sh
pkill avahi-daemon
pkill NetworkManager
pkill wpa_supplicant
pkill dhclient
ifconfig wlan0 down
iwconfig wlan0 channel 1 essid "WPI BOR Pi" mode ad-hoc 
ifconfig wlan0 up
iwlist wlan0 scan
ifconfig wlan0 192.168.1.1 netmask 255.255.255.0
service dhcpcd stop
