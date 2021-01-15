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

while True:
    ans=int(input("Please enter a number 1-13: "))
    if 0 < ans < 13:
        print(months[(ans - 1) * 3:((ans - 1) * 3) + 3])
    else:
        print("Goodbye!")
        break
                
