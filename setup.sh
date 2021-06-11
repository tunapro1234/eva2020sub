# rc.local setup
mv /etc/rc.local /etc/rc.local.old
cp rc.local /etc/rc.local

# vim setup ehehehe
apt install vim -y
cp -r .vim ~/.vim
cp .vimrc ~/.vimrc
echo ok
