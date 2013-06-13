#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pygame.mixer

sounds = pygame.mixer
sounds.init()

def wait_finish(channel):
    while channel.get_busy():
        pass # 用处：让程序等待声音播放结束，再继续运行程序

# s = sounds.Sound("sounds/heartbeat.wav")
# wait_finish(s.play())

# s2 = sounds.Sound("sounds/buzz.wav")
# wait_finish(s2.play())

# s3 = sounds.Sound("sounds/ohno.wav")
# wait_finish(s3.play())

# s4 = sounds.Sound("sounds/carhorn.wav")
# wait_finish(s4.play())

correct_s = sounds.Sound("sounds/correct.wav")
wrong_s = sounds.Sound("sounds/wrong.wav")

prompt = "Press 1 for Correct, 2 for Wrong, or 0 to Quit: "
choice = raw_input(prompt)

number_asked = 0
number_wrong = 0
number_correct = 0

while choice != 0:
    if choice == 1:
        number_asked = number_asked + 1
        number_correct = number_correct + 1
        wait_finish(correct_s.play())
    elif choice == 2:
        number_asked = number_asked + 1
        number_wrong = number_wrong + 1
        wait_finish(wrong_s.play())
    choice = input(prompt)

print("You asked " + str(number_asked) + " questions.")
print(str(number_correct) + " were correctly answered.")
print(str(number_wrong) + " were answered incorrectly.")

