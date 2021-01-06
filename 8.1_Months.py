'''
MONTHS PROGRAM
--------------
Write a user-input statement where a user enters a month number 1-12.
Using the starting string below in your program, print the three month abbreviation 
for the month number that the user enters. Keep repeating this until the user enters a non 1-12 number to quit.
Once the user quits, print "Goodbye!"

months = "JanFebMarAprMayJunJulAugSepOctNovDec"

'''
months = "JanFebMarAprMayJunJulAugSepOctNovDec"

kane = False

while not kane:
    user_inp = int(input("name"))
    if user_inp == 13:
        kane = True
        break
    start = (user_inp-1)*3
    end = start+3
    print(months[start:end])
