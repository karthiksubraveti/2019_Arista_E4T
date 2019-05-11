#!/bin/sh +x
git clone https://github.com/karthiksubraveti/2019_Arista_E4T.git
cd 2019_Arista_E4T
sudo curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py 
sudo python3 get-pip.py
sudo python3 -m pip install jupyter
sudo python3 -m pip install -r html/requirements.txt
