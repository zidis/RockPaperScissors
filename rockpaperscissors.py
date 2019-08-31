import random

def playerwon():
    print('You won!')

def playerlost():
    print('You lost!')

# User input
x = str(input('Pick rock paper or scissors: '))

# Computer pick
choices = ['rock', 'paper', 'scissors']
y = random.choice(choices)
print('The computer picked ' + y + '.')

# Game tie
if x == y:
    print('You tied!')

# Other cases
if x == ('rock'):
    if y == ('paper'):
        playerlost()
    if y == ('scissors'):
        playerwon()

elif x == ('paper'):
    if y == ('scissors'):
        playerlost()
    if y == ('rock'):
        playerwon()

elif x == ('scissors'):
    if y == ('rock'):
        playerlost()
    if y == ('paper'):
        playerwon()
else:
    print('Not a valid choice, please try again.')
