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
room=["You enter the doorway into a room with a couch, a t.v., and a fire place.",2,None,None,None]
room_list.append(room)
room=["You enter the Kitchen you see counters and a sink.",4,2,None,None]
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
    an=input("Please enter N,E,S,W to move to the next room in that direction or Q to quit")
    if an.upper() == "N" or an.lower() == "north":
        next_room=room_list[current_room][1]
        if next_room==None:
            print("You can't go that way")
        else:
            current_room=next_room
    elif an.upper() == "E" or an.lower() == "east":
        next_room=room_list[current_room][2]
        if next_room==None:
            print("You can't go that way")
        else:
            current_room=next_room
    elif an.upper() == "S" or an.lower() == "south":
        next_room=room_list[current_room][3]
        if next_room==None:
            print("You can't go that way")
        else:
            current_room=next_room
    elif an.upper() == "W" or an.lower() == "west":
        next_room=room_list[current_room][4]
        if next_room==None:
            print("You can't go that way")
        else:
            current_room=next_room
    elif an.upper() == "Q" or an.lower() == "quit":
        print("Thanks for playing!")
        done=True
    else:
        print("Thats not an option try again")
    if current_room == 1:
        item = input("Would you like to search the room? Y for yes and N for no")
        if item.upper()=="Y"
            print("You found a Knife but no key")
    if current_room == 3:
        item = input("Would you like to search the room? Y for yes and N for no")
        if item.upper()=="Y"
            print("You found a toothbrush and mouthwash but no key")
    if current_room == 4:
        item = input("Would you like to search the room? Y for yes and N for no")
        if item.upper()=="Y"
            print("You found a candle stick but no key")
    if current_room == 5:
        item = input("Would you like to search the room? Y for yes and N for no")
        if item.upper()=="Y"
            print("You found the key in ...")#finnish

#comment what things are doing
#add a serch function input and make an inventory
#add if you get the key you can excape out the living room and you win