""" module gui_app.py """
import logging
import sys

from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg




class MainWindow(qtw.QMainWindow):
    def __init__(self , *args, **kwargs):
        super().__init__(*args, **kwargs)