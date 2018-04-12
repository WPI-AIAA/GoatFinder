sudo sh ad-hoc.sh > ad-hoc.log 
sleep 30
sudo sh ad-hoc.sh > ad-hoc.log 
sleep 30
iwconfig > iwconfig.log
sleep 1m
sudo sh managed.sh > managed.log
sleep 30
shutdown -h now
