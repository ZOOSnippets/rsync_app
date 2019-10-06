import sys
import os
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

class MainWindow(qtw.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        ## MainWindow UI
        self.setWindowTitle("PDF Merger App")
        self.setWindowIcon(qtg.QIcon("Pdf.ico"))
        self.initUI()
        self.show()

    def initUI(self):
        ## Main UI Widgets code
        self.createLayout()

    def createLayout(self):
        ## Create UI Layout        
        pass

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    app.setStyle("Fusion")
    mw = MainWindow()
    sys.exit(app.exec_())