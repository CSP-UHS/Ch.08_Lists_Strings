'''
MONTHS PROGRAM
--------------
Write a user-input statement where a user enters a month number 1-12.
Using the starting string below in your program, print the three month abbreviation 
for the month number that the user enters. Keep repeating this until the user enters a non 1-12 number to quit.
Once the user quits, print "Goodbye!"

months = "JanFebMarAprMayJunJulAugSepOctNovDec"

'''

x = 1
while x > 0:
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"
    string = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    num = int(input("Please enter a number: "))

    print(months[(num*3)-3:(num*3)])

    if 0 > num or 12 < num:
        print("Goodbye")
        x -= 1