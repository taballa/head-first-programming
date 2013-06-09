#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
print('hello')
guess = 0
secret = randint(1, 10)
while guess != secret:
    _x = input('Guess the number: ')
    guess = int(_x)
    if guess == secret:
        print('You win!')
    else:
        if guess > secret:
            print('Too high')
        else:
            print('Too low')
print('good bye')