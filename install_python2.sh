#apt install python
apk add python
apk add curl
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
python -m pip install paho-mqtt
