'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
room_list = []
#0 - Entrance
room = ["You are in the Entrance. It's a skinny room, but filled with people, you will have to do some maneuvering.",None,1,None,None]
room_list.append(room)
#1 - Central Dining
room = ["You are in the main dining room, a large and open space from your rat perspective. "
        "Many people eating at their tables, but you can't quite see what they're eating. "
        "To your left you see stairs going up somewhere, and in directly ahead you see a kitchen, but no entrance.",6,2,None,0]
room_list.append(room)
#2 - North Dining
room = ["You are in the second dining room, a space similar to the main dining room, but with a few less people, and a bit more secluded."
        "There is a door to the kitchen in front of you.",3,None,None,1]
room_list.append(room)
#3 - Kitchen
room = ["You are in the kitchen. Chefs everywhere. One of them almost steps on you as they busily walk by."
        "You look to see what they're carrying, but nothing interesting.",5,4,2,None]
room_list.append(room)
#4 - Fridge
room = ["You are in the walk-in fridge. It's pretty cold, so you shouldn't stay long. You see another rat with some cheese."
        "It's not the good cheese though. There's food everywhere, you almost don't know where to start.",None,None,None,3]
room_list.append(room)
#5 - Storage
room = ["You are in the walk-in pantry. There's some good stuff in there, but there doesn't seem to be any cheese.",None,None,3,None]
room_list.append(room)
#6 - Balcony
room = ["As you go up the stairs, a woman walking down the stairs screams and starts running. You pause and listen for footsteps."
        "Sure enough, the woman ratted you out, You have less than a minute before they get to you, and this is your last chance,"
        "because going back down is surely the end of the line for you",None,None,None,None]