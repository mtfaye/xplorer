# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='Profiler',
    version='0.01',
    description='Automate data profiling',
    long_description=long_description,
    classifiers=[
        'Development Status :: 0.01 - Alpha',
        'Environment :: Console',   
        'Intended Audience :: Resolution AML Compliance Data Experts',
        'Programming Language :: Python :: 3.7',
        'Topic :: Data Analysis :: Data Wrangling :: Data Transformation',
        'License :: Not Licensed yet',
        'Operating System :: OS Independent, just update path format on config.py for Windows.'
    ],
    keywords='Data Profiler',
    author='Resolution Inc',
    author_email='mouhameth.faye@resolutioninc.ca',
    maintainer='Mouhameth T. Faye',
    maintainer_email='mouhameth.faye@resolutioninc.ca',
    url='',
    license='',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'profiler = profiler.profiler:main',
        ]
    },
    install_requires=[
        'pandas','fire','seaborn','xlsxwriter','pyodbc'
        ]
    )