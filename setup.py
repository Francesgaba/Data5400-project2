#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from distutils.core import setup

setup(
    name='Data5400-project2',
    version='0.2.1',
    description='Classes for webscreping .',
    author='Stefanie Molin',
    author_email='zikih25@gmail.com',
    license='MIT',
    url='https://github.com/Francesgaba/Data5400-project2.git',
    packages=['project2_analysis'],
    install_requires=[
        'matplotlib>=3.0.2',
        'mplfinance>=0.12.7a4',
        'numpy>=1.15.2',
        'pandas>=0.23.4',
        'pandas-datareader>=0.7.0',
        'seaborn>=0.11.0',
        'statsmodels>=0.11.1',
        'yfinance>=0.2.4'
    ],
)




