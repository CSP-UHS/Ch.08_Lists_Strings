'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure gamer
'''

def Beans():
    while True:
        print("Beans")

room_list = []
#0
room = ["You are by the Front Door. To the South, you see a door that leads to the front yard, which is covered by a blanket of snow. To the North is the rest of your house. (N)", 1,None,None,None]
room_list.append(room)
#1
room = ["You are in the Art Hallway. You are in a long hallway. There is a painting on your left which looks like it will crumble if you touch it and a flower vase on your right.(N,S)",2, None, 0,None]
room_list.append(room)
#2
room = ["You are in the Snake Room. You see an open room to your left and to your right. A snake is sitting in a tank in front of you. It looks dangerous.(E,S,W)", None, 4,1,3]
room_list.append(room)
#3
room = ["You are in the Broken Floor Room. You are in a corner. The floor creaks when you walk around.(N,E)", 5,2,None, None]
room_list.append(room)
#4
room = ["You are in the Crazy Floor Room. You are in a corner. The floor is covered in confusing patterns that make you dizzy when you look at them.(N,W)", 7,None,None,2]
room_list.append(room)
#5
room = ["You are in the Crazy Wall Room. You are in a corner. The walls are painted in crazy colors that make your head hurt. You look at the ground when walking through this room.(S,E)", None, 6, 3,None]
room_list.append(room)
#6
room = ["You are in the Bathroom. The is an open room to your left and to your right. There is a random sink with a mirror above it. The mirror opens.(N,E,W)", 8,7,None,5]
room_list.append(room)
#7
room = ["You are in the Broken Walls Room. The walls around you are peeling and revealing wooden boards behind them. Other than that, the room looks to be in pristine condition.(W,S)",None,None,4,6]
room_list.append(room)
#8
room = ["You are in the Back Window Room. You see a window with snow falling outside. You try to break it but the glass just vibrates. It appears to be bullet proof.(S)", None,None,6,None]
room_list.append(room)
#Game
print("Your sitting in your house enjoying some hot cocoa to combat the cold weather.")
print("You feel your house getting colder. Worried, you check you thermostat.")
print("The temperature is dropping by the second.")
print("The door is locked from the outside. Your house is very weird.")
print("Realizing you lost the key somewhere, you need to find it before you freeze.")
print("You have 100 minutes to get out of the house, every move takes 1 minute.")
print("To interact with objects, type I or interact.")
print("If you obtain an item, type B or backpack to view what you have.")
print("To quit, type Q or quit")
print("Go the direction you want by typing the letter for that direction (N, E, S, W).")
print()
print()
print()
items = []
jacket = False
rocky = False
crowbar = False
first_attempt = True
firstAttempt = True
escape_key = False
key2 = False
lose = False
win1 = False
win2 = False
bad_end = False
painting = True
vase = True
goggles = False
outOfTime = False
time = 0
current_room=0
done = False
painkillers = False
while done == False:
    print()
    print(room_list[current_room][0])
    direction = input("What do you want to do (N, E, S, W | I, B, Q)? ")
    direction = direction.replace(" ","")
    if direction.lower() == ("n") or direction.lower() == ("north"):
        next_room = room_list[current_room][1]
        if next_room == None:
            print("You can't go that way!")
        else:
            current_room = next_room
    elif direction.lower() == "e" or direction.lower() == "east":
        next_room = room_list[current_room][2]
        if next_room == None:
            print("You can't go that way!")
        else:
            current_room = next_room
    elif direction.lower() == "s" or direction.lower() == "south":
        next_room = room_list[current_room][3]
        if next_room == None:
            print("You can't go that way!")
        else:
            current_room = next_room
    elif direction.lower() == "w" or direction.lower() == "west":
        next_room = room_list[current_room][4]
        if next_room == None:
            print("You can't go that way!")
        else:
            current_room = next_room
    elif direction.lower() == "q" or direction.lower() == "quit":
        done = True
    elif direction.lower() == "i" or direction.lower() == "interact":
        if current_room == 0:
            if escape_key == True:
                print("You unlock the front door.")
                print("It's even colder outside.")
                win1 = True
                done = True
            else:
                print("You try to unlock the door but are unable to open it.")
        elif current_room == 1:
            interact = input("Do you interact with the painting or the vase? (P or V) ")
            interact = interact.replace(" ","")
            if interact.lower() == "p" or interact.lower() == "painting":
                if painting == True:
                    print("You touch the painting.")
                    print("It instantly crumbles, leaving just the wall behind it.")
                    if vase == False:
                        room_list[1][0] = ("You are in a long hallway. It looks bland as you have destroyed all of the art in it.")
                    else:
                        room_list[1][0] = ("You are in a long hallway. There is a flower vase on your right.")
                    painting = False
                else:
                    print("You already destroyed the painting...")
            elif interact.lower() == "v" or interact.lower() == "vase":
                if vase == True:
                    print("You pick up and smash the vase.")
                    print("It breaks and leaves dirt and a now sad flower on the floor. There was nothing in the dirt.")
                    if painting == False:
                        room_list[1][0] = ("You are in a long hallway. It looks bland as you have destroyed all of the art in it.")
                    else:
                        room_list[1][0] = ("You are in a long hallway. There is a painting on your left which looks like it will crumble if you touch it.")
                    vase = False
                else:
                    print("You already destroyed the vase...")
        elif current_room == 2:
            if key2 == False:
                interact = input("Are you sure you want to reach into the tank with the snake? ")
                interact = interact.replace(" ","")
                if interact.lower() == "y" or interact.lower() == "yes":
                    interact = input("Like super duper ultra sure? ")
                    interact = interact.replace(" ", "")
                    if interact.lower() == "y" or interact.lower() == "yes":
                        interact = input("You definitely won't regret it? ")
                        interact = interact.replace(" ", "")
                        if interact.lower() == "y" or interact.lower() == "yes":
                            print("You reach into the tank.")
                            print("The snake wraps itself around your arm.")
                            print("It appears to be harmless.")
                            print("You find a very tiny key inside the tank.")
                            key2 = True
                            items.append("Small Key")
                        else:
                            print("If you will regret it, then don't do it.")
                    else:
                        print("You need to be sure.")
                else:
                    print("You step away from the tank.")
            else:
                print("You already found everything in the tank.")
        elif current_room == 3:
            if crowbar == False:
                print("You inspect the broken boards on the floor.")
                print("You find a loose board and see something under it, but you can't reach it.")
                interact = input("Do you try to pull open the board and grab it? ")
                interact = interact.replace(" ","")
                if interact.lower() == "y" or interact.lower() == "yes":
                    if painkillers == True:
                            print("You take your painkillers in order to pull back the board. You do so with relative ease.")
                            print("Underneath was a crowbar.")
                            print("You take the crowbar.")
                            crowbar = True
                            items.append("Crowbar")
                            items.remove("Painkillers")
                    else:
                        if first_attempt == True:
                            print("You attempt to pull back the board, but the pain from doing so is too great and you pass out.")
                            print("You wake up after 15 minutes, it is noticeably colder.")
                            time += 15
                        else:
                            print("You don't want to try again until you have something to numb the pain.")
                else:
                    print("You stand back up.")
            else:
                print("There is nothing there.")
        elif current_room == 4:
            if goggles == True:
                print("With the googles you are able to look at the floor.")
                print("On the ground you see the key to get outside.")
                print("You quickly grab it.")
                print("The goggles break from the disgusting floor pattern.")
                escape_key = True
                goggles = False
                items.append("Front Door Key")
                items.remove("Goggles")
            else:
                if firstAttempt == True:
                    print("You try to look at the floor but instantly pass out from the colors.")
                    print("You wasted 25 minutes.")
                    time += 25
                    firstAttempt = False
                else:
                    print("You do not want to waste any more time.")
        elif current_room == 5:
            if goggles == True:
                print("Using the goggles, you look at the walls and see a small key hole.")
                if key2 ==  True:
                    print("You use the key from the snake tank and open a compartment in the wall.")
                    print("It's your old hidden closet, and it contains a thick winter jacket.")
                    print("You put it on and feel a lot warmer")
                    print("You estimate you now have 15 minutes longer to get out.")
                    print("The goggles break shortly after from all of the disgusting colours.")
                    goggles = False
                    jacket = True
                    items.remove("Goggles")
                    items.append("Winter Jacket (equipped)")
                    time-=15
                else:
                    print("You don't have a key that works.")
                    print("The goggles break shortly after from all of the disgusting colours.")
                    goggles = False
                    items.remove("Goggles")
            else:
                print("You look up at the walls and instantly pass out.")
                print("You remember a blur of some kind of hole in the wall.")
                print("You wasted 25 minutes from passing out.")
                time+=25
        elif current_room == 6:
            if time <= 50:
                if rocky == True and painkillers == True:
                    print("There is nothing else in the mirror.")
                else:
                    print("You open up the mirror.")
                    if rocky == True:
                        print("There are some painkillers.")
                        interact = input("Do you grab the painkillers? ")
                        interact = interact.replace(" ", "")
                        if interact.lower() == "painkillers" or interact.lower() == "p":
                            print("You grab the painkillers.")
                            painkillers = True
                            items.append("Painkillers")
                        else:
                            print("You step away without grabbing anything")
                    elif painkillers == True or crowbar == True:
                        print("There is your best friend Rocky, who is a rock.")
                        print("Rocky looks cold.")
                        interact = input("Do you grab Rocky? ")
                        interact = interact.replace(" ", "")
                        if interact.lower() == "rocky" or interact.lower() == "r":
                            print("You grab rocky.")
                            print("He seems happy to see you came back.")
                            rocky = True
                            items.append("Rocky")
                        else:
                            print("You step away without grabbing anything")
                    else:
                        print("There is your best friend Rocky, who is a rock, and some painkillers.")
                        print("Rocky looks cold.")
                        interact = input("Do you grab Rocky or the painkillers? ")
                        interact = interact.replace(" ","")
                        if interact.lower() == "rocky" or interact.lower() == "r":
                            print("You grab rocky.")
                            print("He seems happy to see you.")
                            rocky = True
                            items.append("Rocky")
                        elif interact.lower() == "painkillers" or interact.lower() == "p":
                            print("You grab the painkillers.")
                            print("Rocky looks sad to see you go.")
                            painkillers = True
                            items.append("Painkillers")
                        else:
                            print("You step away without grabbing anything")
            else:
                print("You attempt to open up the mirror, but it is frozen shut.")
        elif current_room == 7:
            print("You walk up to the peeling walls.")
            interact = input("Do you attempt to pull back the boards on the wall? ")
            interact = interact.replace(" ", "")
            if interact.lower() == "y" or interact.lower() == "yes":
                if crowbar == True:
                    print("You use the crowbar to pull back the boards.")
                    print("You find a goggles that seem to make it easier to view walls.")
                    goggles = True
                    items.append("Goggles")
                else:
                    print("You try to pull away the boards, but the are still nailed in tight.")
                    print("You ended up wasting 5 minutes.")
                    time+=5
            else:
                print("You step away from the wall")
        elif current_room == 8:
            if rocky == True:
                print("You smash the window with the rock.")
                print("The window was bullet proof but it was not rock proof.")
                if jacket == False:
                    lose = True
                    done = True
                else:
                    win2 = True
                    done = True
            else:
                print("You bang your hand on the window again. It does nothing.")
                print("You wasted a minute.")
                time+=1
        else:
            print("Bruh how'd you get there??")
    elif direction.lower() == "b" or direction.lower() == "backpack":
        if len(items) == 0:
            print("You have nothing in your backpack.")
        else:
            print(items)
    elif direction.lower() == "beans":
        Beans()
    elif time >= 100:
        outOfTime = True
        done = True
    else:
        print("Please pick N, E, S, W, Quit, or Interact.")
        time-=1
    time+=1
print()
print()
if win1 == True:
    print("You decide to go over to a neighbors house to escape the cold.")
    print("You later learn of a murder in the town, with the body discovered right behind your house.")
    print("Because you were with your neighbor, you had an alibi.")
    print("You get your heating fixed and continue to live in your house.")
    print("You got the:")
    print()
    print()
    print()
    print("             NEUTRAL ENDING             ")
    print()
    print()
    print()
elif win2 == True:
    print("You break the window and run outside.")
    print("You realize it is a lot colder outside, but luckily you have a jacket on.")
    print("You run into the woods hoping to escape the cold winds.")
    print("While outside, you see someone with a large bag and a shovel.")
    print("They are burying a body!")
    print("The police are able to catch the murderer based on your description.")
    print("You become recognized as a town hero, and are given substantial compensation.")
    print("You get your heating fixed and use the money to buy multiple goggles so that you never lose your keys again.")
    print("You got the:")
    print()
    print()
    print()
    print("             GOOD ENDING             ")
    print()
    print()
    print()
elif lose == True:
    print("You break the window and run outside.")
    print("You realize it is a lot colder outside.")
    print("You run into the woods hoping to escape the cold winds.")
    print("While outside, you see someone with a large bag and a shovel.")
    print("They are burying a body!")
    print("They person runs away and you run to see who was killed.")
    print("It was your neighbor!")
    print("You pass out from the cold and exhaustion next to the body.")
    print("The police find you with the body and shortly after, arrest you.")
    print("You spend the rest of your life in prison.")
    print()
    print()
    print()
    print("             BAD ENDING             ")
    print()
    print()
    print()
elif outOfTime == True:
    print("You freeze to death inside of your own house.")
    print("The police find your body and associate it with a murder that happened around the same time.")
    print("You throw off the police with your death so long that the murderer eventually dies of old age.")
    print("You caused a cold case that will never be solved.")
    print()
    print()
    print()
    print("             TIME-OUT ENDING             ")
    print()
    print()
    print()
else:
    print("Imagine not being able to finish the game.")
    print("Go back and finish the game for real my dude.")
    print()
    print()
    print()
    print("             BAILED ENDING             ")
    print()
    print()
    print()
