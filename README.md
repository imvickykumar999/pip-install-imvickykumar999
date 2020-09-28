# pip install --upgrade vixtor

## [vixtor version 0.0.2](https://github.com/imvickykumar999/vixtor/blob/master/vector%20version%200.0.2/vixtor/threeDvector.py)

[![pypi](https://raw.githubusercontent.com/imvickykumar999/vixtor/master/screenshot%20vixtor%20version%200.0.2.png)](https://pypi.org/project/vixtor/)

#### ...in version 0.0.2, printing parameter is introduced, for example : 
    angbw2line(a1=[3,2,-4], b1=[1,2,2], a2=[5,-2,0], b2=[3,2,6], printing = True)
    ...if printing is True then only called function will print info else only return.

## [Available functions you can try...](https://github.com/imvickykumar999/vixtor/blob/master/vector/vixtor/__init__.py)

# Package : vixtor = [Vix].(my nickname) + 3D_Vec.[tor]

## [TUTORIAL.ipynb : pip install vixtor](https://github.com/imvickykumar999/vixtor/blob/master/pip%20install%20vixtor%20version%200.0.2.ipynb)

#### ...made with love and hardwork ;)

# [Post on LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:6715639149992394752/)

### ...this package can solve most of the questions of chapter 11, [NCERT](https://github.com/imvickykumar999/vixtor/blob/master/NCERT-Books-for-class%2012-Maths-Chapter%2011.pdf) (3D Vector) of class 12th.

### ...checkout my [linkedin post](https://www.linkedin.com/feed/update/urn:li:activity:6715639149992394752/) and [YouTube Tutorial](https://www.youtube.com/watch?v=eeZB80pLPP8) to know how to use this package's function also fully explained by solving questions.

![plane](https://raw.githubusercontent.com/imvickykumar999/vixtor/master/vixtor.png)

# [How to Upload to PyPi :](https://github.com/fhamborg/news-please/wiki/PyPI---How-to-upload-a-new-version)

1. creating a folder: any name
2. creating a sub folder : [vector](https://github.com/imvickykumar999/vixtor/tree/master/vector%20version%200.0.2)
3. creating a sub folder : vixtor
4. create __init__.py inside 2nd folder
5. create [setup.py](https://github.com/imvickykumar999/vixtor/blob/master/vector%20version%200.0.2/setup.py) inside 1st folder
6. pip install setuptools
7. import setuptools
8. define setup configuration inside setup.py file
9. include manifest.in
10. include readme.txt
11. include license.txt
13. run 'python setup.py sdist' cmd in terminal
14. install twine package :'pip install twine'
15. twine upload dist/*
or, python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
16. Enter your PyPi username and then password.
