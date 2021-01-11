'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''

room_list=[]
room=["You're in a small entry way with a locked door behind you. it feels rather small as only one door is to the north.",1,None,None,None]
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
room=['''''',None,None,5,7]


done=False
chef_quest=0
electrician_quest=0
builder_quest=0
current_room=0

while done==False:

    print("")

