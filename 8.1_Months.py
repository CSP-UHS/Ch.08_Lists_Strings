'''
MONTHS PROGRAM
--------------
Write a user-input statement where a user enters a month number 1-12.
From the user input number, slice the string below in your program to print the three month abbreviation.
Keep repeating this until the user enters a non 1-12 number to quit.
Once the user quits, print "Goodbye!"
'''

months = "JanFebMarAprMayJunJulAugSepOctNovDec"

done=False
while not done:
    try:
        m=int(input("Please Enter a month (1-12)"))
    except ValueError:
        print("Please enter a interager")
        continue

    if 0<m<13:
        print(months[m*3-3:m*3])
    else:
        break
print("Thanks for playing the Months game!")

