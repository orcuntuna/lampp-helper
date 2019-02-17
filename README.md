
# Lampp Helper (xampp linux)
open, stop and open with one command for linux lampp

## How to install?
1. Download xampp file on this repository
2. Copy xampp file to /usr/local/bin (for path)
3. Give permission for run (+x)

Follow on terminal:

    cd /usr/local/bin/
    sudo cp ~/Downloads/lampp-helper/xampp .
    sudo chmod +x xampp

**Notice:** edit your downloaded file address by yourself
**Info:** this script need python3 and lampp


## How to use?

    cd $(xampp)
    xampp start
    xampp stop
    xampp gui
    xampp --help
