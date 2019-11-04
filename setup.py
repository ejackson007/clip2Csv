from setuptools import setup

APP = ['pystebinIngram.py']
DATA_FILES = ['1.gif','2.gif']
OPTIONS = {
 'iconfile':'logo.ico',
 'argv_emulation': True,
 'packages': ['certifi'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)