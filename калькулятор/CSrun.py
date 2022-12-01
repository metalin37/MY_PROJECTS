from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5 import uic,QtCore
import sys

preclass = uic.loadUiType("CS.ui")[0]

class NewWindow(QMainWindow, preclass):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.ShowP)
        self.pushButton_2.clicked.connect(self.Rasschet)
        self.w_view = 0

    def Rasschet(self):
        self.lineEdit_1.setText('Рассчет')
        text2 = int(self.lineEdit_2.text())
        text3 = int(self.lineEdit_3.text())
        self.lineEdit_4.setText(str(text2 + text3))
        

app = QApplication(sys.argv)
myWindow = NewWindow(None)
myWindow.show()
app.exec_()

"""

app = QApplication([])
win = uic.loadUi("SerialPanel2.ui")
#win = NewWindow(None)
win.show()
sys.exit(app.exec())
"""