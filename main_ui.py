import os
projectPath  = os.path.join(os.path.dirname(__file__))
import logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] (%(threadName)-10s) %(message)s')
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from gui.Ui_MainWindow import Ui_MainWindow
import sys
import time
        

class MainApp(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.login_button.clicked.connect(self.buttonClicked)
    
    def buttonClicked(self):
        username = self.usernameLineEdit.text().lower()
        print(username)

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, 'Message', 
            "Are you sure to quit?", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
            

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())