# QR-Organizer
Através da linguagem de programação Python 3 e da biblioteca OpenCV, desenvolvemos um código que reconhece e lê o conteúdo de QrCodes que estarão anexados a objetos de interesse, para assim retornar uma imagem demonstrando a localização em que o material é normalmente mantido.

![1](1.png)

Além disso, você pode escrever o nome do objeto, como "resistors", e receber a mesma imagem que apareceria identificando o QR do "resistors".

O código foi adaptado para um .apk e pode ser utilizado no android.


# Prerequisites
We used a notebook with Linux Ubuntu 16.04 LTS and 18.04 LTS, others versions and operating systems were not tested. We also used an android device for the whole project.

## Python 3.6 
Python 3.6 was used for the project


## Anaconda 3.8.0
We kept the envornments organized with anaconda 3.8.0. More info [here](https://www.anaconda.com/products/individual)

## OpenCV 4.1.2
OpenCV was used to identify QR Codes, analise them and manipulate images.

## Kivy 1.11.0
We built a iterface with python using the kivy library.

## Buildozer 0.39
To convert the code to .apk format and send it to an android device, we used buildozer.


# Building an apk by yourself
Clone this repository:

	git clone https://github.com/ArturStarling/QR-Organizer
	
Install anaconda(optional). How to download and install anaconda is documented [here](https://docs.anaconda.com/anaconda/install/).
Create an environment:

	conda create -n [repository name]
	
Then activate it:

	conda activate [repository name]
	
Now you need to install python 3.6:

	conda install python==3.6

Install all libraries([OpenCV](https://anaconda.org/conda-forge/opencv), [Kivy](https://anaconda.org/conda-forge/kivy) and [Buildozer](https://anaconda.org/travis/buildozer)) and their dependecies(for [buildozer](https://buildozer.readthedocs.io/en/latest/installation.html))

Now connect your cellphone(developer mode needs to be activated) in your computer and then execute the following commands:
	
	buildozer init


	buildozer android debug deploy run


# Test it on your android device:
1. Download the apk on your android device
2. Create and print QR codes with numeration, for example 1 to 10.

With that, you can already recognize some QR codes and return some images