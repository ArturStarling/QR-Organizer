#! /bin/bash

# atualiza a lista de repositórios do sistema
sudo apt update

sudo rm ~/.buildozer ~/.android 

# baixa o crystax-ndk-10.3.2
mkdir ~/cristax
sudo apt -y install wget
wget -c -P ~/cristax/ https://www.crystax.net/download/crystax-ndk-10.3.2-linux-x86_64.tar.xz
tar -C ~/cristax -xJf ~/cristax/crystax-ndk-10.3.2-linux-x86_64.tar.xz

# instala dependências
sudo dpkg --add-architecture i386
sudo apt install -y python3
sudo apt install -y python3-venv
sudo apt install -y python3-pip
sudo apt install -y python3-dev		
sudo apt install -y build-essential	
sudo apt install -y git			
sudo apt install -y ffmpeg		
sudo apt install -y libsdl2-dev		
sudo apt install -y libsdl2-image-dev	
sudo apt install -y libsdl2-mixer-dev	
sudo apt install -y libsdl2-ttf-dev	
sudo apt install -y libportmidi-dev	
sudo apt install -y libswscale-dev	
sudo apt install -y libavformat-dev	
sudo apt install -y libavcodec-dev	
sudo apt install -y zlib1g-dev	
sudo apt install -y autoconf
sudo apt install -y automake
sudo apt install -y libtool
sudo apt install -y ccache
sudo apt install -y libncurses5:i386
sudo apt install -y libstdc++6:i386
sudo apt install -y libgtk2.0-0:i386 
sudo apt install -y libpangox-1.0-0:i386
sudo apt install -y libpangoxft-1.0-0:i386
sudo apt install -y libidn11:i386
sudo apt install -y openjdk-8-jdk
sudo apt install -y unzip
sudo apt install -y zlib1g:i386

# cria um ambiente virtual
python3 -m venv .env

# instala as libs necessárias dentro do ambiente virtual
source .env/bin/activate
pip install Cython==0.25.2
pip install buildozer==0.34
pip install colorama
pip install appdirs
pip install sh
pip install jinja2
pip install six
pip install kivy
