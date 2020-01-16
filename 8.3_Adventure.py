'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
room_list=[]
room=("you are next to the front door",1,None,None,None)
room_list.append(room)
room=("you enter the jaw dropping Living room",None,2,0,3)
room_list.append(room)
room=("you enter the dark and gloomy closet",None,None,None,1)
room_list.append(room)
room=("you enter the kitchen with much broken glass on the floor",4,1,None,None)
room_list.append(room)
room=("you enter the stunning sunroom with light penetrating every corner",6,5,3,None)
room_list.append(room)
room=("you enter the sunlit master bedroom with blood seemingly dried on the wall with evidence of a struggle",None,None,None,4)
room_list.append(room)
room=("You won! You've got out of the house",None,None,4,None)
room_list.append(room)

current_room=0
done=False
while not done:
    print()
    print(room_list[current_room][0])
    user_choice=input("N, E, S, W to move around, Q to Quit")

    if user_choice.lower() == "north" or user_choice.lower() == "n":
        next_room=room_list[current_room][1]
        if next_room==None:
            print("you cant go that way")
        else:
            current_room=next_room

    elif user_choice.lower() == "east" or user_choice.lower() == "e":
        next_room = room_list[current_room][2]
        if next_room == None:
            print("you cant go that way")
        else:
            current_room = next_room

    elif user_choice.lower() == "south" or user_choice.lower() == "s":
        next_room = room_list[current_room][3]
        if next_room == None:
            print("you cant go that way")
        else:
            current_room = next_room

    elif user_choice.lower() == "west" or user_choice.lower() == "w":
        next_room = room_list[current_room][4]
        if next_room == None:
            print("you cant go that way")
        else:
            current_room = next_room

    elif user_choice.lower() == "quit" or user_choice.lower() == "q":
        print("Thanks for playing!")
        done=True

    else:
        print("input not detected")

