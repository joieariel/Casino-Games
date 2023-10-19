""" Joie Whitmon

Objective: In this project, you'll build a Roulette simulation. Players will choose a type of bet and sometimes a specific number, depending on the bet type. The program will then spin a virtual Roulette wheel and land on a number between 1 and 36. Based on the player's bet and the wheel's outcome, the program will determine if the player wins and calculate their earnings. Your goal is to ensure that the game runs smoothly and the payouts are accurate.

Roulette Basics: 
• Roulette Wheel: Contains numbers 1 through 36. In our simulation, we're excluding any zeroes commonly found on traditional wheels. 
• Betting: Players predict where a ball will land after the wheel stops spinning. They place bets based on these predictions.
• Spinning: The wheel spins, a ball is introduced, and as the wheel slows, the ball will settle into one of the numbered pockets, giving the winning number.


Algorithm:

1)	Import the random module (import random)
2)	Initialize the variables. Each bet is $5 (betcost = 5) The players must start with a balance so  (balance = (whatever value the balance will be)) eg: (balance = 200)
Welcome Message
1)	Print welcome message and game rules (every bet costs $5)
Main Game Loop
2)	Enter a loop for that continues the game until the player wants to stop.
3)	Print the numbered betting option. (Betting Options: 1. Straight Up: (description here.) 2. Split: (description here), and so on…., 7. Quit.)
4)	Ask the user for their betting option choice (1-7). (betting option = input(Enter your betting option choice (1-7): “) 
End of Game
5)	If the user enters 7 end the game. (if bettingoption == “7”: break)
6)	Print a thank you for playing message.
If player enters something other than 1-7
7)	If the choice is not (1-7) ask the user to enter a number between 1-7. Allow user to try again. (continue).
Deduct bet cost
8)	Subtract the cost of the bet from the balance (balance = balance – betcost) or (balance -= bet cost)
9)	Spin the virtual wheel to get a random number between 1 and 36) (wheelresult = random.randint(1,36)
If player chooses 1 or Straight Up option
10)	If the player enters 1 (Straight Up, which accepts a single number). (if bettingoption == 1: ….. ) 
11)	Ask the user to enter a number between 1-36.
12)	If the number the user inputs is equal to the randomized wheel result, they win and 35 should be multiplied to their bet cost. Print the rolled number and a congratulations message saying they win.
Examples of 11-13: 
if bettingpointoption == 1:
	winnings = betcost * 35
	print (“The rolled number is”, wheelresult,”.”)
	print(“Congratulations! You win $,”winnings,”(35 to 1 payout)”,)
13)	Else, print the result (The rolled number is…)
14)	Print a sorry message (Sorry, you lose this round. Better luck next time!)
If the player chooses 2 or Split 
15)	Ask the player to enter a number from 1-36.
16)	If the chosen number is equal to the randomized wheel result or one less/one more than the result, calculate and display the winnings (17 times the bet cost)
17)	If the chosen number is not equal or adjacent to the number, print a statement saying that the player has lost this round. 
If the player chooses 3 or Street
18)	Ask the player to enter a number 1-36.
19)	If the chosen number is equal to or the next two numbers in a sequence. ( one more, or two more than the randomized wheel result). Calculate and display the winnings (11 times the bet cost)
20)	If the chosen number is not equal to, one more than, or two more than the wheel result, print a message saying the player lost this round. 
If the player chooses 4 or Top
21)	Spin the virtual wheel (printed message)
22)	If the randomized number from the wheel spin is any number 1-18 (including 1 and 18), calculate and print the winnings. (even money) (The winnings will be 2 times the bet cost)
23)	Else, print the result and inform the player that they lost. 
If the player chooses 5 or Bottom
24)	Spin the virtual wheel
25)	If the randomized number from the wheel spin is any number 19-36 (19 and 36 included). Calculate and print the winnings. (2 times the bet cost)
26)	Else, print the result and inform the player that they have lost 
If the player chooses 6 or Even/Odd
27)	Ask the user to enter either “Even” or “Odd”
28)	If the user enters even check to see if the randomized wheel result is even
29)	If the number is even print the result, and winnings (2 times the bet cost)
30)	Vice versa with Odd
31)	If the user’s input does not match the randomized wheel result, print a message telling the player that they’ve lost the this round. 
Update balance
32)	Subtract 5 (bet cost) from the players balance for every bet the player makes. 
33)	If the player wins, add the winnings to their balance. 
Check player’s balance
34)	If the player’s balance is less than the best cost, exit the game loop and print a goodbye or thank you for playing message. (also do this if option 7 is chosen)
"""
import random

