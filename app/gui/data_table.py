import datetime
import logging
from typing import Optional, Union

from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg

from app.db.db import DB

from app.setup_logging import setup_logger


logger = setup_logger('data_table', logging.DEBUG)


class TableView(qtw.QTableView):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.db = self.initialize_database()

        self.initialize_model()

        self.setupUI()
