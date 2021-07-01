# setup file for py2exe for conversion of script into Win exe

from distutils.core import setup
import py2exe

setup(console = ['metadump_gui.py'])