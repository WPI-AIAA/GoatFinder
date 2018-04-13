sudo cp /etc/wpa_supplicant/wpa_supplicant-bor.conf /etc/wpa_supplicant/wpa_supplicant.conf
sudo cp /etc/network/interfaces-bor /etc/network/interfaces

sudo pkill wpa_supplicant
sudo sh ./wpa_sup
