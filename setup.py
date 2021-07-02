# setup file for py2exe for conversion of script into Win exe
# as described in https://www.py2exe.org/index.cgi/Tutorial

from distutils.core import setup
import py2exe

setup(console = ['metadump_gui.py'])
