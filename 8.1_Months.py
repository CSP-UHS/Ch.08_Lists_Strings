'''
MONTHS PROGRAM
--------------
Write a user-input statement where a user enters a month number 1-12.
Using the starting string below in your program, print the three month abbreviation 
for the month number that the user enters. Keep repeating this until the user enters a non 1-12 number to quit.
Once the user quits, print "Goodbye!"

months = "JanFebMarAprMayJunJulAugSepOctNovDec"

months = "JanFebMarAprMayJunJulAugSepOctNovDec"

print("Please select a month that you want the name for using the 1 - 12")
first = int(last - 3)
last = usernum
usernum = int(input("What is your number"))
month = [first:last]

num = input("What is your number? (1 - 12)")

last = int(num * 3)
first = int(last - 3)

print(first, last)
'''
months = "JanFebMarAprMayJunJulAugSepOctNovDec"
done = False
while not done:
    usermonth = int(input("What is your number? (1 - 12)"))
    q = str(input("Is this all you need?"))
    print[first:last]
    if q == 'Y':
        done = True