#!/usr/bin/python

from distutils.core import setup

setup(
    name='ConsoleBitly',
    version='0.1',
    url="http://github.com/swaroopsm/Console-Bitly",
    license='MIT Licence',
    author="Swaroop SM",
    author_email="swaroop.striker@gmail.com",
    description="A thin wrapper around the bit.ly API",
    long_description=open('README.txt').read(),
    packages=['ConsoleBitly']
    
)
