#!/bin/sh +x
sudo curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py 
sudo python3 get-pip.py
sudo python3 -m pip install jupyter
sudo python3 -m pip install -r html/requirements.txt
