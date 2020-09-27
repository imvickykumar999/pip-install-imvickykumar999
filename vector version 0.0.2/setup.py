from setuptools import setup, find_packages

setup(
    name = 'vixtor', # while installing pacakge
    version = '0.0.2',
    description = 'Solves questions like 3D vector.',
    long_description = open('Readme.md').read(),
    url = 'https://github.com/imvickykumar999/vixtor',
    author = 'Vicky Kumar',
    keywords = ['custom','python package','function and class','3D line', 
    '3D plane', 'angle bw planes or line', 'distance bw point and plane'],
    license = 'MIT',
    packages = ['vixtor'], # while importing package
    install_requires = ['']
)