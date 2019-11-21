'''
MONTHS PROGRAM
--------------
Write a user-input statement where a user enters a month number 1-13.
Using the starting string below in your program, print the three month abbreviation 
for the month number that the user enters. Keep repeating this until the user enters 13 to quit.
Once the user quits, print "Goodbye!"

months = "JanFebMarAprMayJunJulAugSepOctNovDec"

'''
months = "JanFebMarAprMayJunJulAugSepOctNovDec"
times=0
done=False
while done is False:
    print()
    month = int(input("Pick a number 1-12 for a month or 13 to quit\n"))
    if month==1:
        print("The month you chose abv. is",months[0:3])
        times+=1
    elif month==2:
        print("The month you chose abv. is",months[3:6])
        times += 1
    elif month==3:
        print("The month you chose abv. is",months[6:9])
        times += 1
    elif month==4:
        print("The month you chose abv. is",months[9:12])
        times += 1
    elif month==5:
        print("The month you chose abv. is",months[12:15])
        times+=1
    elif month==6:
        print("The month you chose abv. is",months[15:18])
        times += 1
    elif month==7:
        print("The month you chose abv. is",months[18:21])
        times += 1
    elif month==8:
        print("The month you chose abv. is",months[21:24])
        times += 1
    elif month==9:
        print("The month you chose abv. is",months[24:27])
        times += 1
    elif month==10:
        print("The month you chose abv. is",months[27:30])
        times += 1
    elif month==11:
        print("The month you chose abv. is",months[30:33])
        times+=1
    elif month==12:
        print("The month you chose abv. is",months[33:36])
        times += 1
    else:
        print("You used the program",times,"times!\nThank you for your time.")
        done=True
