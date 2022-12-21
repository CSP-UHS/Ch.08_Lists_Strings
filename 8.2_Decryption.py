"""
DECRYPTION PROGRAM
------------------
An ENCRYPTION program was used to generate the following secret code. The encryption program converted each character
of the string into its ASCII decimal number, applied a +/-20 algorithm to it and then converted it back to
characters. Your task is to write a DECRYPTION program to decipher the following secret code. Don't waste time changing
your program 40 times. Use a FOR loop from -20 to +20 to generate all the possibilities in one run of your program.

Extra Challenge: Instead of printing out 41 lines of text to look at, can you determine a way to just print out the
decrypted line only
along with the shift number?
"""
print()
S_M = "Lxwp{j}~uj}rxw|*)bx~)l{jltnm)}qn)lxmn7)]qn)ox{ln)r|)\][XWP)r}q)x~*"
for i in range(-20, 20, 1):
    s = 0
    decrypted = ''
    for c in S_M:
        x = ord(c)
        x += i
        c2 = chr(x)
        if c2 == " ":
            s += 1
        decrypted += c2
    if s > 2:
        print(str(i), " "+decrypted)
