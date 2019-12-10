'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
print("Welcome to my game, here you will try to excape the house through the livingroom door but first you will have to find the key")
room_list=[]
#ask if they would like to search in each room
room=["You enter the doorway into a room with a couch, a t.v., and a fire place.",2,None,None,None] # room 0, will find a lighter
room_list.append(room)
room=["You enter the Kitchen you see counters and a sink.",4,2,None,None]#room 1, find a knife
room_list.append(room)
room=["You enter the south hallway you see lots of doors.",5,3,0,1]#room2
room_list.append(room)
room=["You enter the bathroom you see your reflection and some cabnents and a sink.",]#room 3, find a toothbrush
room_list.append(room)
room=["You entered the dinning room, you see a table, chairs, and hutch",]#room 4 find a candle stick
room_list.append(room)
room=["You have entered the north hallway, you see an table witha vase of flowers",]#room 5
room_list.append(room)
room=["You have entered the guest bedroom, you see a bed and ",]#room 6 find shoes?
room_list.append(room)
room=["",]#room 7 you find nothing of use or value
room_list.append(room)
room=["",]#room 8 possibly find a key
room_list.append(room)
