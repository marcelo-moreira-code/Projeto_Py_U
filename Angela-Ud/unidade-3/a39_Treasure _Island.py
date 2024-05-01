print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")
choice = input("You're at a cross road. Where do you want to go? Type 'left' or 'right': ")
print(choice)
#choice_left
if choice == "left":
    choice_wait = input("You come to a lake. There is an island in the middle of the lake.\n Type 'wait' to wait for a boat.\n Or type 'swim' to swim across. ")
    if choice_wait == "wait":
        color = input("You arrive at the island unharmed.\nThere is a house with 3 doors.\nOne red, one yellow and one blue.\nWhich colour dou you choose?")
        if color == "blue" or "red":
            print("You enter a room of beasts. Game Over!")
        else:
            print("You Win!")    
    else:
        print("Swing a across!")    




#choice_right 
if choice == "right":
    print("You fail!")


