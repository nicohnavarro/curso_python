# Describir la configuracion del paquete distribuible
from setuptools import setup

setup(
    name="paquete_calculos",
    version="1.4",
    description="Paquete de Calculos Basicos",
    author="Nicolas",
    author_email="nicohnavarro@gmail.com",
    url="www.github.com/nicohnavarro",
    packages=["paquetes","paquetes.paquete_calculos"] #ruta Completa!
    #en consola sobre el directorio que vamos a utilizar ->python setup.py sdist
    #en consola adentro del directorio dist creado ->pip3 install nombre del archivo zip
    #en consola adentro del directorio dist creado ->pip3 uninstall nombre del archivo zip
)