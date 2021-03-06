from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import toascii
import time
import sys

"""class ResultWindow(QWidget):
    def __init__(self, kwargs):
        QWidget.__init__(self)

        for kwarg in list(kwargs):
            self.__dict__[kwarg] = kwargs[kwarg]

        self.title = 'Viewer'

        self.left = 100
        self.top = 100

        self.ascii_obj = None

        self.init()

    def init(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self._width, self._height)

        if self._type == 'image':
            self.ascii_obj = toascii.Image(self.filepath, scale=self.scale, gradient=self.gradient)
        elif self._type == 'video':
            self.ascii_obj = toascii.Video(self.filepath, scale=self.scale, gradient=self.gradient)
        elif self._type == 'live':
            self.ascii_obj = toascii.Live(self.filepath, scale=self.scale, gradient=self.gradient, fps=self.fps)

        self.show_label = QLabel(f'\n{" "*self.ascii_obj.scaled__width}'*self.ascii_obj.scaled__height)

        if self._type != 'live':
            self.ascii_obj.convert()

        self.show()

    def show(self):
        QWidget.show(self)

        if self._type == 'live':
            self.view_live()
        elif self._type == 'video':
            self.view_video()
        elif self._type == 'image':
            self.view_image()

    def view_live(self):
        while True:
            #start = time.perf_counter()

            img = self.ascii_obj.fetch_frame()  # returns text

            #diff = start - time.perf_counter()
            #time.sleep((spf - diff + abs(spf - diff)) / 2)
            time.sleep(.05) # 20 fps I think

            self.show_label.setText(img)
"""

class App(QWidget):
    def __init__(self, app):
        QWidget.__init__(self)

        self.app = app
        self.app_palette = QPalette()

        self.title = 'To-ASCII'

        # window positioning
        self.left = 50
        self.top = 50

        # window dimensions
        self._width = 300
        self._height = 10

        self.filepath = None  # required
        self._type = None  # required
        self.scale = 1
        self.gradient = 0
        self.fps = 30

        self.res_window = None

        self.init()

    def init(self):
        # Dark mode fusion
        self.app.setStyle("Fusion")
        self.app_palette.setColor(QPalette.Window, QColor(53, 53, 53))
        self.app_palette.setColor(QPalette.WindowText, Qt.white)
        self.app_palette.setColor(QPalette.Base, QColor(25, 25, 25))
        self.app_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        self.app_palette.setColor(QPalette.ToolTipBase, Qt.white)
        self.app_palette.setColor(QPalette.ToolTipText, Qt.white)
        self.app_palette.setColor(QPalette.Text, Qt.white)
        self.app_palette.setColor(QPalette.Button, QColor(53, 53, 53))
        self.app_palette.setColor(QPalette.ButtonText, Qt.white)
        self.app_palette.setColor(QPalette.BrightText, Qt.red)
        self.app_palette.setColor(QPalette.Link, QColor(42, 130, 218))
        self.app_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        self.app_palette.setColor(QPalette.HighlightedText, Qt.black)
        self.app.setPalette(self.app_palette)
        self.app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self._width, self._height)

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
            file, _ = QFileDialog.getOpenFileName(self, 'Choose a file', '', 'Image Files (*.png *.jpg *.bmp *.jpeg);;Video Files (*.avi *.mp4 *.mov *.mkv *.gif *.mpg *.mpeg)', options=QFileDialog.Options())

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
            self.scale = (value + 1) / 100
            self.scale_label.setText('Scale: {:1.2f}x'.format(self.scale))
        except AttributeError:
            pass

    def connect_show_button(self):
        #self.res_window = ResultWindow(self.__dict__)
        #self.res_window.show()

        if self.filepath is None:
            pass

if __name__ == '__main__':
    main = QApplication([])
    app = App(main)
    main.exec()
