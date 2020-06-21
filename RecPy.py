import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import sounddevice as sd
from scipy.io.wavfile import write


class rpcode(QDialog):
    def __init__(self):
        super(rpcode, self).__init__()
        loadUi('recorderApp.ui', self)
        self.Return = 0
        self.fs = 16000
        self.a = 0
        self.Text.setText('Kindly mention duretion of recording and click start recording button....')
        self.START.clicked.connect(self.STARTVOICERECORDING)

    @pyqtSlot()
    def STARTVOICERECORDING(self):
        Duration = int(self.input.toPlainText())
        self.a = sd.rec(int(Duration * self.fs), self.fs, 1)
        sd.wait()
        write('F:/runtimeTerrorr/output/out.wav', self.fs, self.a)
        self.Text.setText('Recording Done')


app = QApplication(sys.argv)
window = rpcode()
window.show()
try:
    sys.exit(app.exec_())
except:
    print('exiting')
