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
number = 1
print("Enter a number between 1 and 12 for the respective month abbreviation.")
print("Enter a different number to exit.")
while 1 <= number <= 12:
    number = int(input("Input: "))
    start = (number - 1 ) * 3
    end = start + 3
    print(months[start:end])
print("Goodbye!")