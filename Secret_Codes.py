secret_message = "Hello im alex ;)"
solved_message = ""
encrypted_text = ""
for c in secret_message:
    x = ord(c)
    x = x+1
    c2 = chr(x)
    encrypted_text = encrypted_text + c2
print(encrypted_text)

for c in encrypted_text:
    x = ord(c)
    x = x-1
    c2 = chr(x)
    solved_message = solved_message+ c2
print(solved_message)