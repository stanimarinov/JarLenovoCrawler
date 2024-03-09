""" module gui_app.py """
import logging
import sys

from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg

from app.data_proces import DataProces
from app.config_loader import load_config
from app.setup_logging import setup_logger

from app.gui.data_table import DataTable

logger = setup_logger('qui_app', logging.DEBUG)

class MainWindow(qtw.QMainWindow):
    def __init__(self , *args, **kwargs):
        super().__init__(*args, **kwargs)