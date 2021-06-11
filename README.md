# Installation

ssh into py with following command (using cmd) `ssh pi@192.168.2.2` accept the authentication by typing yes if prompted. Put in the ssh password default is `companion` (i changed yours to `tunapro1`) then paste the command below and reboot the device.

```sh
cd && wget https://github.com/tunapro1234/eva2020sub/archive/refs/tags/0.3.zip && unzip 0.3.zip && mv eva2020sub* eva2020sub && cd eva2020sub && sudo bash setup.sh
```

Log file is located in: `/home/pi/eva2020sub/log.txt`. If there is no log file in the specified path, contact me.
Every 5 seconds it tries to connect pixhawk at `/dev/ttyACM0`. Path could be different i am not sure. If it does not connect, again contact me.

# Cleaning the installation

```sh
cd && sudo rm -rf 0.3.zip eva2020sub /etc/rc.local && sudo mv /etc/rc.local.old /etc/rc.local
```
