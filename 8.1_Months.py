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
num = 1
while True:
    if num < 1 or num > 12:
        break
    else:
        num = int(input('Please Enter a month number: ')) - 1
        print(months[num * 3:num * 3 + 3])

print('Goodbye!')