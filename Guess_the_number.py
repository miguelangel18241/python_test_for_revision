secret_number = 6
guess_count = 0
guess_limit = 3
interested = True
name = input('What is your name? ')
print (f'Hi {name}, thanks for participating.')
inv = ""

while True:
    inv = input('Would you like to play a fun game? Yes or no? ').lower()
    if inv == 'si':
        print(f'{name}, welcome to the game.')
    elif inv == 'no':
        print('See you fucker :P ')
    break
while guess_count < guess_limit:
    if guess_count == 0:
        print(f'You have three tries to guess a number from one to ten, let us begin!!!')
    guess = int(input('Guess a number from 1 to 10: '))
    if guess == secret_number:
        print(f'{name}, you have won, congratulations!!!')
        break
    else:
        guess_count += 1
else:
    print(str(name) + ' thanks for participating, maybe another time.')
print('''
Game over!
''')
