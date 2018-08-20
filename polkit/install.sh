echo "Disable polkit password prompts..."
sudo cp disable-passwords.pkla /var/lib/polkit-1/localauthority/50-local.d/disable-passwords.pkla
