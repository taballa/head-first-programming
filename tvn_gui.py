#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter
import pygame.mixer

sounds = pygame.mixer
sounds.init()

correct_s = sounds.Sound("sounds/correct.wav")
wrong_s = sounds.Sound("sounds/wrong.wav")

number_correct = 0
number_wrong = 0

app = Tkinter.Tk()
app.title("Your tkinter application")

num_good = Tkinter.IntVar() # 使用 IntVar() 前必须先初始化任意一个 Tk() !
num_good.set(0)
num_bad = Tkinter.IntVar()
num_bad.set(0)

def button_click():
    print ("I've just been clicked!")

def play_correct():
    global number_correct
    number_correct = number_correct + 1
    num_good.set(num_good.get() + 1)
    correct_s.play()

def play_wrong():
    global number_wrong
    number_wrong = number_wrong + 1
    num_bad.set(num_bad.get() + 1)
    wrong_s.play()

b1 = Tkinter.Button(app, text = "Click me!", width = 10, command = button_click)
b1.pack(padx =10 , pady = 10)
# b2 = Tkinter.Button(app, text = "Right", width = 10)
# # b2.pack(side = 'right', padx =10 , pady = 10)
# b3 = Tkinter.Button(app, text = "Top", width = 10)
# # b3.pack(side = 'top', padx =10 , pady = 10)
# b4 = Tkinter.Button(app, text = "Left", width = 10)
# # b4.pack(side = 'left', padx =10 , pady = 10)

l1 = Tkinter.Label(app, text = "When you are ready, click on the botton.", height = 3)
l1.pack()

l2 = Tkinter.Label(app, textvariable = num_good)
l2.pack(side = 'left')

l3 = Tkinter.Label(app, textvariable = num_bad)
l3.pack(side = 'right')

correct_b = Tkinter.Button(app, text = "Correct", width = 10, command = play_correct)
wrong_b = Tkinter.Button(app, text = "Wrong", width = 10, command = play_wrong)

correct_b.pack(side = "left", padx = 10, pady = 10)
wrong_b.pack(side = "right", padx = 10, pady =10)

app.geometry('450x200+200+100')
app.mainloop()

print(str(number_correct) + " were correctly answered")
print(str(number_wrong) + " were answered incorrectly")
