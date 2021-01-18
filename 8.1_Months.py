'''
MONTHS PROGRAM
--------------
Write a user-input statement where a user enters a month number 1-12.
Using the starting string below in your program, print the three month abbreviation 
for the month number that the user enters. Keep repeating this until the user enters a non 1-12 number to quit.
Once the user quits, print "Goodbye!"

months = "JanFebMarAprMayJunJulAugSepOctNovDec"

'''

per = input("enter a month number 1-12: ")

months = ["Jan ","Feb ","Mar ","Apr ","May ","Jun ","Jul ","Aug ","Sep ","Oct ","Nov ","Dec "]

if per == 1:
    print(months[0])

elif per == 2:
    print(months[1])

elif per == 3:
    print(months[2])

elif per == 4:
    print(months[3])

elif per == 5:
    print(months[4])

elif per == 6:
    print(months[5])

elif per == 7:
    print(months[6])

elif per == 8:
    print(months[7])

elif per == 9:
    print(months[8])

elif per == 10:
    print(months[9])

elif per == 11:
    print(months[10])

elif per == 12:
    print(months[11])


