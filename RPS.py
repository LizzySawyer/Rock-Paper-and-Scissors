
     


import random

def init():
        game_over = False
        while  not game_over:
                options =("r", "p", "s")

                computer = random.choice(options)

                gamer = None
                
                print("Welcome to Rock, Paper, Scissors game \n")

                gamer = input("pick an option: R(rock), P(paper), S(scissors)\n").lower()
                
                if gamer == computer:
                        print(computer , gamer )
                        print("it's a tie!")
                        continue

                elif gamer == "r":
                        if computer == "s":
                                print("computer:" , computer )
                                print("player:" , gamer )
                                print("Player wins! Rock breaks Scissors")
                                break
                        elif computer == "p":
                                print("computer:" , computer )
                                print("player:" , gamer )
                                print("Computer wins! Paper covers Rock")
                                break
                
                elif gamer == "p":
                        if computer == "r":
                                print("computer:" , computer )
                                print("player:" , gamer )
                                print("Player wins! Paper covers Rock")
                                break
                        elif computer == "s":
                                print("computer:" , computer )
                                print("player:" , gamer )
                                print("Computer wins! Scissors cuts Paper")
                                break
                
                elif gamer == "s":
                        if computer == "r":
                                print("computer:" , computer )
                                print("player:" , gamer )
                                print("Computer wins! Rock breaks Scissors")
                                break
                        elif computer == "p":
                                print("computer:" , computer )
                                print("player:" , gamer )
                                print("Player wins! Scissors cuts Paper")
                                break
                else:
                        print("Invalid input")
                
def word():
        print("invalid option!Try again")
                        

init()



