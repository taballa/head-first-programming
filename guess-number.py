print('hello')
guess = 0
while guess != 5:
    _x = input('Guess the number: ')
    guess = int(_x)
    if guess > 5:
        print('Too high')
    else:
        print('Too low')
print('You win')
print('good bye')