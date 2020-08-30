from PyQt5.QtWidgets import *
import toascii
import sys

class App(QWidget):
    def __init__(self):
        super().__init__()

        self.title = 'To-ASCII'

        # window positioning
        self.left = 50
        self.top = 50

        # window dimensions
        self.width = 640
        self.height = 480

        self.filepath = None  # required
        self._type = None  # required
        self.scale = 1
        self.gradient = 0
        self.fps = 30

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.layout = QHBoxLayout() # two columns

        self.layout.addWidget(QRadioButton('Camera'))
        self.layout.addWidget(QRadioButton('Camera Roll'))

        self.setLayout(self.layout)
        
        self.show()

if __name__ == '__main__':
    app = QApplication([])
    ex = App()
    sys.exit(app.exec_())
