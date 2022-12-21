"""
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game
"""
room_list = []
room = ["Starting Room", 3, 1, 0, 0]  # room 0
room_list.append(room)
# ----------------------------
room = ["Science Room", 1, 2, 1, 0]  # room 1
room_list.append(room)
# ----------------------------
room = ["Science Test", 2, 2, 2, 1]  # room 2
room_list.append(room)
# ----------------------------
room = ["English Room", 4, 3, 0, 3]  # room 3
room_list.append(room)
# ----------------------------
room = ["English Test", 4, 5, 3, 4]  # room 4
room_list.append(room)
# ----------------------------
room = ["Random Trivia", 6, 5, 5, 4]  # room 5
room_list.append(room)
# ----------------------------
room = ["Math Room", 6, 7, 5, 6]  # room 6
room_list.append(room)
# ----------------------------
room = ["Math Test", 8, 6, 7, 7]  # room 7
room_list.append(room)
# ----------------------------
room = ["History Room", 9, 8, 7, 8]  # room 8
room_list.append(room)
# ----------------------------
room = ["History Test", 9, 9, 8, 10]  # room 9
room_list.append(room)
# ----------------------------
room = ["Final Exam", 10, 9, 10, 11]  # room 10
room_list.append(room)
# ----------------------------
room = ["Prize", 11, 11, 11, 10]  # room 11
room_list.append(room)
# ----------------------------
current_room = 0
# START PROGRAM ---------------------------------------------------------
done = False
# If you don't want to go to the science room to get a key, change key = to a number greater than 2.
key = 0
print()
print("\033[0;33mINSTRUCTIONS:\n")
print("\033[0;0m - In each room, you will be tested on your school smarts.")
print(" - You will be asked 3 questions in each room and you must get all 3 correct to move on.")
print(" - 1 wrong answer and you'll be sent to the beginning - the starting room")
print(" - There are 2 rooms of each subject (history, math, science, and english): 1st room is the easier "
      "questions and the other is your test, the harder ones. \n")
