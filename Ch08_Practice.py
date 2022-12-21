"""
myList = [2, 10, 5, 98]  # [position 0, position 2]
myTuple = (255, 234, 212)
# lists = mutable <-- can change it
# tuples = immutable <-- can't change it (saves processing time)
print(type(myList))
print()  # ----------------
droids = [34, "C3PO", True, [1, 5, 6]]  # <-- remember there is no 3 spot ([position 0, 1, 2])
print(droids[0])
droids[1] = "K2SO"
print(droids)
for item in droids:
    print(item)
print()  # ----------------
print(len(droids))
print()  # ----------------
# if droids is changed to having 4 options, then range(3) must change to range(4)
for i in range(len(droids)):
    print(droids[i])
print()  # ----------------
print(droids[3][1])
print()  # ----------------
for i in range(len(droids)):
    print(type(droids[i]))
print()  # ----------------
nat_league_top3 = [["Mets", "Nationals", "Braves"], ["Cardinals", "Reds", "Pirates", "Cubs"], ["Dodgers", "Giants",
                                                                                        "Diamondbacks"]]
print(len(nat_league_top3))
print(len(nat_league_top3[1][2]))
nat_league_top3[1][3] = "Losers"
print(nat_league_top3)
print()  # ----------------
nat_league_top3[1].append("Losers")
print(nat_league_top3)
print()  # ----------------
my_list = []
for i in range(5):
    num = int(input("Enter an integer: "))
    my_list.append(num)
print(my_list)
print()  # ---------------
for i in range(len(my_list)):
    my_list[i] += 2
    print(my_list[i])
print(my_list)
print()  # ---------------
uhs_slogan = "My school is the best"
print(type(uhs_slogan))
print(uhs_slogan)
print(uhs_slogan[0])  # This will print the 1st letter of the string
print(len(uhs_slogan))
print(uhs_slogan[-1])  # prints a "t" and doesn't use base 0 ( if it did the answer would be "s"
print(uhs_slogan[0:5])  # prints the first 5 letters <-- [inclusive, inclusive] and won't include h
print(uhs_slogan[17:])  # positive number or
print(uhs_slogan[-4:])  # negative number (gets the same number)
print(uhs_slogan[:13] + "awesome!")  # "sliced" the string and put something else on it
print()  # --------------
for letter in uhs_slogan:
    print(letter)

email = "hermonm@urbandaleschools.com"
username = ""
for letter in email:
    if letter == '@':
        break
    else:
        username += letter
print(username)
print(chr(62))  # ascii symbol for (#)
print()  # --------------------------------------------------------------------------
months = "JanFebMarAprMayJunJulAugSepOctNovDec"
done = False
while not done:
    try:
        yourMonth = int(input("Enter a month using numbers 1 - 12. "))
    except ValueError:
        print("Enter an integer: ")
        continue
    if 0 < yourMonth < 13:
        print(months[yourMonth*3-3:yourMonth*3])
    else:
        break
print()
print("Thanks for playing. Goodbye!")
"""
