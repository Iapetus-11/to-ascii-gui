from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import toascii
import sys
import os

class App(QWidget):
    def __init__(self):
        super().__init__()

        self.title = 'To-ASCII'

        # window positioning
        self.left = 50
        self.top = 50

        # window dimensions
        self.width = 300
        self.height = 10

        self.filepath = None  # required
        self._type = None  # required
        self.scale = 1
        self.gradient = 0
        self.fps = 30

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #self.layout = QGridLayout() # two columns
        self.layout = QVBoxLayout()
        self.sub_layouts = (QHBoxLayout(), QHBoxLayout(), QHBoxLayout(), QHBoxLayout(),)

        self.source_label = QLabel('Source: None Chosen')
        self.sub_layouts[0].addWidget(self.source_label)

        self.camera_button = QPushButton('Use Camera')
        self.camera_button.clicked.connect(lambda: self.connect_source_button('live'))
        self.sub_layouts[1].addWidget(self.camera_button)

        self.file_button = QPushButton('Choose File')
        self.file_button.clicked.connect(lambda: self.connect_source_button('file'))
        self.sub_layouts[1].addWidget(self.file_button)

        self.scale_slider = QSlider(Qt.Horizontal)
        self.scale_slider.valueChanged[int].connect(self.connect_scale_slider)
        self.scale_slider.setValue(100)
        self.sub_layouts[2].addWidget(self.scale_slider)

        self.scale_label = QLabel('Scale 1.00x')
        self.sub_layouts[2].addWidget(self.scale_label)

        self.show_button = QPushButton('Show ASCII')
        self.show_button.clicked.connect(lambda: self.connect_show_button())
        self.sub_layouts[3].addWidget(self.show_button)

        for sub_layout in self.sub_layouts:
            self.layout.addLayout(sub_layout)

        self.setLayout(self.layout)
        self.show()

    def connect_source_button(self, _type):
        if _type == 'live':
            self.source_label.setText('Source: Camera')
            self.filepath = 0
            self._type = 'live'
        elif _type == 'file':
            file, _ = QFileDialog.getOpenFileName(self, "Choose a file", "", "Image Files (*.png *.jpg *.bmp *.jpeg);;Video Files (*.avi *.mp4 *.mov *.mkv *.gif *.mpg *.mpeg)")

            if file:
                if file[-3:] in ('png', 'jpg', 'bmp', 'jpe'):
                    self._type = 'image'
                else:
                    self._type = 'video'

                self.filepath = file

                file = file if len(file) < 40 else '...' + file[-37:]

                self.source_label.setText(f'Source: {file}')

    def connect_scale_slider(self, value):
        try:
            self.scale = (value + 1) / 100)
            self.scale_label.setText('Scale: {:1.2f}x'.format(self.scale)
        except AttributeError:
            pass

    def connect_show_button(self):
        os.system(f'to-ascii -t {self._type} -f {self.filepath} -s {self.scale} -r 30 -g 1 && pause > nul')

if __name__ == '__main__':
    app = QApplication([])
    ex = App()
    sys.exit(app.exec_())