print("If you look anything up, then you have already lost.")
print("   ============================================================================================================")
while not done:
    print()
    print("\033[0;34mThis is the starting room. No troubles shall come to you in this room.\n")
    direction = input("Which way? North, East, South, West? or Q to quit ")
    if direction.lower() == "north":
        next_room = room_list[current_room][1]
        current_room = next_room
    elif direction.lower() == "n":
        next_room = room_list[current_room][1]
        current_room = next_room
    # ---------------------------------
    elif direction.lower() == "east":
        next_room = room_list[current_room][2]
        current_room = next_room
    elif direction.lower() == "e":
        next_room = room_list[current_room][2]
        current_room = next_room
    # ------------------------------------
    elif direction.lower() == "south":
        next_room = room_list[current_room][3]
        current_room = next_room
    elif direction.lower() == "s":
        next_room = room_list[current_room][3]
        current_room = next_room
    # ------------------------------------
    elif direction.lower() == "west":
        next_room = room_list[current_room][4]
    elif direction.lower() == "w":
        next_room = room_list[current_room][4]
        current_room = next_room
    # ------------------------------------
    elif direction.lower() == "quit":
        key = 0
        done = True
    else:
        if direction.lower() == "q":
            key = 0
            done = True
        else:
            print("invalid input.")
            print("----------")
    # -------------------------------------------------------------
    # -------------------------------------------------------------
    correct = 0
    while not done:
        # Room 1 - Science Room ------------------------------------------------------------------------------------
        if current_room == 1:
            print("\033[0;32m~~~~~~~~~~~~~~~~~\n")
            print("This is the science room. Good Luck!")
            # Question 1 -----------------------------------------------------------------------------
            quest1 = input("1.) What is the most basic unit of life? ")
            if quest1.lower() == "cell":
                print("   - Great Job!")
            elif quest1.lower() == "cells":
                print("   - Great Job!")
            else:
                print("   - That was wrong. The answer is cells. Now you have to start over.")
                print("============================")
                current_room = 0
                key = 0
                break
            # Question 2 -----------------------------------------------------------------------------
            quest2 = input("2.) Does sound travel faster in the air or in water? ")
            if quest2.lower() == "water":
                print("   - Great Job!")
            else:
                print("   - That was wrong. It was water.")
                print("============================")
                current_room = 0
                key = 0
                break
            # Question 3 -----------------------------------------------------------------------------
            quest3 = input("3.) What is the main gas that makes up the Earth's atmosphere? ")
            if quest3.lower() == "nitrogen":
                print("   - Great Job!")
                current_room = 2
            elif quest3.lower() == "n":
                print("   - Great Job!")
                current_room = 2
            else:
                print("   - That was wrong. It was Nitrogen")
                print("============================")
                current_room = 0
                key = 0
                break
        # Room 2 - Science Test ------------------------------------------------------------------------------------
        elif current_room == 2:
            print("\033[0;31m~~~~~~~~~~~~~~~~~\n")
            print("This is where you take your science test. Don't get any wrong!!")
            print()
            # Question 1 -----------------------------------------------------------------------------
            quest1 = input("1.) What is the name of the tallest grass on earth? ")
            if quest1.lower() == "bamboo":
                print("   - Great Job!")
            else:
                print("   - That was wrong. It was bamboo. Now you have to start over.")
                print("============================")
                current_room = 0
                key = 0
                break
            # Question 2 -----------------------------------------------------------------------------
            quest2 = input("2.) How many bones do sharks have in their bodies? ")
            if quest2.lower() == "none":
                print("   - Great Job!")
            elif quest2.lower() == "0":
                print("   - Great Job!")
            else:
                print("   - That was wrong. There are no bones in their bodies. They have powerful, flexible cartilage")
                print("============================")
                current_room = 0
                key = 0
                break
            # Question 3 -----------------------------------------------------------------------------
            quest3 = input("3.) What is the rarest blood type in humans? ")
            if quest3.lower() == "ab negative":
                print("   - Great Job! Back to the starting room - Just so you don't have to answer Room 1's questions "
                      "again. You're welcome.")
                key += 1
                current_room = 0
            else:
                print("   - That was wrong. The answer is AB Negative.")
                print("============================")
                current_room = 0
                key = 0
                break
        # Room 3 - English Room --------------------------------------------------------------------------------------
        elif current_room == 3:
            print("\033[0;35m~~~~~~~~~~~~~~~~~\n")
            print("This is the English Room. Good Luck! Don't Fail.")
            print()
            # Question 1 -----------------------------------------------------------------------------
            quest1 = input("1.) How many syllables are put in the first line of a Haiku? ")
            if quest1 == "5":
                print("   - Great Job!")
            elif quest1.lower() == "five":
                print("   - Great Job!")
            else:
                print("   - That was wrong. There are 5 syllables in the first line of a Haiku!")
                print("============================")
                current_room = 0
                key = 0
                break
            # Question 2 -----------------------------------------------------------------------------
            quest2 = input("2.) Which type of figurative language requires the use of 'like' or 'as'? ")
            if quest2.lower() == "simile":
                print("   - Great Job!")
            else:
                print("   - That was wrong. Similes compare 2 things using like or as.")
                print("============================")
                current_room = 0
                key = 0
                break
            # Question 3 -----------------------------------------------------------------------------
            quest3 = input("3.) In the play Romeo and Juliet, who, actually, died first: Romeo or Juliet? ")
            if quest3.lower() == "romeo":
                print("   - Great Job!")
                current_room = 4
            else:
                print("   - That was wrong. Romeo is the correct answer. Juliet faked her death --> Romeo killed "
                      "himself --> Juliet actually dies after seeing a dead Romeo.")
                print("============================")
                current_room = 0
                key = 0
                break
        # Room 4 - English Test --------------------------------------------------------------------------------------
        elif current_room == 4:
            print("\033[1;37m~~~~~~~~~~~~~~~~~\n")
            print("This is the English Test! Tip: Don't Fail.")
            print()
            # Question 1 -----------------------------------------------------------------------------
            quest1 = input("1.) True or False: A myth teaches a lesson. ")
            if quest1.lower() == "false":
                print("   - Great Job!")
            else:
                print("   - That was wrong. It was false. Legends have lessons, not myths.")
                print("============================")
                current_room = 0
                key = 0
                break
            # Question 2 -----------------------------------------------------------------------------
            quest2 = input("2.) When talking about the school after High School, is it spelled college or collage? ")
            if quest2.lower() == "college":
                print("   - Great Job!")
            elif quest2.lower() == "e":
                print("   - Great Job!")
            else:
                print("   - That was wrong. Collage, with an A, is an art technique while college with an E is the "
                      "place.")
                print("============================")
                current_room = 0
                key = 0
                break
            # Question 3 -----------------------------------------------------------------------------
            quest3 = input("3.) The most commonly used letter from the English alphabet is ____________ ")
            if quest3.lower() == "e":
                print("   - Great Job!")
                current_room = 5
            else:
                print("   - That was wrong. E is the most common letter.")
                print("============================")
                current_room = 0
                key = 0
                break
        # Room 5 - Random Trivia --------------------------------------------------------------------------------------
        elif current_room == 5:
            print("\033[0;32m~~~~~~~~~~~~~~~~~\n")
            print("This is just Random Trivia. Do you're best")
            print()
            # Question 1
            quest1 = input("1.) Which continent is closest to Antarctica? ")
            if quest1.lower() == "south america":
                print("   - Great Job!")
            else:
                print("   - That was wrong. South America is the closest continent.")
                print("============================")
                current_room = 0
                key = 0
                break
            # Question 2
            quest2 = input("2.) The chinese zodiac for 2022 is a(n) ______ ")
            if quest2.lower() == "tiger":
                print("   - Great Job!")
            else:
                print("   - That was wrong. 2022 is the year of the Tiger! ")
                print("============================")
                current_room = 0
                key = 0
                break
            # Question 3
            quest3 = input("3.) Which mammal spends most of its day sleeping? ")
            if quest3.lower() == "sloth":
                print("   - Great Job!")
                current_room = 6
            elif quest3.lower() == "sloths":
                print("   - Great Job!")
                current_room = 6
            else:
                print("   - That was wrong. Sloths were the correct answer.")
                print("============================")
                current_room = 0
                key = 0
                break
        # Room 6 - Math Room ----------------------------------------------------------------------------------------
        elif current_room == 6:
            print("\033[0;31m~~~~~~~~~~~~~~~~~\n")
            print("This is the math room.")
            print()
            # Question 1 -----------------------------------------------------------------------------
            quest1 = input("1.) What is the only even prime number? ")
            if quest1 == "2":
                print("   - Great Job!")
            elif quest1.lower() == "two":
                print("   - Great Job!")
            else:
                print("   - That was wrong. 2 is the only even prime number. Any other even number is divisible by 2.")
                print("============================")
                current_room = 0
                key = 0
                break
            # Question 2 -----------------------------------------------------------------------------
            quest2 = input("2.) 100 + 500 = ")
            if quest2 == "600":
                print("   - Great Job!")
            elif quest2.lower() == "six hundred":
                print("   - Great Job!")
            else:
                print("   - That was wrong. It was 600. (This is one of the easiest questions on this game, and you "
                      "got it wrong! Let's hope it was just a typo.")
                print("============================")
                current_room = 0
                key = 0
                break
            # Question 3 -----------------------------------------------------------------------------
            quest3 = input("3.) (4)(2)+(6-4)-9+5 = ")
            if quest3 == "6":
                print("   - Great Job!")
                current_room = 7
            elif quest3.lower() == "six":
                print("   - Great Job!")
                current_room = 7
            else:
                print("   - That was wrong. It was six.")
                print("============================")
                current_room = 0
                key = 0
                break
        # Room 7 - Math Test ----------------------------------------------------------------------------------------
        elif current_room == 7:
            print("\033[0;34m~~~~~~~~~~~~~~~~~\n")
            print("This is where you take your math test.")
            print()
            # Question 1 --------------------------------------
            quest1 = input("1.) How many millimeters are in a meter? ")
            if quest1 == "1000":
                print("   - Great Job!")
            elif quest1.lower() == "one thousand":
                print("   - Great Job!")
            elif quest1.lower() == "1 thousand":
                print("   - Great Job!")
            else:
                print("   - That was wrong. Now you have to start over.")
                print("============================")
                current_room = 0
                key = 0
                break
            # Question 2 --------------------------------------
            quest2 = input("2.) Right angles measure _________ degrees ")
            if quest2.lower() == "90":
                print("   - Great Job!")
            elif quest2.lower() == "ninety":
                print("   - Great Job!")
            else:
                print("   - That was wrong. Now you have to start over.")
                print("============================")
                current_room = 0
                key = 0
                break
            # Question 3 --------------------------------------
            quest3 = input("3.) A circle is a polygon. True or False ")
            if quest3.lower() == "false":
                print("   - Great Job! A polygon requires a shape to have straight lines. A circle is curved - without "
                      "straight lines")
                current_room = 8
            elif quest3.lower() == "no":
                print("   - Great Job!")
                current_room = 8
            else:
                print("   - That was wrong. A polygon requires a shape to have straight lines. A circle is curved - "
                      "without straight lines")
                print("============================")
                current_room = 0
                key = 0
                break
        # Room 8 - History Room ---------------------------------------------------------------------------------------
        elif current_room == 8:
            print("\033[0;37m~~~~~~~~~~~~~~~~~\n")
            print("You are in the History Room. Time to remember the past. ")
            print()
            # Question 1 --------------------------------------
            quest1 = input("1.) The United States bought Alaska from which country? ")
            if quest1.lower() == "russia":
                print("   - Great Job!")
            else:
                print("   - That was wrong. It was Russia!")
                print("============================")
                current_room = 0
                key = 0
                break
            # Question 2 --------------------------------------
            quest2 = input("2.) Who was the 4th president of the USA? ")
            if quest2.lower() == "james madison":
                print("   - Great Job!")
            elif quest2.lower() == "james":
                print("   - Great Job!")
            elif quest2.lower() == "madison":
                print("   - Great Job!")
            else:
                print("   - That was wrong. It was James Madison. ")
                print("============================")
                current_room = 0
                key = 0
                break
            # Question 3 --------------------------------------
            quest3 = input("3.) What year was the Declaration of Independence signed? ")
            if quest3.lower() == "1776":
                print("   - Great Job!")
                current_room = 9
            else:
                print("   - That was wrong. It was in 1776")
                print("============================")
                current_room = 0
                key = 0
                break
        # Room 9 - History Test -------------------------------------------------------------------------------------
        elif current_room == 9:
            print("\033[0;33m~~~~~~~~~~~~~~~~~\n")
            print("You are going to take the History Test. Time to remember the past, again.")
            print()
            # Question 1 --------------------------------------
            quest1 = input("1.) What year was Pluto downgraded to a dwarf planet? ")
            if quest1 == "2006":
                print("   - Great Job!")
            else:
                print("   - That was wrong. It was in 2006, specifically on Aug. 24, 2006!")
                print("============================")
                current_room = 0
                key = 0
                break
            # Question 2 --------------------------------------
            quest2 = input("2.) How many days in a week were there in ancient Roman times? ")
            if quest2 == "8":
                print("   - Great Job!")
            elif quest2.lower() == "eight":
                print("   - Great Job!")
            else:
                print("   - That was wrong. There were 8 days in one week! Would that mean more school for them?")
                print("============================")
                current_room = 0
                key = 0
                break
            # Question 3 --------------------------------------
            quest3 = input("3.) How many U.S. presidents have been assassinated, as of 2022? ")
            if quest3 == "4":
                print("   - Great Job! 4 presidents have been assassinated as of 2022: Abraham Lincoln, James A. "
                      "Garfield, William McKinley, John F. Kennedy")
                current_room = 10
            elif quest3.lower() == "four":
                print("   - Great Job! 4 presidents have been assassinated as of 2022: Abraham Lincoln, James A. "
                      "Garfield, William McKinley, John F. Kennedy")
                current_room = 10
            else:
                print("   - That was wrong. 4 presidents have been assassinated as of 2022: Abraham Lincoln, James A. "
                      "Garfield, William McKinley, John F. Kennedy")
                print("============================")
                current_room = 0
                key = 0
                break
        # Room 10 - Final --------------------------------------------------------------------------------------------
        elif current_room == 10:
            print("\033[0;36m~~~~~~~~~~~~~~~~~\n")
            print("This is your final. Don't Mess Up! This is way harder than school. This is a test on the "
                  "inspiration of this game.")
            print()
            # Question 1 --------------------------------------
            final1 = input("1.) What game did this layout come from? ")
            if final1.lower() == "zelda":
                print("   - Great Job!")
            elif final1.lower() == "link":
                print("   - I'll accept it. It was The Legend of Zelda, but Link is also correct as there have been "
                      "many other video games with Link as the title. ")
            elif final1.lower() == "legend of zelda":
                print("   - Great Job!!")
            elif final1.lower() == "the legend of zelda":
                print("   - Great Job!!")
            else:
                print("   - That was wrong. The Legend of Zelda is what I based this game off of.")
                print("============================")
                current_room = 0
                key = 0
                break
            # Question 2 --------------------------------------
            final2 = input("2.) Which quest number did the layout of the map come from? (haha, not giving you the "
                           "amount of quests there are!) ")
            if final2 == "2":
                print("   - Great Job!!")
            elif final2.lower() == "two":
                print("   - Great Job!!")
            else:
                print("   - Nope, that wasn't the answer. It was based off of quest 2.")
                print("============================")
                current_room = 0
                key = 0
                break
            # Question 3 --------------------------------------
            final3 = input("3.) Which labyrinth number did the layout of the map come from? (haha, not giving you the "
                           "amount of labyrinths there are!) ")
            if final3.lower() == "5":
                print("   - Great Job!!")
                current_room = 11
            elif final3.lower() == "five":
                print("   - Great Job!!")
                current_room = 11
            else:
                print("   - Nope, that wasn't the answer. It was based off of labyrinth 5.")
                print("============================")
                current_room = 0
                key = 0
                break
        # Room 11 - Trifore!! -----------------------------------------------------------------------------------------
        elif current_room == 11:
            print("\033[1;36m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            print("Congratulations!! You made it through the labyrinth!")
            print("     - You have received a piece of the triforce, now find labyrinth 2. I doubt you can find it "
                  "without help from an old man.")
            key = 0
            done = True
        else:
            print("============================")
            current_room = 0
            key = 0
            break
print("Thanks for playing!!")
print("Unless, you looked an answer up. Then, you get nothing.")
