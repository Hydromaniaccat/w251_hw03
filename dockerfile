

FROM w251/cuda:dev-tx2-4.2.1_b97

ARG URL=http://169.44.201.108:7002/jetpacks/4.2.1
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt install -y git pkg-config wget build-essential cmake unzip

RUN apt-get -y install python-opencv
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python get-pip.py
RUN python -m pip install numpy
RUN python -m pip install paho-mqtt
RUN mkdir /python
COPY facial_detection.py /python

WORKDIR /tmp
# RUN rm *.deb

RUN curl $URL/libopencv_3.3.1-2-g31ccdfe11_arm64.deb  -so libopencv_3.3.1-2-g31ccdfe11_arm64.deb
RUN curl $URL/libopencv-dev_3.3.1-2-g31ccdfe11_arm64.deb -so libopencv-dev_3.3.1-2-g31ccdfe11_arm64.deb
RUN curl $URL/libopencv-python_3.3.1-2-g31ccdfe11_arm64.deb -so libopencv-python_3.3.1-2-g31ccdfe11_arm64.deb

RUN apt install -y  libtbb-dev libavcodec-dev libavformat-dev libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgtk2.0-dev
RUN apt install -y libswscale-dev libv4l-dev
RUN dpkg -i *.deb

RUN apt install -y libcanberra-gtk-module libcanberra-gtk3-module libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev 

RUN rm -f /tmp/*.deb
