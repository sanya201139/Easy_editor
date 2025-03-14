import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class ImageProcessor():
    def __init__(self, save_dir):
        self.filename = None
        self.image = None
        self.save_dir = save_dir
    
    def loadimage(self, filename):
        self.filename = filename
        image_path = os.path.join(workdir, filename)
        self.image = Image.open(image_path)
    
    def showImage(self, path):
        pixmapimage = QPixmap(path)
        label_width, label_heidht = lb_image.width(), lb_image.height()
        scaled_pixmap = pixmapimage.scaled(label_width, label_height, Qt.KeepAspectRatio)
        lb_image.setPixmap(scaled_pixmap)
        lb_image.setVisible(True)

    def do_bw(self):
        self.image = self.image.convert('L')
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def saveImage(self):
        path = os.path.join(workdir, self.save_dir)
        if not (os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)
    def do_flip(self):
        self.image = self.image.rotate(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

save_dir = 'Modified'
workimage = ImageProcessor(save_dir)


app = QApplication([])
win = QWidget()
btn_dir = QPushButton('Папка')
lw_files = QListWidget()
lb_image = QLabel('Картинка')
btn_left = QPushButton('Лево')
btn_right = QPushButton('Право')
btn_flip = QPushButton('Зеркало')
btn_sharp = QPushButton('Резкость')
btn_bw = QPushButton('Ч/Б')
btn_save = QPushButton('Сохранить')
btn_reset = QPushButton('Убрать обработку')


win.resize(700, 400)

row = QHBoxLayout()          
col1 = QVBoxLayout()        
col2 = QVBoxLayout()
col1.addWidget(btn_dir)      
col1.addWidget(lw_files)    
col2.addWidget(lb_image, 95)
row_tools = QHBoxLayout()    
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)
row_tools.addWidget(btn_save)  # Добавляем кнопку в интерфейс
row_tools.addWidget(btn_reset)  # Добавляем кнопку в интерфейс
col2.addLayout(row_tools)


row.addLayout(col1, 20)
row.addLayout(col2, 80)
win.setLayout(row)


workdir = ''

def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def filter(files, extensions):
    result = list()
    for filename in files:
        for expansion in extensions:
            if filename.endswith(extension):
                result.append(filename)
    return result


def showFilenamesList():
    workdir = QFileDialog.getExistingDirectory()
    extensions['jpg', 'png', 'bmp', 'svg', 'eps']

def showChosenImage():
    if lw_files.currentRow() >= 0:
        filename = lw_files.currentItem().text()
        workimage.loadImage(filename)
        image_path = os.path.join(workdir, workimage.filename)
        workimage.showImage(image_path)
lw_files.currentRowChanged.connect(showChosenImage)
btn_bw.clicked.connect(workimage.do_bw)
btn_flip.clicked.connect(workimage.do_flip)
btn_dir.clicked.connect(chooseWorkdir)
win.show()
app.exec()
