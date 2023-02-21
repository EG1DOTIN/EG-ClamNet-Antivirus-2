#!/bin/bash

brew uninstall clamav
sudo rm -rf /usr/local/etc/clamav/
sudo rm /Library/LaunchDaemons/clamav.clamd.plist
sudo rm /Library/LaunchDaemons/clamav.freshclam.plist
