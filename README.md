# braiins_uninstaller
 
Clone the repo by running : 

    git clone https://github.com/VirusHQ/braiins_uninstaller.git 


Make sure that you have python 3 installed on the system (Ubuntu WSL already comes with it)
Then run these commands:

    cd braiins_uninstaller/ (opens uninstaller directory)
    nano iplist.txt (edit this file , add the ip addresses that have braiins on them)
    python3 run.py (runs the uninstaller)

if running "python3 run.py" comes up with a pip error run :

    sudo apt update && sudo apt install python3-pip -y 
    
and this will fix the errors