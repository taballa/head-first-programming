print('hello')
_x = input('Guess the number: ')
guess = int(_x)
while guess != 5:
    if guess > 5:
        print('Too high')
    else:
        print('Too low')
    guess = int(input('Guess the number: '))
print('You win')
print('good bye')