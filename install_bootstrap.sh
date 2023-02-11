sudo apt install python3
sudo apt install pip3
sudo pip3 install scapy
read networkid_zerotier
if [ -z "$networkid_zerotier" ] {    
    curl -s https://install.zerotier.com | sudo bash
    zerotier-cli join $networkid_zerotier
    }
fi
git clone https://github.com/lthiery/SPI-Py.git
python3 SPI-Py/setup.py
git clone https://github.com/pimylifeup/MFRC522-python.git
python3 MFRC522-python/setup.py
read filetoberunatstartpath
echo "$filetoberunatstartpath"+" # added dentet gui interface binary to run at start" | tee -a ~/.bashrc


