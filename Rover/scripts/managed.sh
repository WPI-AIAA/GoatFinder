iwconfig wlan0 mode managed
ifconfig wlan0 0.0.0.0 0.0.0.0

sudo wpa_supplicant &
sudo dhclient &
sudo NetworkManager &
sudo avahi-daemon &
