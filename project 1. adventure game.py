#python project adventure game

answer = input("would you like to play a game? [yes or no]: ")

print()
if answer == "yes":
    print("good choice, your fate awaits you!")
    print()
       
        
    answer = input("you begin walking down a dark trail in nantucket and come to a intersection, do you go right or left?: [right or left]")
    print()

    if answer == "right":
        print("yout turned right, you have encountered a lttle masked man on a tricycle.")

        answer = input("do you attack the man or trade for his tricycle and flee?: [attack or trade]")
        print()
        if answer == "attack":
            print("you made the wrong choice to attack jigsaw, you have died!!!")

        if answer == "trade":
            print("good choice, home is but a few pedals away!!")

        else:
             print("{} is not a valid input, vios con dios.".format(answer))




    if answer == "left":
        print("you turned left, down the road a bit you spot a light flashing.")

        answer = input("you get to the flashing lights to find a trading post, would you like to go in?: [yes or no]")
        print()

        if answer == "yes":
            print("good choice, tricycles are on sale and home is but a few pedals away!!.")

        elif answer == "no":
            print("oh no, a snowstorm is enroute and home is too far to walk, you have frozen to death!")
        else:
            print("{} is not a valid input, vios con dios.".format(answer))
            

else:
    print("sorry pal your path has ended!!")


