'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''

room_list=[]
room=['''You're in a small entry way with a locked door behind you. it feels rather small as only one door is to the 
north.''',1,None,None,None]
room_list.append(room)
room=['''You go through the door into an electrical room. it has a large old power switch on the wall. some large power 
cables are cut and others damaged as if neglected for a long time.''',4,None,0,2]
room_list.append(room)
room=['''Entering the room you see and electrical box. It's a room that appears to control power form the other. power 
from here is given to all other rooms in the building.''',3,2,None,None]
room_list.append(room)
room=['''Looking around the room you see damaged wood. It's decorated as if a cabin but with dark stained wood. The trim
 and some boards missing from the wood flooring.''',8,4,2,None]
room_list.append(room)
room=['''Entering a place it's like a work shop. there a three work big work bencshes with tools on them. One has knives
 and kitchen cutlery. Another tool for wood working and construction. The last has cables and numerous electronics and 
 tools''',7,5,1,3]
room_list.append(room)
room=['''looking around this room you see it's like a serving area. It has a table and one chair at it. it seems as if 
something is''',6,None,None,4]
room_list.append(room)
room=['''The room around looks like an professional kitchen. Many tool and counter space to cook on. everything is 
neatly organized in all the cupboards.''',None,None,5,7]
room_list.append(room)
room=['''You're in a long hallway that's has dark wood trim. The flooring is a dark wood. The walls are like a wooden 
cabin. there are two doors splitting the hallway in half. Ones north the other south. at the end two doors east and 
west.''',9,6,4,8]
room_list.append(room)
room=['''You're in what appears to be an old brick building. the wall to the west has a hole with bricks missing and 
destroyed bricks and cracked mortar. It's a sizable hole and outside it's fiercely snowing. ''',None,7,3,None]
room_list.append(room)
room=['''The room you in is decorated lik and trophy room. There is a locked door to the north.''',None,None,7,None]
room_list.append(room)



current_room=0
next_room=0
completed_objectives=0

done=False
while not done:
    print()
    print(room_list[current_room][0])
    user_input = input("would you like to go N,E,S,W or Q").upper()
    if user_input=="N" or user_input=="North":
        next_room = room_list[current_room][1]
        current_room=next_room
    elif user_input=="E" or user_input=="East":
        next_room = room_list[current_room][2]
        current_room=next_room
    elif user_input=="S" or user_input=="South":
        next_room = room_list[current_room][3]
        current_room = next_room
    elif user_input=="W" or user_input=="West":
        next_room = room_list[current_room][4]
        current_room = next_room
    elif user_input=="Q" or user_input=="Quit":
        done = True
        print("Bye")
    else:
        print("I don't know what you typed.")
    if next_room == None:
        print("You can't go that way.")
    if current_room==6:
        task=input ("Do you want to complete task?")
        if task=="Y":
            completed_objectives += 1
            print("Task completed")
        else:
            print("Okay")
    if current_room==5:
        task=input("Do you want to complete task")
        if task=="Y":
            completed_objectives += 1
            print("Task completed")
        else:
            print("Okay")
    if completed_objectives==2:
        print("You succed in getting out.")
        done=True
