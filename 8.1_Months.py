'''
MONTHS PROGRAM
--------------
Write a user-input statement where a user enters a month number 1-13.
Using the starting string below in your program, print the three month abbreviation 
for the month number that the user enters. Keep repeating this until the user enters 13 to quit.
Once the user quits, print "Goodbye!"

months = "JanFebMarAprMayJunJulAugSepOctNovDec"

'''
q=False
months="JanFebMarAprMayJunJulAugSepOctNovDec"
while q==False:
    i=int(input("What month # do you want?(13 to quit)"))
    if i==13:
       break
    else:
        print(months[(i*3-3):(i*3)])
print("Goodbye!")