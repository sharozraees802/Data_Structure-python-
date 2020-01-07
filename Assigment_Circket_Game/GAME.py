import random
import time
# import os
from IPython.display import clear_output
from colorama import *



j = 0
player = 0
run = 0
targt = random.randint(20,40)
print(Fore.BLUE)
print("ENTER A ENTER KEY AND START GAME")
print("HOW TO PLAY PRESS ONLY USE")
print("ENTER KEY and number key use")

y = 15
for i in range(0,y):
    print(Fore.RED)
    print("------------------------")
    print("|	       | | |	   |")
    print("|            ( )        |")
    print("|             |         |")
    print("|            / L        |")
    print("|			           |")
    print("|			           |")
    print("|			           |")
    print("|			           |")
    print("|			           |")
    print("|			           |")
    print("|			           |")
    print("------------------------")
    # time.sleep(.05)
    yn = "( )" + "\n\r" + " | " + "\n\r" + "/ \\"
    print(Fore.BLACK)
    print(yn)

    print()
    clear_output()
    # os.system('cls')
    if y > 10:
        y -=1
    else:
        y = 15
        print(Fore.RED)
        print("------------------------")
        print("|	       | | |       |")
        print("|            ( )        |")
        print("|             |         |")
        print("|            / L        |")
        print("|			           |")
        print("|			           |")
        print("|			           |")
        print("|			           |")
        print("|			           |")
        print("|( )                    |")
        print("| |                     |")
        print("|/ L                    |")
        print("------------------------")
        # print(targt)
        score = run
        for j in range(1, 7):
            print("guess  the ball \n")
            BALL = "\n 1:googly \n 2:off spin \n 3:leg spin \n 4:right swing \n 5:left swing \n 6:fast \n 7:medium fast \n 8:leg break \n 9:bouncer \n 10:youker "
            print(Fore.BLUE)
            print(BALL)
            temp = random.randint(1,5)
            print()
            ball = int(input("Enter your ball number "))
            result = 0
            result = (ball - temp)
            clear_output()
            # os.system('cls')
            if result == 0:
                print("FOUR RUN")
                run +=4
            elif result == 1:
                print("SIX RUN")
                run +=6
            elif result == 2:
                print("TWO RUN")
                run +=2
            elif result == 3:
                print("OUT")
                run +=0
                player +=1
            elif result == 5:
                print("WID BALL")
                run +=1
                j -= 1
            else:
                print("DOT BALL")

            print(Fore.RED)
            print("                                                         ------------------------")
            print("                                                         |	       | | |       |")
            print("                                                         |            ( )       |")
            print("                                                         |             |        |")
            print("                                                         |            / L       |")
            print("                                                         |			           |")
            print("                                                         |			           |")
            print("                                                         |			           |")
            print("                                                         |			           |")
            print("                                                         |			           |")
            print("                                                         |( )                   |")
            print("                                                         | |                    |")
            print("                                                         |/ L                   |")
            print("                                                         -----------------------")
            print("Score: "+str(run) + "                           "  " Ball: " + str(j) + "                           "  " Out " + str(player) + "                           " " Targt " + str(targt))

        if score == targt:
            clear_output()
            # os.system('cls')
            print(Fore.CYAN)
            print("LOSE MATCH  " + "  Score: " + str(run) + "                           "  "OUt: " + str(player)+ "                           " " target: " + str(targt))
            break
        elif score > targt:
            clear_output()
            # os.system('cls')
            print(Fore.CYAN)
            print("WIN MATCH  " + "  Score: " + str(run) + "                           "  "OUt: " + str(player)+ "                           " " target: " + str(targt))
            break
        else:
            clear_output()
            # os.system('cls')
            print(Fore.CYAN)
            print("LOSE MATCH  " + "  Score: " + str(run) + "                           "  "OUt: " + str(player)+ "                           " " target: " + str(targt))
            break

