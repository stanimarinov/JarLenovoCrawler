""" module gui_app.py """
import logging
import sys

from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg

format_str = '%(name)s:%(levelname)s:%(message)s'
logging.basicConfig(format=format_str, level=logging.DEBUG)
logger = logging.getLogger('gui_app')



class MainWindow(qtw.QMainWindow):
    def __init__(self , *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setupUI(self):
        self.setWindowTitle('Laptop Data')

        layout = qtw.QVBoxLayout()
        lblTableCaption = qtw.QLabel('Laptop Data')
        lblTableCaption.setObjectName('lblTableCaption')
        lblTableCaption.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(lblTableCaption)

        btnsLayout = qtw.QHBoxLayout()
        self.btnCrawlerRun = qtw.QPushButton('Run Crawler')
        self.btnShowData = qtw.QPushButton('Show Data')

        btnsLayout.addWidget(self.btnCrawlerRun)
        btnsLayout.addWidget(self.btnShowData)
        layout.addLayout(btnsLayout)

        layout.addSpacing(10)
        
        mainWidget = qtw.QWidget()
        mainWidget.setLayout(layout)
        self.setCentralWidget(mainWidget)

        self.center_window()    

    def center_window(self):
            window_width = 400
            window_height = 400
            primary_screen = qtg.QGuiApplication.primaryScreen()
            if primary_screen:
                available_geometry = primary_screen.availableGeometry()
    
            self.setGeometry(
                (available_geometry.width() - window_width) // 2,
                (available_geometry.height() - window_height) // 2,
                window_width,
                window_height
            )          

class MainApp(qtw.QApplication):
   def __init__(self, *args) -> None:
       super().__init__(*args)
       self.main_window = MainWindow()
       self.main_window.show()

if __name__ == '__main__':
    app = MainApp(sys.argv)
    sys.exit(app.exec())       