'''
DECRYPTION PROGRAM
------------------
An encryption program was used to generate the following secret code. The encryption program converted each character 
of the string into its ASCII decimal number, applied a +/-20 algorithm to it and then converted it back to
characters. Your task is to write a Decryption program to decipher the following secret code. Don't waste time changing 
your program 40 times. Use a FOR loop from -20 to +20 to generate all the possibilities in one run of your program.

Secret Message: Lxwp{j}~uj}rxw|*)bx~)l{jltnm)}qn)lxmn7)]qn)ox{ln)r|)\][XWP)r}q)x~*
'''
'''
num=[];count=-1;list=-1
sm="Lxwp{j}~uj}rxw|*)bx~)l{jltnm)}qn)lxmn7)]qn)ox{ln)r|)\][XWP)r}q)x~*"
dm=[]
for item in sm:
    x=ord(item)
    dm.append(x)
print(dm)
for item in dm:
    count+=1
    item-=20
    num.append([])
    for i in range(-20,20,1):
        item+=1
        num[count].append(chr(item))
for item in sm:
    list+=1
    print(num[list])
print("Congratulations! You cracked the code. The force is STRONG with you!")
'''
sm="Lxwp{j}~uj}rxw|*)bx~)l{jltnm)}qn)lxmn7)]qn)ox{ln)r|)\][XWP)r}q)x~*"
for item in range(-20,21,1):
    decrypted_text=""
    for letter in sm:
        num=ord(letter)
        newnum=num+item
        newletter=chr(newnum)
        decrypted_text+=newletter
    print(decrypted_text)
