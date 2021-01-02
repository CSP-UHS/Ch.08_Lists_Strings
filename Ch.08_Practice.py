#Lists, Tuples, and Strings
#baseball=["Mets", "Braves", "Cardinals", "Dodgers"] List - Mutable
#baseball=("Mets", "Braves", "Cardinals", "Dodgers") Tuples - Immutable
#print(baseball) - prints list
#print(baseball[2]) - prints "Cardinals"
#numbers=[3,4,8,2,9,4,7,4]
#print(numbers[5]) - prints 4
#baseball[1]="Phillies" - changes "Braves" to "Phillies"
#print(baseball)

#for-each
#for team in baseball: - prints everything in list
    #print(team)

#for i in range(4): - prints 0-3 on list
    #print(baseball[i])

#print(len(baseball)) - tells how many items in list

#for i in range(len(baseball)):
    #print(baseball[i]) - prints everything on list

#baseball.append("Rockies") - adds "Rockies"

#x=[1,2,3]
#baseball=("Mets", x, "Cardinals", "Dodgers")
#print(baseball)
#x[2]=24
#print(baseball)

#uhs_slogan="My School is the best"
#print(uhs_slogan[0]) - prints "M"
#print(uhs_slogan[0:3]) - prints first 3 characters "My "
#print(uhs_slogan[:13]+'awesome!') - prints "My School is awesome!"

#import random
#for i in rnage(10):
    #x=random.randrange(120)
    #print(f"My number: {x:3}") - 3 field width