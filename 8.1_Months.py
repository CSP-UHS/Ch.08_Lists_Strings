'''
MONTHS PROGRAM
--------------
Write a user-input statement where a user enters a month number 1-12.
Using the starting string below in your program, print the three month abbreviation 
for the month number that the user enters. Keep repeating this until the user enters a non 1-12 number to quit.
Once the user quits, print "Goodbye!"



'''
months = "JanFebMarAprMayJunJulAugSepOctNovDec"

while 1:
    month = int(input("Enter a number between 1-12: "))
    if month < 1 or month > 12:
        print("goodbye")
        break
    else:
        pos = (month - 1) * 3
        monthz = months[pos:pos+3]
        print("The month abbreviation is ", monthz)