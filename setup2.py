from setuptools import setup

APP = ['pystebinTechdata.py']
DATA_FILES = []
OPTIONS = {
 'iconfile':'images_1024x1024.icns',
 'argv_emulation': True,
 'packages': ['certifi'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)