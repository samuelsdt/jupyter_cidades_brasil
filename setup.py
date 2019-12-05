'''
Created on 5 de dez de 2019

@author: Samuel
'''
from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))


with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='jupyter_cidades_brasil', 


    version='1.0',


    description='Mapa coroplético com as cidades brasileiras para visualização no Jupyter Notebook',  # Optional

    url='https://github.com/samuelsdt/jupyter_cidades_brasil', 

    author='Samuel Schmidt', 

    author_email='samuelsdt@hotmail.com',  

    packages=['brlcities'],
  
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4',

   
    install_requires=['ipyleaflet', 'ipywidgets', 'branca'], 

    
    package_data={
        'geodata': ['data.geo.json'],
    },
    
    include_package_data=True
)
