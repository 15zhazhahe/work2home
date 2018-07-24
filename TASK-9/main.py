#-*- coding:utf-8 -*-

import sys
from PIL import Image
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()

        self.initUI()


    def initUI(self):
        
        layout = QVBoxLayout()

        layout_h = QHBoxLayout()
        
        self.combo = QComboBox(self)  
        self.combo.addItem("Ubuntu")  
        self.combo.addItem("Mandriva")  
        self.combo.addItem("Fedora")  
        self.combo.addItem("Red Hat")  
        self.combo.addItem("Gentoo")  
        self.connect(combo, SIGNAL('activated(QString)'),self.onActivated)
        layout_h.addWidget(self.combo)

        layout.addLayout(layout_h)
        
        self.btn = QPushButton()
        self.btn.clicked.connect(self.loadImage)
        self.btn.setText('Load Image')
        layout.addWidget(self.btn)

        self.imageView = QLabel("Please Load a Image")
        self.imageView.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.imageView)
        self.setLayout(layout)

        self.setGeometry(300, 100, 2000, 1200)
        self.setWindowTitle('Tooltips')    
        self.show()

    def onActivated(self, text):  
        print text 

    def pil2pix(self, im):
        im = im.convert("RGBA")
        data = im.tobytes("raw","RGBA")
        qim = QImage(data, im.size[0], im.size[1], QImage.Format_ARGB32)
        pix = QPixmap.fromImage(qim)
        return pix

    def loadImage(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Load Image', '.', 'Image files(*.jpg *.gif *.png)')
        img = Image.open(fname)
        self.imageView.setPixmap(self.pil2pix(img))
        

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())