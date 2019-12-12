'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
print("Welcome to my game, here you will try to excape the house through the livingroom door but first you will have to find the key")
room_list=[]
current_room=0
done=False
#ask if they would like to search in each room
room=["You enter the doorway into a room with a couch, a t.v., and a fire place.",2,None,None,None] # room 0, will find a lighter
room_list.append(room)
room=["You enter the Kitchen you see counters and a sink.",4,2,None,None]#room 1, find a knife
room_list.append(room)
room=["You enter the south hallway you see lots of doors.",5,3,0,1]#room2
room_list.append(room)
room=["You enter the bathroom you see your reflection and some cabnents and a sink.",6,None,None,2]#room 3, find a toothbrush
room_list.append(room)
room=["You entered the dinning room, you see a table, chairs, and hutch.",None,5,1,None]#room 4 find a candle stick
room_list.append(room)
room=["You have entered the north hallway, you see an table witha vase of flowers.",7,6,2,4]#room 5
room_list.append(room)
room=["You have entered the guest bedroom, you see a bed and a dresser.",8,None,3,5]#room 6 find shoes?
room_list.append(room)
room=["You have entered the Master bedroom, You see a bed, another door, and a dresser.",None,8,5,None]#room 7 you find nothing of use or value
room_list.append(room)
room=["You have entered the Master Bathroom, you see a mirror, cabinents and a glass shower.",None,None,6,7]#room 8 possibly find a key
room_list.append(room)
while not done:
    print()
    print(room_list[current_room][0])
    An=input("Please enter N,E,S,W,Q to move to the next room in that direction")
    if An = "N" or An = "n":
        next_room=room_list[current_room][2]
        if next_room==None:
            print("You can't go that way")
        else:
            current_room=next_room
    elif An = "E" or An = "e":
        next_room=room_list[current_room][0]
        if next_room==None:
            print("You can't go that way")
        else:
            current_room=next_room
#start on number 13 and fix the elif with what room there next one would be and comment what things are doing