#every bet costs $5
betcost = 5
#initial balance is $200
balance = 200

#greeting
print("       Welcome to Joie's Roulette Table!")
print("                Game Rules:")
print("             Every bet costs $5")

#create the menu
menu = """Betting Options: 
1) Straight Up (Single Number Game):
  - Single number selection
  - If the ball lands on your number, you win 35 times your bet. (Potential payout is 35 to 1)
2) Split (Double Number Game):
  - Single number selection
  - If the ball lands on your number or one of the adjacent numbers (above or below), you win 17 times your bet. (Potential payout is 17 to 1)
3) Street (Three Number Game):
  - Single number selection
  - If the ball lands on your number or the next two numbers in a sequence, you will 11 times your bet. (Potential payout is 11 to 1.)
4) Top (Numbers 1-18)
  - This is a bet that will land on any number 1 to 18, inclusive.
  - If you're correct and the ball lands on a number 1-18, you receive a fixed payout of $10. 
5) Bottom (Numbers 19-36)
  - This is a bet that the ball will land on any number 19 to 36, inclusive.
  - If you're correct, you recieve a fixed payout of $10.
6) Even/Odd
  - This is a bet that the ball will land on either an even or odd number 
  - If you are correct, you receive a fixed payout of $10. 
  
7) Quit
"""

#main game loop
while True:
    print(menu)

    #user decides what they want to play
    betting_option = int(input("Enter the corresponding number (1-7) of the betting option of your choice: "))

    #if player wants to stop playing/quit
    if betting_option == 7:
        print("  ")
        print("Thanks for playing at Joie's Roulette Table!")
        break

    #if user inputs an invalid number
    if betting_option not in range(1, 8):
        print(" ")
        print("Uh oh! Invalid input. Please enter a number between 1 and 7. ")
        print("  ")

    #deduct bet cost
    balance -= betcost

    #spin the wheel to get a random number between 1-36
    wheelresult = random.randint(1, 36)

    #user choice variable defined here
    userchoice = 0
###############################################################################
    #if player chooses 1 or STRAIGHT UP
    if betting_option == 1:
        #user chooses number
        userchoice = int(input("Which number would you like for the Straight Up bet? (1-36): "))

        #if user enters number not in the range
        if userchoice not in range(1, 37):
            print(" ")
            print("---------------------------------------------")
            print("UH OH! Invalid input. Try again, please enter a number between 1 and 36. ")
            print("---------------------------------------------")
            print(" ")
            continue

        #spinning wheel
        print("   ")
        print("......................................")
        print("..........Spinning the Wheel..........")
        print("......................................")
        #if the player wins/if chosen number is equal to wheel result
        if userchoice == wheelresult:
            winnings = betcost * 35
            print("  ")
            print("The rolled number is", wheelresult)
            print("Congratulations! You win $", winnings, "(35 to 1 payout)")
            print(" ")
        #if the player loses/if the wheel result and chosen number are not equal
        else:
            print("  ")
            print("The rolled number is", wheelresult)
            print("Sorry, you lose this round. Better luck next time!")
            print("   ")
################################################################################
    #if the player chooses 2 or SPLIT
    elif betting_option == 2:
        #user chooses number
        userchoice = int(input("Which number would you like to select for the Split bet? (1-36): "))
        # if user enters number not in the range
        if userchoice not in range(1, 37):
            print(" ")
            print("---------------------------------------------")
            print("UH OH! Invalid input. Try again, please enter a number between 1 and 36. ")
            print("---------------------------------------------")
            print(" ")
            continue
        #spinning the wheel
        print("   ")
        print("......................................")
        print("..........Spinning the Wheel..........")
        print("......................................")
        #if the player wins/if chosen number is equal to wheel result or the next two numbers in a sequence
        if userchoice == wheelresult or userchoice == wheelresult + 1 or userchoice == wheelresult - 1:
            winnings = betcost * 17
            print("  ")
            print("The rolled number is", wheelresult)
            print("Congratulations! You win $", winnings, "(17 to 1 payout)")
            print(" ")
        
        #if the player loses/if the wheel result and chosen number are not equal
        else:
            print("   ")
            print("The rolled number is", wheelresult)
            print("Sorry, you lose this round. Better luck next time!")
            print("  ")
