'''
MONTHS PROGRAM
--------------
Write a user-input statement where a user enters a month number 1-12.
Using the starting string below in your program, print the three month abbreviation 
for the month number that the user enters. Keep repeating this until the user enters a non 1-12 number to quit.
Once the user quits, print "Goodbye!"

months = "JanFebMarAprMayJunJulAugSepOctNovDec"

'''
go = False
months = "JanFebMarAprMayJunJulAugSepOctNovDec"
while go == False:
    num = int(input("Choose a number between 1-12.:  "))
    if num >= 1 and num <= 12:
        print(months[(num*3)-3:(num*3)])
    else:
        print("Goodbye")
        go = True