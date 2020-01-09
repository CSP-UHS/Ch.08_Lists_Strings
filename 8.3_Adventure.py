'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
room_list=[];done=False;current_room=1;wait=False;var=0;Fkey=0;Quarters=0;LS=0;Ukey=0
#Outside
room=["You exit to the outside porch. You take a deep breath and walk home.",1,None,None,None]
room_list.append(room)

#First Floor
room=["The tiger rug is staring at you, there's a wardrobe and a small bench in the corner.",4,6,0,2]
room_list.append(room)

room=["You enter the living room. A large couch dominates the center of the room and the T.V. in the corner has nothing"
      " but static playing.\nAnother large wardrobe is in the corner in this room.",3,1,None,None]
room_list.append(room)

room=["Walking into the laundry room you notice that both the dryer is running. A basket of clothes sits "
      "in the corner filled to the brim.",None,4,2,None]
room_list.append(room)

room=["Entering into the large room there is a Grand Staircase that wraps itself along the wall, made completely of "
      "carved marble with a red carpet draped down the center of the stairs",7,5,1,3]
room_list.append(room)

room=["In the kitchen there are several dishes filling the sink. The oven was left on and there appears "
      "to still be something left in it.",None,None,6,4]
room_list.append(room)

room=["When you enter into this room you are startled by a loud squeak. You look down and you have stepped onto a "
      "child's toy. The rest of the room also seems to be covered\nwith children's toys and there is a "
      "chest in the corner and a gumball machine",5,None,None,1]
room_list.append(room)

#2nd Floor
room=["You walk up the stairs and enter a hallway. Ominous paintings line the walls and it seems like their eyes follow"
      " you as you walk past them.",10,None,4,8]
room_list.append(room)

room=["You enter the bathroom, the tub is full of hot water and the sink is running.",9,7,None,None]
room_list.append(room)

room=["You enter the room and there's a bed in the corner and a dresser with a candle stand on top.",None,10,8,None]
room_list.append(room)

room=["In the master bedroom there's a large four poster bed with the drapes drawn, you can see a figure laying in the "
      "bed. A dress is hanging from the bed and a dresser in the corner \nhas all it's drawers pulled "
      "revealing clothes strewn about.",None,None,7,9]
room_list.append(room)


print("Welcome to Escape the House. In this game you will travel through house and collect items in the hopes of "
      "escaping the house. When you are asked for a direction to move answer \nN,E,S, or W. If you are asked a yes "
      "or no question you can answer with yes,no,y or n. Let's get started.")
print()
print("You awaken on the floor, there's a tiger head in front of you but it's just a rug. There's a wardrobe in "
      "the corner and a small bench near the door.")

