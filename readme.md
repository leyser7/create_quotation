# create exec
pyinstaller -F --add-data "./config:./config" --icon=./config/icon.png create_quotation.py --onefile 

# Version cli
    python createPrice.py -m cli
