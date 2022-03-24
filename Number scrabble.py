# This code is for a game called number scrabble where two players take turns to choose numbers between 1 and 9 three
# times with a goal of having a sum of 15. No numbers can be repeated or chosen twice and the first player to reach  15
# wins

# initializing the sums of both players by 0 and creating the list of numbers
Sum_1 = 0
Sum_2 = 0
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# printing the greeting and giving the option for displaying the rules

print("Hello and welcome to Number Scrabble!!")
instructions = input("would you like to take a look at the rules?  (yes/no)\n").lower()

# checking that the input was correct and giving an error if not

while instructions != 'yes' and instructions != 'no':
    print("ERROR!\nInput is invalid please enter \"yes\" or \"no\"")
    instructions = input()

# if condition for displaying the rules

if instructions == 'yes':

    print("This is how the game works:\n\n" 
          "Number scrabble is played between 2 players.\nThe players take turns choosing a number from "
          "a list of numbers between 1 and 9"
          "\nOnce a number has been picked, it cannot be picked "
          "again.\nThe first player that picks three numbers that add up to 15 wins the game.\n\nLets begin the game!!")

elif instructions == 'no':
    print("Ok, Let's start the game !!!")

# input of the players names

player_1 = input("Player 1 please enter your name: ")
player_2 = input("Player 2 please enter your name: ")

# loop for a 3 time entry
for i in range(3):

    # printing the game state and asking player 1 to enter a number

    print(*lst)
    print(player_1, 'please choose a number from the list : ')
    num_1 = int(input())

    # While loop to prevent the player from entering out of range or the same number twice

    while num_1 not in lst:
        print('ERROR! \nThis number is not present in the list \nPlease choose a number from the list  ')
        num_1 = int(input())

    # update the sum and the game state and print on screen

    Sum_1 += num_1
    i = lst.index(num_1)
    lst = lst[:i] + ['X'] + lst[i + 1:]
    print(*lst)

    # asking player 2 to enter a number

    print(player_2, 'please enter a number from the list : ')
    num_2 = int(input())

    # While loop to prevent the player from entering out of range or the same number twice

    while num_2 not in lst:
        print('ERROR! \nThis number is not present in the list \nPlease choose a number from the list  ')
        num_2 = int(input())

    # update the sum and the game state and print on screen

    Sum_2 += num_2
    i = lst.index(num_2)
    lst = lst[:i] + ['X'] + lst[i + 1:]

# determining the winner

if Sum_1 == 15:
    print(player_1, 'is the winner!!!!!!\nGood luck next time', player_2, ':\\')
elif Sum_2 == 15:
    print(player_2, 'is the winner!!!!!!\nGood luck next time', player_1, ':\\')
else:
    print('It\'s a Draw!')