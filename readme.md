# install requirment 
    sudo apt-get install python3-tk

# create exec
    pyinstaller -F --add-data "./config:./config" --icon=./config/icon.png create_quotation.py --onefile 

# Version cli
    python create_quotation.py -m cli
