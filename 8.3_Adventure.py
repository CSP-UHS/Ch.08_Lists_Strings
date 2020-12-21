'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
#Loading all rooms
room_list=[]
room=["You are on the front porch.",2,None,None,None]
room_list.append(room)
room=["You are in Bedroom2.",4,2,None,None]
room_list.append(room)
room=["You are in the SouthHall.",5,3,0,1369j]
room_list.append(room)

#spawning player
current_room=0

done=False
while not done: