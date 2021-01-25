'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''

# # room setup: Room Description, North, East, South, West,
import random

room_list = []
room = ['You stand in the castle entrance.  The main courtyard lies to the south, and the guard tower is to the West.',
        None, None, 1, 2]
room_list.append(room)
room = ['The courtyard is connects to many parts of the castle.  The entrance is to the north, the Kitchen is to the '
        'east, the Grand Hall is to the south, and the West wall is to the west.', 0, 5, 6, 3]
room_list.append(room)
room = ['From the top of the tower, you can see most of the castle.  The entrance is to the east, and the West wall is '
        'to the south.', None, 0, 3, None]
room_list.append(room)
room = ['The West wall is wide and straight.  There are plenty of crates to hide behind.  The tower is to the north, '
        'and the courtyard is to the East, and the South wall is to the south.', 2, 1, 4, None]
room_list.append(room)
room = ['The South wall is a small and cramped corridor.  The West wall is to the north.  There is a hidden passage to '
        'the Throne room to the east.', 3, 7, None, None]
room_list.append(room)
room = ['The kitchen is filled with smoke, and it smells of fresh bread.  The only way out is to the west, into '
        'the courtyard.', None, None, None, 1]
room_list.append(room)
room = ['You feel small next to the towering pillars in the Grand Hall.  One set of stairs to the west leads to the '
        'Throne room, and another set to the east leads to the Royal Bedroom.  The courtyard is also to the north.',
        1, 8, None, 7]
room_list.append(room)
room = ['The large golden throne dominates the Throne room.  Strangely, there are no guards here.  A doorway to the '
        'east leads to the Grand Hall.  There is also a hidden passage to the west.', None, 6, None, 4]
room_list.append(room)
room = ['The heavy curtains make the Royal bedroom feel dark yet spacious.  The only exit is to the west, into the '
        'Grand Hall.', None, None, None, 6]
room_list.append(room)

# #print(room_list)

current_room = 0

done = False
next_room = None


royal_crown = False  # #In order to win, you must escape with the crown

coin_sack = False    # #bribe guards
bread = False        # #bribe peasant
rope = False         # #escape over wall
knife = False        # #fight guards
royal_clothing = False      # #disguise self
peasants_clothing = False   # #disguise self


def investigate():
    print('\nYou investigate the room.')
    global royal_crown, coin_sack, bread, rope, knife, royal_clothing, peasants_clothing    # #make all variables global

    if current_room == 7 and royal_crown is False:
        print('\nYou find the royal crown resting upon the throne.')
        royal_crown = True
    elif current_room == 8 and royal_clothing is False:
        print('\nYou find a set of royal clothing in the closet.')
        royal_clothing = True
    elif current_room == 5 and bread is False:
        print('\nYou steal a piece of bread from the kitchen.')
        bread = True
    elif current_room == 4 or current_room == 2 and coin_sack is False and random.randrange(0, 2) == 1:
        print('\nYou find a coin sack hidden underneath a loose floorboard')
        coin_sack = True
    elif random.randrange(0, 4) == 1 and rope is False:
        print('You find a rope.')
        rope = True
    elif random.randrange(0, 4) == 1 and peasants_clothing is False:
        print("You find a set of peasant's clothing.")
        peasants_clothing = True
    elif random.randrange(0, 4) == 1 and knife is False:
        print('You find a knife.')
        knife = True
    else:
        print('\nYou do not find anything in your investigation.')


def inventory():
    print('\nCurrent backpack items:')
    if coin_sack is True:
        print('Sack of coins')
    if bread is True:
        print('Bread')
    if rope is True:
        print('Rope')
    if knife is True:
        print('Knife')
    if royal_clothing is True:
        print('Royal Clothing')
    if peasants_clothing is True:
        print("Peasant's Clothing")
    action = input('\nWould you like to use an item? (Y/N): ')
    if action.upper() == 'Y' or action.upper() == 'YES':
        print('placeholder')
    elif action.upper() == 'N' or action.upper() == 'NO':
        print('You do not use an item.')


while not done:
    print('\n', room_list[current_room][0])
    choice = input('Would you like to go North, South, East, or West?  You can also investigate the current room (I) '
                   'or check your backpack (B).  Enter Q to quit: ')
    if choice.upper() == 'N' or choice.upper() == 'NORTH':
        next_room = room_list[current_room][1]
        if next_room is None:
            print('\nThere is no room there.')
        else:
            current_room = next_room
            print('\nYou enter the room to the north.')
    elif choice.upper() == 'E' or choice.upper() == 'EAST':
        next_room = room_list[current_room][2]
        if next_room is None:
            print('\nThere is no room there.')
        else:
            current_room = next_room
            print('\nYou enter the room to the east.')
    elif choice.upper() == 'S' or choice.upper() == 'SOUTH':
        next_room = room_list[current_room][3]
        if next_room is None:
            print('\nThere is no room there.')
        else:
            current_room = next_room
            print('\nYou enter the room to the south.')
    elif choice.upper() == 'W' or choice.upper() == 'West':
        next_room = room_list[current_room][4]
        if next_room is None:
            print('\nThere is no room there.')
        else:
            current_room = next_room
            print('\nYou enter the room to the west.')
    elif choice.upper() == 'Q' or choice.upper() == 'QUIT':
        done = True
        continue

    elif choice.upper() == 'I' or choice.upper() == 'INVESTIGATE':
        investigate()

    elif choice.upper() == 'B' or choice.upper() == 'BACKPACK':
        inventory()


# #mechanic to search from the tower?
