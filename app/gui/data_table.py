import datetime
import logging
from typing import Optional, Union

from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg



format_str = '%(name)s:%(levelname)s:%(message)s'
logging.basicConfig(format=format_str, level=logging.DEBUG)
logger = logging.getLogger('data_table')


class TableView(qtw.QTableView):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.db = self.initialize_database()

        self.initialize_model()

        self.setupUI()