###############################################################################
    #if the player chooses 3 or STREET
    elif betting_option == 3:
        #user chooses number
        userchoice = int(input("Which number would you like for the Street bet? (1-36): "))
        #if user enters number not in the range
        if userchoice not in range(1, 37):
            print(" ")
            print("---------------------------------------------")
            print("UH OH! Invalid input. Try again, please enter a number between 1 and 36. ")
            print("---------------------------------------------")
            print(" ")
            continue
        #spinning the wheel
        print("   ")
        print("......................................")
        print("..........Spinning the Wheel..........")
        print("......................................")
        #if the player wins/if chosen number is equal to wheel result or the next two numbers in a sequence
        if userchoice == wheelresult or userchoice == wheelresult + 1 or userchoice == wheelresult + 2:
            winnings = betcost * 11
            print("  ")
            print("The rolled number is", wheelresult)
            print("Congratulations! You win $", winnings, "(11 to 1 payout)")
            print(" ")
        #if the player loses/if the wheel result and chosen number are not equal
        else:
            print("   ")
            print("The rolled number is", wheelresult)
            print("Sorry, you lose this round. Better luck next time!")
            print("  ")
###############################################################################
    #if the player chooses 4 or TOP
    elif betting_option == 4:
        print("   ")
        print("......................................")
        print("..........Spinning the Wheel..........")
        print("......................................")
        #if the player wins/if wheelresult is between 1 and 18 inclusive
        if wheelresult >= 1 and wheelresult <= 18:
            winnings = betcost * 2
            print("  ")
            print("The rolled number is", wheelresult)
            print("Congratulations! You win $",winnings, "(even money - $10)")
            print(" ")
        #if the player loses/if the wheel result is not between 1-18, inclusive
        else:
            print("   ")
            print("The rolled number is", wheelresult)
            print("Sorry, you lose this round. Better luck next time!")
            print("  ")
###############################################################################
    #if the player chooses 5 or BOTTOM
    elif betting_option == 5:
        print("   ")
        print("......................................")
        print("..........Spinning the Wheel..........")
        print("......................................")
        #if the player wins/if wheelresult is between 19-36, inclusive
        if wheelresult >= 19 and wheelresult <= 36:
            winnings = betcost * 2
            print("  ")
            print("The rolled number is", wheelresult)
            print("Congratulations! You win $",winnings, "(even money - $10)")
            print(" ")
        #if the player loses/if the wheel result is not between 1-18, inclusive
        else:
            print("   ")
            print("The rolled number is", wheelresult)
            print("Sorry, you lose this round. Better luck next time!")
            print("  ")

###############################################################################
    #if the player chooses 6 or EVEN/ODD
    elif betting_option == 6:
        #user chooses either even or odd
        evenodd = input("Your preference for Even/Odd (Enter 'even' or 'odd'): ")

        # if user enters something other than even or odd
        if evenodd != 'even' and evenodd != 'odd':
            print(" ")
            print("---------------------------------------------")
            print("UH OH! Invalid input. Try again, please enter 'even' or 'odd.' (case sensitve)")
            print("---------------------------------------------")
            print(" ")
            continue

        #spinning the wheel
        print("   ")
        print("......................................")
        print("..........Spinning the Wheel..........")
        print("......................................")
        #if the player wins/if chosen value is equal to wheelresult
        if evenodd == 'even' and wheelresult % 2 == 0 or evenodd == 'odd' and wheelresult % 2 != 0:
            winnings = betcost * 2
            print("  ")
            print("The rolled number is", wheelresult)
            print("Congratulations! You win $",winnings, "(even money - $10)")
            print(" ")
        #if the player loses/if the wheel result and userchoice are not the same
        else:
            print("   ")
            print("The rolled number is", wheelresult)
            print("Sorry, you lose this round. Better luck next time!")
            print("  ")   
            
