# create exec
pyinstaller -F --add-data "./config:./config" createPrice.py --onefile

# Version cli
    python createPrice.py -m cli
