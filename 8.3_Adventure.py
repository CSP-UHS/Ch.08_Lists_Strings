'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
mail = "Check Mail"
open_mail = "There's 4 unopened envelopes"
porch_light = "Flip the porch lights"
hall_light = "Flip the lights"
centhall_light = "Flip the lights"
curtains = "Use curtains"
norhall_lights = "Flip the lights"
bed_lights = "Flip the lights"
garden_lights = "Flip the lights"
esthall_lights = "Flip the lights"
mastbed_lights = "Flip the lights"
dinerm_lights = "Flip the lights"
kitchen_lights = "Flip the lights"
bathrm_lights = "Flip the lights"
patio_lights = "Flip the lights"
eat_fridge = "Eat from the fridge"

porchlght = ["You flipped the lights off", "You flipped the lights on"]
halllght = ["You flipped the lights off", "You flipped the lights on"]
centhalllght = ["You flipped the lights off", "You flipped the lights on"]
norhalllight = ["You flipped the lights off", "You flipped the lights on"]
bedlght = ["You flipped the lights off", "You flipped the lights on"]
gardenlght = ["You flipped the lights off", "You flipped the lights on"]
esthalllght = ["You flipped the lights off", "You flipped the lights on"]
mastbedlght = ["You flipped the lights off", "You flipped the lights on"]
dinermlght = ["You flipped the lights off", "You flipped the lights on"]
kitchenlght = ["You flipped the lights off", "You flipped the lights on"]
bathrmlght = ["You flipped the lights off", "You flipped the lights on"]
patiolght = ["You flipped the lights off", "You flipped the lights on"]
curtainspread = ["You spread the curtains", "You closed the curtains"]
eat = "You ate a piece of food from the fridge"

room_list = []
room = ["You are on the Porch.", 1, None, None, None, mail, None, open_mail, None, None, None]
room_list.append(room)
room = ["You are in Hall.", 4, 2, None, 0, hall_light, porch_light, porchlght[0], halllght[0],porchlght[1], halllght[1]]
room_list.append(room)
room = ["You are in Central Hall.", 3, 6, 1, None, centhall_light, curtains, centhalllght[0], curtainspread[0], centhalllght[1], curtainspread[1]]
room_list.append(room)
room = ["You are in North Hall.", 12, 10, 5, 2, norhall_lights, None, norhalllight[0], None, norhalllight[1], None]
room_list.append(room)
room = ["You are in Bedroom.", None, None, None, 1, bed_lights, None, bedlght[0], None, bedlght[1], None]
room_list.append(room)
room = ["You are in Garden.", 11, 3, None, None, garden_lights, None, gardenlght[0], None, gardenlght[1], None]
room_list.append(room)
room = ["You are in East Hall.", 9, 7, 2, None, esthall_lights, None, esthalllght[0], None, esthalllght[1], None]
room_list.append(room)
room = ["You are in Master Bedroom.", None, None, 6, None, mastbed_lights, None, mastbedlght[0], None, mastbedlght[1], None]
room_list.append(room)
room = ["You are in Dining Room.", None, None, 9, None, dinerm_lights, None, dinermlght[0], None, dinermlght[1], None]
room_list.append(room)
room = ["You are in Kitchen.", None, 8, 6, None, kitchen_lights, eat_fridge, kitchenlght[0], eat, kitchenlght[1], None]
room_list.append(room)
room = ["You are in Bathroom.", None, None, 3, None, bathrm_lights, None, bathrmlght[0], None, bathrmlght[1], None]
room_list.append(room)
room = ["You are in Patio1.", None, 12, None, 5, patio_lights, None, patiolght[0], None, patiolght[1], None]
room_list.append(room)
room = ["You are in Patio2.", None, None, 11, 3, patio_lights, None, patiolght[0], None, patiolght[1], None]
room_list.append(room)

# spawning the player
current_room = 0
done = False
on = True
on2 = True
while not done:
    print()
    print(room_list[current_room][0])
    done2 = False
    while not done2:
        print("What do you want to do?")
        print("A)", room_list[current_room][5])
        if room_list[current_room][6] == None:
            pass
        else:
            print("B)", room_list[current_room][6])
        print("C) Go to other room")
        room_interact = input()

        if room_interact.upper() == "A":
            if on == True:
                print(room_list[current_room][7])
                on = False
            else:
                print(room_list[current_room][9])
                on = True
        elif room_interact.upper() == "B":
            if on2 == True:
                print(room_list[current_room][8])
                on2 = False
            else:
                print(room_list[current_room][10])
                on2 = True
        elif room_interact.upper() == "C":
            done2 = True
    news = input("Which way do you want to go? N,E,W,S or Q? ")
    if news.upper() == "N" or news.upper() == "NORTH":
        next_room = room_list[current_room][1]
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room
    elif news.upper() == "E" or news.upper() == "EAST":
        next_room = room_list[current_room][2]
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room
    elif news.upper() == "W" or news.upper() == "WEST":
        next_room = room_list[current_room][3]
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room
    elif news.upper() == "S"  or news.upper() == "SOUTH":
        next_room = room_list[current_room][4]
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room
    elif news.upper() == "Q" or news.upper() == "QUIT":
        done = True
    else:
        print("I don't understand")
