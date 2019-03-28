'''
MONTHS PROGRAM
--------------
Write a user-input statement where a user enters a month number 1-13.
Using the starting string below in your program, print the three month abbreviation 
for the month number that the user enters. Keep repeating this until the user enters 13 to quit.
Once the user quits, print "Goodbye!"

months = "JanFebMarAprMayJunJulAugSepOctNovDec"

'''
y = 1
while y == 1:
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Goodbye"]
    print("Put in a number between 1 - 12 to receive the corresponding month, or enter 13 to quit.")
    x = int(input("Enter:"))
    if x < 13:
        print(months[x-1])
    else:
        print(months[12])
        y = 0
