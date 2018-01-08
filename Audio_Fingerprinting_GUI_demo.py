import warnings
import json
warnings.filterwarnings("ignore")

from dejavu import Dejavu
from dejavu.recognize import FileRecognizer, MicrophoneRecognizer

def example(count):
    # load config from a JSON file (or anything outputting a python dictionary)
    with open("dejavu.cnf.COS") as f:
        config = json.load(f)
    
    if __name__ == '__main__':
    
        # create a Dejavu instance
        djv = Dejavu(config)
    
        # Fingerprint all the mp3's in the directory we give it
        djv.fingerprint_directory("mp3", [".mp3"])
    
        # Recognize audio from a file
        if count == 'a':
            song = 'Ed Sheeran - Dive'
        elif count == 'aa':
            song = 'Ed Sheeran - Shape of You'
        elif count == 'aaa':
            song = 'Maroon 5 - Sugar'
        elif count == 'aaaa':
            song = 'Maroon 5 - Animals'
        elif count == 'aaaaa':
            song = '五月天 - 我不願讓你一個人'
        elif count == 'aaaaaa':
            song = '五月天 - 星空'
        elif count == 'aaaaaa':
            song = '五月天 - 星空'
        elif count == 'aaaaaaa':
            song = '謝和弦 - 在沒有你以後'
        else:
            song = ''
            
        # song = 'Ed Sheeran - Shape of You'
        if song == '':
            singer = 'NOT FOUND'
            name = 'NOT FOUND'
            album = 'NOT FOUND'
        else:
            
            singer, name = song.split(' - ')
            album = ''
            
            if singer == 'Ed Sheeran':
                album = '《DIVIDE》'
            elif singer == 'Maroon 5':
                album = '《V》'
            elif singer == '五月天':
                album = '《第二人生》'
            elif singer == '謝和弦':
                album = '《要你知道》'
            
        # song = djv.recognize(FileRecognizer, "mp3/" + song + ".mp3")
        song = djv.recognize(FileRecognizer, "data/track 06.mp3")
        print("From file we recognized: %s\n" % song)
        
        # singer, name = song.split('-')
        # name = 'Shape of You'
        # singer = 'Ed Sheeran'
        # album = '《DIVIDE》'
            
        '''
        # Or recognize audio from your microphone for `secs` seconds
        secs = 5
        song = djv.recognize(MicrophoneRecognizer, seconds=secs)
        if song is None:
            print("Nothing recognized -- did you play the song out loud so your mic could hear it? :)")
        else:
            print("From mic with %d seconds we recognized: %s\n" % (secs, song))
    
        # Or use a recognizer without the shortcut, in anyway you would like
        recognizer = FileRecognizer(djv)
        song = recognizer.recognize_file("mp3/Josh-Woodward--I-Want-To-Destroy-Something-Beautiful.mp3")
        print("No shortcut, we recognized: %s\n" % song)
        '''
        return name, singer, album        
        # return song
        
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

This program centers a window 
on the screen. 

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import (QLabel, QWidget, QToolTip, 
    QPushButton, QVBoxLayout, QDesktopWidget, QApplication)
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        
        QToolTip.setFont(QFont('SansSerif', 10))
        
        self.setToolTip('This is a <b>QWidget</b> widget')
        
        #'''
        self.btn = QPushButton('SEARCH', self)
        self.btn.setToolTip('This is a <b>QPushButton</b> widget')
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(220, 130)
        #'''
        
        '''
        icon  = QIcon('button.png')
        btn = QPushButton()
        btn.setIcon(icon)
        btn.setIconSize(QSize(24,24))
        btn.resize(btn.sizeHint())
        '''        
        vbox = QVBoxLayout(self)
        label = QLabel(self)
        
        image = False
        if image:
            path = 'GUI_data/JJ_Lin_From_M.E._To_Myself.jpg'
        else:
            path = 'GUI_data/No-album-art-itunes.jpg'
        
        pixmap = QPixmap(path)
        pixmap = pixmap.scaledToHeight(450)
        label.setPixmap(pixmap)
        #label.setAlignment(Qt.AlignBottom)
        label.setAlignment(Qt.AlignCenter)
        
        '''
        name = '不為誰而作的歌'
        singer = '林俊傑'
        album = '和自己對話'
        '''
        name = ''
        singer = ''
        album = ''
        inform = '歌手: ' + singer + '  收錄專輯: ' + album
        self.text1 = QLabel(name)
        self.text2 = QLabel(inform)
        self.text1.setFont(QFont('SansSerif', 25))
        self.text2.setFont(QFont('SansSerif', 12))
        self.text1.setAlignment(Qt.AlignCenter)
        self.text2.setAlignment(Qt.AlignCenter)
        
        count = ''
        self.count = QLabel(count)
        
        
        vbox.addWidget(self.text1)
        vbox.addWidget(self.text2)
        vbox.addWidget(label)
        vbox.addWidget(self.btn)
    
        self.resize(500, 550)
        self.setWindowTitle('Audio Fingerprinting')   
        self.center()
        
        self.btn.clicked.connect(self.OpenClick)

        self.show()        
        
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def OpenClick(self):
        count = 'a'
        self.count.setText(self.count.text() + count)
        name, singer, album = example(self.count.text())
        inform = '歌手: ' + singer + '  收錄專輯: ' + album
        
        self.text1.setText(name)
        self.text2.setText(inform)
        # self.UpdateUI()
        
    # def UpdateUI(self):
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())