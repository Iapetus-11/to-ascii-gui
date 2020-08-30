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
        self.width = 300
        self.height = 400

        self.filepath = None  # required
        self._type = None  # required
        self.scale = 1
        self.gradient = 0
        self.fps = 30

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.layout = QGridLayout() # two columns

        self.source_label_1 = QLabel('Source:')
        self.source_label_2 = QLabel('Not Chosen')
        self.layout.addWidget(self.source_label_1, 0, 0)
        self.layout.addWidget(self.source_label_2, 0, 1)

        self.camera_button = QPushButton('Use Camera')
        self.camera_button.clicked.connect(lambda: self.option_camera())

        self.file_button = QPushButton('Choose File')
        self.file_button.clicked.connect(lambda: self.option_file())

        self.layout.addWidget(self.camera_button, 1, 1)
        self.layout.addWidget(self.file_button, 1, 0)

        #self.

        self.setLayout(self.layout)
        self.show()

    def option_camera(self):
        print('camera button')

    def option_file(self):
        print('file button')

if __name__ == '__main__':
    app = QApplication([])
    app.setStyle('Fusion')
    ex = App()
    sys.exit(app.exec_())
