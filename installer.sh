#!/bin/bash

echo "Installing..."

git clone https://github.com/Roentengium/package-installer-project /home/$USER/upinst

cd /home/$USER/upinst

echo "This part requires sudo, please enter your password."

sudo mv upinst /usr/local/bin
sudo chown $USER /usr/local/bin/upinst
sudo chmod +x /usr/local/bin/upinst

echo "Installation finished!"
