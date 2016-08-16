# SeymourSolo
This repo contains modifications to the 3DR Solo python scripts that Southern Miss uses on their Solos.  Presently this only includes a relay controller used to take pictures with a mounted Qx1.  

Here is a link to relay module I am using:

http://numato.com/1-channel-usb-powered-relay-module/


This is a youtube link to a demo of the relay controlling the Qx1:

https://www.youtube.com/watch?v=wNmwPvXV5PA


dronekit-sitl copter-3.3 --home=31.245373,-89.399773,584,353

mavproxy.py --master tcp:127.0.0.1:5760 --sitl 127.0.0.1:5501 --out 192.168.1.122:14550 --out 127.0.0.1:14551

