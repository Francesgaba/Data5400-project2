#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from setuptools import setup, find_packages

setup(
    name='project2',
    version='0.1.0',
    author='ziqi huang',
    author_email='zikih25@gmail.com',
    description='project2',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Francesgaba/Data5400-project2',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)


# In[ ]:




