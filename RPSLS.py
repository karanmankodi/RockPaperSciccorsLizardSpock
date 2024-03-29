# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
import random

# helper functions

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if (name == 'rock'):
        number = 0
        return number
    elif (name == 'Spock'):
        number = 1
        return number
    elif (name == 'paper'):
        number = 2
        return number
    elif (name == 'lizard'):
        number = 3
        return number
    elif (name == 'scissors'):
        number = 4
        return number
    else:
        print "Enter correct name"
        

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if (number == 0):
        name = "rock"
        return name
    elif (number == 1):
        name = "spock"
        return name
    elif (number == 2):
        name = "paper"
        return name
    elif (number == 3):
        name = "lizard"
        return name
    elif (number == 4):
        name = "sciccors"
        return name
    else:
        print "enter correct number"
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    
    # print a blank line to separate consecutive games
    print "\n"
    
    # print out the message for the player's choice
    print ("Player chooses "+player_choice+ "")
    
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 4)
        
    # convert comp_number to comp_choice using the function number_to_name()
    comp_name = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print ("Computer chooses "+comp_name+ "")
    
    # compute difference of comp_number and player_number modulo five
    difference = comp_number - (player_number)
    mod = difference % 5

    # use if/elif/else to determine winner, print winner message
    if (mod == 0):
        print "Player and computer tie!"
    elif (mod == 1):
        print "Computer wins!"
    elif (mod == 2):
        print "Computer wins!"
    elif(mod == 3):
        print "Player wins!"
    elif(mod == 4):
        print "Player wins!"
    else:
        print "Error"
    
# test your code - LEAVE THESE CALLS IN YOUR SUBMITTED CODE
user_input = raw_input()
rpsls(user_input)


# always remember to check your completed program against the grading rubric


