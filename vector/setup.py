from setuptools import setup, find_packages

setup(
    name = 'vixtor', # while installing pacakge
    version = '0.0.1',
    description = 'Solves questions like 3D vector.',
    long_description = open('Readme.txt').read(),
    url = 'https://github.com/imvickykumar999',
    author = 'Vicky Kumar',
    keywords = ['custom','python package','function and class','3D line', 
    '3D plane', 'angle bw planes or line', 'distance bw point and plane'],
    license = 'MIT',
    packages = ['vixtor'], # while importing package
    install_requires = ['']
)