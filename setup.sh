# rc.local setup
mv /etc/rc.local /etc/rc.local.old
cp rc.local /etc/rc.local

# vim setup ehehehe
apt install vim -y

cp -r .vim /home/pi/.vim
cp .vimrc /home/pi/.vimrc

cp -r .vim root/.vim
cp .vimrc root/.vimrc

echo ok
