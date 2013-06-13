#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sound_panel import *
from Tkinter import *
import pygame.mixer
import os


mixer = pygame.mixer
mixer.init()

app = Tk()
app.title("Head First Mix")

dirList = os.listdir('.') # 获取当前目录下所有文件
for fname in dirList:
    if fname.endswith('.wav'):
        panel = SoundPanel(app, mixer, fname)
        panel.pack()

# panel = SoundPanel(app, mixer, "50459_M_RED_Nephlimizer.wav")
# panel.pack()
# panel = SoundPanel(app, mixer, "49119_M_RED_HardBouncer.wav")
# panel.pack()

create_gui(app, mixer, "50459_M_RED_Nephlimizer.wav")
create_gui(app, mixer, "49119_M_RED_HardBouncer.wav")

app.mainloop()