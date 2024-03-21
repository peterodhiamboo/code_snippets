# This is a number guesing game within a specified range:
# game can be modified by the user inputting the range of number that they desire

def guess_game(last_number_of_range):
    #Thhhis is used to collect the user input
    number = int(input('Enter the last number of range: \n range starts from 1 - ? '))

    print(f'You selected : {number}')

    while(number != 1):
        number = int(input('try again: '))
    print('You guessed right :')


guess_game(3)