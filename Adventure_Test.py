# Rules
'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
# Defining Variables
x = 0
desk = False
chest = False
quest = True
safe = False
# Creating Changing Room names for the hallway
halllist = ["1. Go to first room on left", "2. Go to second room on left", "3. Go to First room on right",
            "4. Go to second room on right", "5. Go through the open doorway", "6. Go to cargo hold"]

# Putting rooms in master list
Mroom = [
 ["You are in the cargo hold", "You see a ladder to a balcony that leads to a hallway in front of you, "
  "and a ladder that leads to a room above you.", "1. Go to hallway\n2. Go up", 2, 8, 0, 0, 0, 0],
 ["You are in the hallway", str(halllist), "", 3, 4, 6, 5, 7, 1],
 ["You are in a colorful and dangerous room", "there are weapons of all kinds hanging from colorful and beautiful walls"
  , "1. Go back to hallway", 2, 0, 0, 0, 0, 0],
 ["You are in a smelly and unkempt room", "the beds are unmade, there is food all over the floor",
  "1. Go back to hallway", 2, 0, 0, 0, 0, 0],
 ["You are in a seemingly untouched room", "everything is neat and perfect, almost as if no one has been in there "
  "in years", "1. Go back to hallway", 2, 0, 0, 0, 0, 0],
 ["You tried to open the door, but it is locked"],
 ["You are in the living room", "there is a couch with a weird looking holographic chess table in front of it",
  "1. Go back to hallway", 2, 0, 0, 0, 0, 0],
 ["You are in the cockpit", "Outside the window you see thousands of stars",
  "1. Go to gunner seat\n2. Go to Phantom\n3. Go down", 9, 10, 1, 0, 0, 0],
 ["You are in the nose gunner", "there is a white helmet with yellow and orange stripes sitting next to the seat",
  "1. Go back to the cockpit", 8, 0, 0, 0, 0, 0],
 ["You are in the phantom", "idk", "1. Go back to cockpit", 8, 0, 0, 0, 0, 0]]

# Creating function for changing text


def namechange():
    if x == 2:
        halllist[0] = "1. Enter Sabine's room"
    elif x == 3:
        halllist[1] = "2. Enter Ezra and Zeb's room"
    elif x == 4:
        halllist[3] = "4. Enter Kanan's room"
    elif x == 5:
        halllist[2] = "3. Try to enter Hera's room"
    elif x == 0:
        Mroom[0][0] = "You are back in the cargo hold"
    elif x == 1:
        Mroom[1][0] = "You are back in the hallway"
    elif x == 8:
        Mroom[7][0] = "You are back in the living room"


# Creating Game
while True:
    if x == 5:
        print(Mroom[5][0], "\n")
        x = 1
        continue
    if x == 1:
        print(Mroom[1][0], "\n")
        for i in range(len(halllist)):
            print(halllist[i])
    else:
        print(Mroom[x][0], "\n")
        print(Mroom[x][1], "\n")
        print(Mroom[x][2])
    namechange()
    move = int(input("\nWhat would you like to do?\n"))
    if move > 0:
        if Mroom[x][move+2] - 1 < 0:
            print("\n\033[31mBad move, try again\033[0m\n")
        else:
            x = Mroom[x][move+2] - 1
    else:
        print("\n\033[31mBad move, try again\033[0m\n")