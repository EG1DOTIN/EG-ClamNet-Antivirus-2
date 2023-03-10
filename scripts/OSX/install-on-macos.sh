#!/bin/bash

CONFIG_FOLDER=/usr/local/etc/clamav
CLAMD_CONFIG_FILE=$CONFIG_FOLDER/clamd.conf
FRESHCLAM_CONFIG_FILE=$CONFIG_FOLDER/freshclam.conf
DB_FOLDER=/usr/local/var/lib/clamav
RUN_FOLDER=/usr/local/var/run/clamav
LOG_FOLDER=/usr/local/var/log
CLAMD_LOG_FILE=$LOG_FOLDER/clamd.log
CLAMD_ERROR_LOG_FILE=$LOG_FOLDER/clamd.error.log
FRESHCLAM_LOG_FILE=$LOG_FOLDER/freshclam.log
FRESHCLAM_ERROR_LOG_FILE=$LOG_FOLDER/freshclam.error.log

sudo chown -R $(whoami) "$LOG_FOLDER"
sudo chmod 777 "$LOG_FOLDER"

( brew list --versions clamav > /dev/null ) || brew install clamav || exit

[ -e "$CLAMD_CONFIG_FILE" ] || (
  sudo cp "${CLAMD_CONFIG_FILE}.sample" "$CLAMD_CONFIG_FILE"
  sudo sed -e "s/# Example config file/# Config file/" \
           -e "s/^Example$/# Example/" \
           -e "s/^#LogFile .*/LogFile ${CLAMD_LOG_FILE//\//\\/}/" \
           -e "s/^#PidFile .*/PidFile ${RUN_FOLDER//\//\\/}\/clamd.pid/" \
           -e "s/^#DatabaseDirectory .*/DatabaseDirectory ${DB_FOLDER//\//\\/}/" \
           -e "s/^#LocalSocket .*/LocalSocket ${RUN_FOLDER//\//\\/}\/clamd.socket/" \
           -i -n "$CLAMD_CONFIG_FILE"
)
[ -e "$FRESHCLAM_CONFIG_FILE" ] || (
  sudo cp "${FRESHCLAM_CONFIG_FILE}.sample" "$FRESHCLAM_CONFIG_FILE"
  sudo sed -e "s/# Example config file/# Config file/" \
           -e "s/^Example$/# Example/" \
           -e "s/^#DatabaseDirectory .*/DatabaseDirectory ${DB_FOLDER//\//\\/}/" \
           -e "s/^#UpdateLogFile .*/UpdateLogFile ${FRESHCLAM_LOG_FILE//\//\\/}/" \
           -e "s/^#PidFile .*/PidFile ${RUN_FOLDER//\//\\/}\/freshclam.pid/" \
           -e "s/^#NotifyClamd .*/NotifyClamd ${CLAMD_CONFIG_FILE//\//\\/}/" \
           -i -n "$FRESHCLAM_CONFIG_FILE"
)
sudo mkdir -p "$DB_FOLDER"
sudo mkdir -p "$RUN_FOLDER"
[ -e "$CLAMD_LOG_FILE" ] || sudo touch "$CLAMD_LOG_FILE"
[ -e "$CLAMD_ERROR_LOG_FILE" ] || sudo touch "$CLAMD_ERROR_LOG_FILE"
[ -e "$FRESHCLAM_LOG_FILE" ] || sudo touch "$FRESHCLAM_LOG_FILE"
[ -e "$FRESHCLAM_ERROR_LOG_FILE" ] || sudo touch "$FRESHCLAM_ERROR_LOG_FILE"
sudo chown -R root:wheel "$CONFIG_FOLDER"
sudo chown -R $(whoami) "$DB_FOLDER"
sudo chown -R $(whoami) "$RUN_FOLDER"
sudo chown $(whoami) "$CLAMD_LOG_FILE" "$CLAMD_ERROR_LOG_FILE" "$FRESHCLAM_LOG_FILE" "$FRESHCLAM_ERROR_LOG_FILE"
sudo chmod 777 "$CLAMD_CONFIG_FILE" "$FRESHCLAM_CONFIG_FILE" 
sudo chmod 777 "$CLAMD_LOG_FILE" "$CLAMD_ERROR_LOG_FILE" "$FRESHCLAM_LOG_FILE" "$FRESHCLAM_ERROR_LOG_FILE"

DAEMON_FOLDER=/Library/LaunchDaemons
CLAMD_DAEMON_NAME=clamav.clamd
CLAMD_DAEMON_FILE=$DAEMON_FOLDER/$CLAMD_DAEMON_NAME.plist
FRESHCLAM_DAEMON_NAME=clamav.freshclam
FRESHCLAM_DAEMON_FILE=$DAEMON_FOLDER/$FRESHCLAM_DAEMON_NAME.plist
[ -d "$DAEMON_FOLDER" ] || sudo mkdir "$DAEMON_FOLDER"

sudo freshclam -v
sudo tee "$CLAMD_DAEMON_FILE" << EOF > /dev/null
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>${CLAMD_DAEMON_NAME}</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/local/sbin/clamd</string>
        <string>--foreground</string>
    </array>
    <key>KeepAlive</key>
    <true/>
    <key>StandardErrorPath</key>
    <string>${CLAMD_ERROR_LOG_FILE}</string>
</dict>
</plist>
EOF
sudo tee "$FRESHCLAM_DAEMON_FILE" << EOF > /dev/null
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>${FRESHCLAM_DAEMON_NAME}</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/local/bin/freshclam</string>
        <string>--daemon</string>
        <string>--foreground</string>
    </array>
    <key>KeepAlive</key>
    <true/>
    <key>StandardErrorPath</key>
    <string>${FRESHCLAM_ERROR_LOG_FILE}</string>
</dict>
</plist>
EOF
sudo chown root:wheel "$CLAMD_DAEMON_FILE" "$FRESHCLAM_DAEMON_FILE"
sudo chmod 0644 "$CLAMD_DAEMON_FILE" "$FRESHCLAM_DAEMON_FILE"
sudo launchctl load "$CLAMD_DAEMON_FILE" "$FRESHCLAM_DAEMON_FILE"