while done==False:
    if current_room == 0:
        print(room_list[current_room][0])
        print("Congratulations you have escaped")
    if current_room == 1:
        print()
        print(room_list[current_room][0])
        var = current_room
        while wait == False:
            print()
            decision = input("Would you like to inspect the wardrobe?")
            if decision.lower() == "yes" or decision.lower() == "y":
                print()
                print("It's empty with dust")
                break
            elif decision.lower() == "no" or decision.lower() == "n":
                print()
                print("Okay")
                break
            else:
                print("That's not an option.")
        wait = False
        while wait == False:
            print()
            direction = input("Which direction would you like to go?")
            if direction.lower() == "n" or direction.lower() == "north":
                if room_list[var][1] == None:
                    print("There's no door that way.")
                else:
                    current_room = room_list[var][1]
                    break
            if direction.lower() == "e" or direction.lower() == "east":
                if room_list[var][2] == None:
                    print("There's no door that way.")
                else:
                    current_room = room_list[var][2]
                    break
            if direction.lower() == "s" or direction.lower() == "south":
                if room_list[var][3] == None:
                    print("There's no door that way.")
                else:
                    if Fkey==1:
                        print("Congratulations, you've won")
                        done=True
                        break
                    else:
                        print("It's locked, it seems you need a key.")
            if direction.lower() == "w" or direction.lower() == "west":
                if room_list[var][4] == None:
                    print("There's no door that way.")
                else:
                    current_room = room_list[var][4]
                    break
    if current_room == 2:
        print()
        print(room_list[current_room][0])
        var = current_room
        while wait == False:
            print()
            decision = input("Would you like to inspect the wardrobe?")
            if decision.lower() == "yes" or decision.lower() == "y":
                print()
                print("You find some laundry soap and pick it up")
                LS+=1
                break
            elif decision.lower() == "no" or decision.lower() == "n":
                print()
                print("Okay")
                break
            else:
                print("That's not an option.")
        while wait == False:
            print()
            decision = input("Would you like to inspect the couch?")
            if decision.lower() == "yes" or decision.lower() == "y":
                print()
                print("You find 4 quarters and pick them up")
                Quarters+=4
                break
            elif decision.lower() == "no" or decision.lower() == "n":
                print()
                print("Okay")
                break
            else:
                print("That's not an option.")
        wait = False
        while wait == False:
            print()
            direction = input("Which direction would you like to go?")
            if direction.lower() == "n" or direction.lower() == "north":
                if room_list[var][1] == None:
                    print("There's no door that way.")
                else:
                    current_room = room_list[var][1]
                    break
            if direction.lower() == "e" or direction.lower() == "east":
                if room_list[var][2] == None:
                    print("There's no door that way.")
                else:
                    current_room = room_list[var][2]
                    break
            if direction.lower() == "s" or direction.lower() == "south":
                if room_list[var][3] == None:
                    print("There's no door that way.")
                else:
                    current_room = room_list[var][3]
                    break
            if direction.lower() == "w" or direction.lower() == "west":
                if room_list[var][4] == None:
                    print("There's no door that way.")
                else:
                    current_room = room_list[var][4]
                    break
    if current_room == 3:
        print()
        print(room_list[current_room][0])
        var = current_room
        while wait == False:
            print()
            decision = input("Would you like start the washer?")
            if decision.lower() == "yes" or decision.lower() == "y":
                print()
                if LS == 1:
                    print("While dumping the clothes you find a key and pick it up")
                    Ukey+=1
                    break
                else:
                    print("You need some laundry soap first.")
                    break
            elif decision.lower() == "no" or decision.lower() == "n":
                print()
                print("Okay")
                break
            else:
                print("That's not an option.")
            wait = False
            break
        while wait == False:
            print()
            direction = input("Which direction would you like to go?")
            if direction.lower() == "n" or direction.lower() == "north":
                if room_list[var][1] == None:
                    print("There's no door that way.")
                else:
                    current_room = room_list[var][1]
                    break
            if direction.lower() == "e" or direction.lower() == "east":
                if room_list[var][2] == None:
                    print("There's no door that way.")
                else:
                    current_room = room_list[var][2]
                    break
            if direction.lower() == "s" or direction.lower() == "south":
                if room_list[var][3] == None:
                    print("There's no door that way.")
                else:
                    current_room = room_list[var][3]
                    break
            if direction.lower() == "w" or direction.lower() == "west":
                if room_list[var][4] == None:
                    print("There's no door that way.")
                else:
                    current_room = room_list[var][4]
                    break
    if current_room == 4:
        print()
        print(room_list[current_room][0])
        var = current_room
        while wait == False:
            print()
            direction = input("Which direction would you like to go?")
            if direction.lower() == "n" or direction.lower() == "north":
                if room_list[var][1] == None:
                    print("There's no door that way.")
                else:
                    current_room = room_list[var][1]
                    break
            if direction.lower() == "e" or direction.lower() == "east":
                if room_list[var][2] == None:
                    print("There's no door that way.")
                else:
                    current_room = room_list[var][2]
                    break
            if direction.lower() == "s" or direction.lower() == "south":
                if room_list[var][3] == None:
                    print("There's no door that way.")
                else:
                    current_room = room_list[var][3]
                    break
            if direction.lower() == "w" or direction.lower() == "west":
                if room_list[var][4] == None:
                    print("There's no door that way.")
                else:
                    current_room = room_list[var][4]
                    break
    if current_room == 5:
        print()
        print(room_list[current_room][0])
        var = current_room
        while wait == False:
            print()
            decision = input("Would you like to inspect the oven?")
            if decision.lower() == "yes" or decision.lower() == "y":
                print()
                print("The heat hits your face. There is a lasagna in the oven. It's too hot to touch.")
                break
            elif decision.lower() == "no" or decision.lower() == "n":
                print()
                print("Okay")
                break
            else:
                print("That's not an option.")
        wait = False
        while wait == False:
            print()
            direction = input("Which direction would you like to go?")
            if direction.lower() == "n" or direction.lower() == "north":
                if room_list[var][1] == None:
                    print("There's no door that way.")
                else:
                    current_room = room_list[var][1]
                    break
            if direction.lower() == "e" or direction.lower() == "east":
                if room_list[var][2] == None:
                    print("There's no door that way.")
                else:
                    current_room = room_list[var][2]
                    break
            if direction.lower() == "s" or direction.lower() == "south":
                if room_list[var][3] == None:
                    print("There's no door that way.")
            if direction.lower() == "w" or direction.lower() == "west":
                if room_list[var][4] == None:
                    print("There's no door that way.")
                else:
                    current_room = room_list[var][4]
                    break
    if current_room == 6:
        print()
        print(room_list[current_room][0])
        var = current_room
        while wait == False:
            print()
            decision = input("Would you use the gumball machine?")
            if decision.lower() == "yes" or decision.lower() == "y":
                print()
                if Quarters==4:
                    print("The mechanism turns and spits out a gumball.")
                    print("You begin chewing on it. It's grape flavored.")
                    break
                else:
                    print("Seems you need some quarters first.")
                    break
            elif decision.lower() == "no" or decision.lower() == "n":
                print()
                print("Okay")
                break
            else:
                print("That's not an option.")
        wait = False
        while wait == False:
            print()
            direction = input("Which direction would you like to go?")
            if direction.lower() == "n" or direction.lower() == "north":
                if room_list[var][1] == None:
                    print("There's no door that way.")
                else:
                    current_room = room_list[var][1]
                    break
            if direction.lower() == "e" or direction.lower() == "east":
                if room_list[var][2] == None:
                    print("There's no door that way.")
                else:
                    current_room = room_list[var][2]
                    break
            if direction.lower() == "s" or direction.lower() == "south":
                if room_list[var][3] == None:
                    print("There's no door that way.")
            if direction.lower() == "w" or direction.lower() == "west":
                if room_list[var][4] == None:
                    print("There's no door that way.")
                else:
                    current_room = room_list[var][4]
                    break
    if current_room == 7:
        print()
        print(room_list[current_room][0])
        var = current_room
        while wait == False:
            print()
            direction = input("Which direction would you like to go?")
            if direction.lower() == "n" or direction.lower() == "north":
                if room_list[var][1] == None:
                    print("There's no door that way.")
                else:
                    if Ukey==1:
                        current_room = room_list[var][1]
                        break
                    else:
                        print("It's locked")
            if direction.lower() == "e" or direction.lower() == "east":
                if room_list[var][2] == None:
                    print("There's no door that way.")
                else:
                    current_room = room_list[var][2]
                    break
            if direction.lower() == "s" or direction.lower() == "south":
                if room_list[var][3] == None:
                    print("There's no door that way.")
                else:
                    current_room = room_list[var][3]
                    break
            if direction.lower() == "w" or direction.lower() == "west":
                if room_list[var][4] == None:
                    print("There's no door that way.")
                else:
                    current_room = room_list[var][4]
                    break
    if current_room == 8:
        print()
        print(room_list[current_room][0])
        var = current_room
        while wait == False:
            print()
            decision = input("Would you like to turn off the sink?")
            if decision.lower() == "yes" or decision.lower() == "y":
                print()
                print("You attempt to turn off the sink but the handles appear to be stuck.")
                break
            elif decision.lower() == "no" or decision.lower() == "n":
                print()
                print("Okay")
                break
            else:
                print("That's not an option.")
        while wait == False:
            print()
            decision = input("Would you like to inspect the bathtub?")
            if decision.lower() == "yes" or decision.lower() == "y":
                print()
                print("While walking over you slip on the water from the sink and hit your head "
                      "on the edge of the tub. Unfortunately it kills you.")
                done=True
                wait=True
                break
            elif decision.lower() == "no" or decision.lower() == "n":
                print()
                print("Okay")
                break
            else:
                print("That's not an option.")
        while wait == False:
            print()
            direction = input("Which direction would you like to go?")
            if direction.lower() == "n" or direction.lower() == "north":
                if room_list[var][1] == None:
                    print("There's no door that way.")
                else:
                    current_room = room_list[var][1]
                    break

            if direction.lower() == "e" or direction.lower() == "east":
                if room_list[var][2] == None:
                    print("There's no door that way.")
                else:
                    current_room = room_list[var][2]
                    break
            if direction.lower() == "s" or direction.lower() == "south":
                if room_list[var][3] == None:
                    print("There's no door that way.")
                else:
                    current_room = room_list[var][3]
                    break
            if direction.lower() == "w" or direction.lower() == "west":
                if room_list[var][4] == None:
                    print("There's no door that way.")
                else:
                    current_room = room_list[var][4]
                    break
    if current_room == 9:
        print()
        print(room_list[current_room][0])
        var = current_room
        while wait == False:
            print()
            decision = input("Would you like to inspect the drawer?")
            if decision.lower() == "yes" or decision.lower() == "y":
                print()
                print("You pull on the drawers and one finally opens to reveal absolutely nothing.")
                break
            elif decision.lower() == "no" or decision.lower() == "n":
                print()
                print("Okay")
                break
            else:
                print("That's not an option.")
        while wait == False:
            print()
            decision = input("Would you like to inspect the bed?")
            if decision.lower() == "yes" or decision.lower() == "y":
                print()
                print("You lie down and immediately fall asleep. You wake up after a couple hours, nothing seems to be"
                      "off except your back hurts.")
                done = True
                wait = True
                break
            elif decision.lower() == "no" or decision.lower() == "n":
                print()
                print("Okay")
                break
            else:
                print("That's not an option.")
        while wait == False:
            print()
            direction = input("Which direction would you like to go?")
            if direction.lower() == "n" or direction.lower() == "north":
                if room_list[var][1] == None:
                    print("There's no door that way.")
                else:
                    current_room = room_list[var][1]
                    break
            if direction.lower() == "e" or direction.lower() == "east":
                if room_list[var][2] == None:
                    print("There's no door that way.")
                else:
                    if Ukey==1:
                        current_room = room_list[var][1]
                        break
                    else:
                        print("It's locked")
            if direction.lower() == "s" or direction.lower() == "south":
                if room_list[var][3] == None:
                    print("There's no door that way.")
                else:
                    current_room = room_list[var][3]
                    break
            if direction.lower() == "w" or direction.lower() == "west":
                if room_list[var][4] == None:
                    print("There's no door that way.")
                else:
                    current_room = room_list[var][4]
                    break
    if current_room == 10:
        print()
        print(room_list[current_room][0])
        var = current_room
        while wait == False:
            print()
            decision = input("Would you like to inspect eh bed?")
            if decision.lower() == "yes" or decision.lower() == "y":
                print()
                print("You pull back the curtains and there is a mummified body behind to curtains, it's wearing the"
                      "same clothes as you.... you look down at your hand and it's translucent.")
                break
            elif decision.lower() == "no" or decision.lower() == "n":
                print()
                print("Okay")
                break
            else:
                print("That's not an option.")
        while wait == False:
            print()
            decision = input("Would you like to inspect the clothes?")
            if decision.lower() == "yes" or decision.lower() == "y":
                print()
                print("You dig through the clothes and find a key")
                Fkey+=1
                break
            elif decision.lower() == "no" or decision.lower() == "n":
                print()
                print("Okay")
                break
            else:
                print("That's not an option.")
        while wait == False:
            print()
            direction = input("Which direction would you like to go?")
            if direction.lower() == "n" or direction.lower() == "north":
                if room_list[var][1] == None:
                    print("There's no door that way.")
                else:
                    current_room = room_list[var][1]
                    break
            if direction.lower() == "e" or direction.lower() == "east":
                if room_list[var][2] == None:
                    print("There's no door that way.")
                else:
                    current_room = room_list[var][2]
                    break
            if direction.lower() == "s" or direction.lower() == "south":
                if room_list[var][3] == None:
                    print("There's no door that way.")
                else:
                    current_room = room_list[var][3]
                    break
            if direction.lower() == "w" or direction.lower() == "west":
                if room_list[var][4] == None:
                    print("There's no door that way.")
                else:
                    current_room = room_list[var][4]
                    break
print()
pa=input("Would you like to play again?")
if pa=="y" or pa=="yes":
    print("Coolio")
    done=False
    wait=False
else:
    print("Come again soon!")





