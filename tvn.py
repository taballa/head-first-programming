#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame.mixer

sounds = pygame.mixer
sounds.init()

def wait_finish(channel):
    while channel.get_busy():
        pass # 用处：让程序等待声音播放结束，再继续运行程序

s = sounds.Sound("sounds/heartbeat.wav")
wait_finish(s.play())

s2 = sounds.Sound("sounds/buzz.wav")
wait_finish(s2.play())

s3 = sounds.Sound("sounds/ohno.wav")
wait_finish(s3.play())

s4 = sounds.Sound("sounds/carhorn.wav")
wait_finish(s4.play())


def function():
    answer = raw_input("Answer is : ")
    number_asked = 0
    number_wrong = 0
    number_correct = 0

    if answer == 1:
        number_correct = number_correct + 1
    elif answer == 2:
        number_wrong = number_wrong + 1
    elif answer == 0:
        print("number_correct: " + number_correct)
        print("number_wrong: " + number_wrong)

