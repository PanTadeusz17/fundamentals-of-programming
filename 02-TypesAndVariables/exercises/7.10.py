###
# A program that enables a user to challenge a computer.
# The computer throws dice. Then, the user then tries to guess
# the number from dice by entering a number from 1 to 6
# from the keyboard. If the user has guessed the number
# from the dice, the computer prints True. Otherwise,
# the computer prints False.
#
import random
# COMPUTER TURN
computer = random.randint(1,6)
# YOUR TURN
you = int(input('Roll the dice: '))

if (you < 1) or (you > 6):
    print('Dice has numbers from 1 to 6')

if computer < you:
    print(f'You Won! Computer rolled {computer}')

else:
    print(f'You Lost! Computer rolled {computer}')
