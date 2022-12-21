'''
DECRYPTION PROGRAM
------------------
An ENCRYPTION program was used to generate the following secret code. The encryption program converted each character 
of the string into its ASCII decimal number, applied a +/-20 algorithm to it and then converted it back to
characters. Your task is to write a DECRYPTION program to decipher the following secret code. Don't waste time changing 
your program 40 times. Use a FOR loop from -20 to +20 to generate all the possibilities in one run of your program.

Extra Challenge: Instead of printing out 41 lines of text to look at, can you determine a way to just print out the decrypted line only
along with the shift number?
'''

Secret_Message="Lxwp{j}~uj}rxw|*)bx~)l{jltnm)}qn)lxmn7)]qn)ox{ln)r|)\][XWP)r}q)x~*"

# A list of characters which aren't used in common english writing
uncommonChars = ("@","#","^","*","_","~","`","{","}","[","]","(",")","\\","/","|","<",">")

def findCaesarCipher(msg):
    shiftRange = 20
    for i in range(-shiftRange, shiftRange):
        notSolution = False
        cryptString = ""
        for j in msg:
            newChar = chr(ord(j) + i)  # Shifts character
            cryptString += newChar  # Adds to string
        for k in uncommonChars:
            if k in cryptString:  # Checks if it contains an uncommon character
                notSolution = True  # If it does, this is not the solution
        if notSolution: continue  # If this is not the solution, cycle to the next shift number
        print("Decrypted message : " + cryptString)
        print("Shift : " + str(i))


findCaesarCipher(Secret_Message)
