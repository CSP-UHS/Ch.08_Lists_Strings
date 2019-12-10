'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game


'''

def Beans():
    while True:
        print("Beans")

room_list = []
#0
room = ["You see a door that leads to the front yard, which is covered by a blanket of snow. (N)", 1,None,None,None]
room_list.append(room)
#1
room = ["You are in a long hallway. There is a painting on your left which looks like it will crumble if you touch it and a flower vase on your right.(N,S)",2, None, 0,None]
room_list.append(room)
#2
room = ["You see an open room to your left and to your right. A snake is sitting in a tank in front of you. It looks dangerous.(E,S,W)", None, 4,1,3]
room_list.append(room)
#3
room = ["You are in a corner. The floor creaks when you walk around.(N,E)", 5,2,None, None]
room_list.append(room)
#4
room = ["You are in a corner. The floor is covered in confusing patterns that make you dizzy when you look at them.(N,W)", 7, 2,None,None]
room_list.append(room)
#5
room = ["You are in a corner. The walls are painted in crazy colors that make your head hurt. You look at the ground when walking through this room.(S,E)", None, None, 3,6]
room_list.append(room)
#6
room = ["The is an open room to your left and to your right. There is a random sink with a mirror above it. The mirror opens.(N,E,W)", 8,5,None,7]
room_list.append(room)
#7
room = ["The walls around you are peeling and revealing wooden boards behind them. Other than that, the room looks to be in pristine condition.(E,S)",None,6,4,None]
room_list.append(room)
#8
room = ["You see a window with snow falling outside. You try to break it but the glass just vibrates. It appears to be bullet proof.(S)", None,None,6,None]
room_list.append(room)
#Game
print("Your sitting in your house enjoying some hot cocoa to combat the cold weather.")
print("You feel your house getting colder. Worried, you check you thermostat.")
print("The temperature is dropping by the second.")
print("The door is locked from the outside. Your house is very weird.")
print("Realizing you lost the key somewhere, you need to find it before you freeze.")
print("To interact with objects, type I or interact.")
print("To quit, type Q or quit")
print("Go the direction you want by typing the letter for that direction (N, E, S, W).")
print()
print()
print()
crowbar = False
first_attempt = True
escape_key = False
key2 = False
lose = False
win1 = False
win2 = False
bad_end = False
painting = True
vase = True
time = 0
current_room=0
done = False
painkillers = False
while done == False:
    print()
    print(room_list[current_room][0])
    direction = input("What do you want to do (N, E, S, W | I, Q)? ")
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
                win1 = True
                done = True
            else:
                print("You try to unlock the door but are unable to open it.")
        elif current_room == 1:
            interact = input("Do you interact with the painting or the vase? (P or V) ")
            interact = interact.replace(" ","")
            if interact.lower() == "p" or interact.lower() == "painting":
                print("You touch the painting.")
                print("It instantly crumbles, leaving just the wall behind it.")
                if vase == False:
                    room_list[1][0] = ("You are in a long hallway. It looks bland as you have destroyed all of the art in it.")
                else:
                    room_list[1][0] = ("You are in a long hallway. There is a flower vase on your right.")
                painting = False
            elif interact.lower() == "v" or interact.lower() == "vase":
                print("You pick up and smash the vase.")
                print("It breaks and leaves dirt and a now sad flower on the floor. There was nothing in the dirt.")
                if painting == False:
                    room_list[1][0] = ("You are in a long hallway. It looks bland as you have destroyed all of the art in it.")
                else:
                    room_list[1][0] = ("You are in a long hallway. There is a painting on your left which looks like it will crumble if you touch it.")
                vase = False
        elif current_room == 2:
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
                        print("You find a very tiny key inside.")
                        key2 = True
                    else:
                        print("If you will regret it, then don't do it.")
                else:
                    print("You need to be sure.")
            else:
                print("You step away from the tank.")
        elif current_room == 3:
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
                else:
                    if first_attempt == True:
                        print("You attempt to pull back the board, but the pain from doing so is too great and you pass out.")
                        print("You wake up after 15 minutes, it is noticeably colder.")
                        time += 15
                    else:
                        print("You don't want to try again until you have something to numb the pain.")
            else:
                print("You stand back up.")
        elif current_room == 4:
            pass
        elif current_room == 5:
            pass
        elif current_room == 6:
            pass
        elif current_room == 7:
            print("You walk up to the peeling walls.")
            interact = input("Do you attempt to pull back the boards on the wall? ")
            interact = interact.replace(" ", "")
            if interact.lower() == "y" or interact.lower() == "yes":
                if crowbar == True:
                    pass
            else:
                print("You step away from the wall")
        elif current_room == 8:
            pass
    elif direction.lower() == "beans":
        Beans()
    elif time == 100:
        lose = True
        done = True
    else:
        print("Please pick N, E, S, W, Quit, or Interact.")
    time+=1


