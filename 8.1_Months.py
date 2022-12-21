'''
MONTHS PROGRAM
--------------
Write a user-input statement where a user enters a month number 1-12.
From the user input number, slice the string below in your program to print the three month abbreviation.
Keep repeating this until the user enters a non 1-12 number to quit.
Once the user quits, print "Goodbye!"
'''

months = "JanFebMarAprMayJunJulAugSepOctNovDec"

while True:
    userInput = int(input("Type a month number : "))
    if userInput < 1 or userInput > 12:
        print("Goodbye!")
        break
    print(months[(userInput-1)*3:(userInput-1)*3+3])