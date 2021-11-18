'''
#Lists (mutable)
favorite_numbers = [13, 42, 7]
other_numbers = (10, 66, 79)
my_list= [13, "Marc", 42, 7, 16,[1, 2, 3]]

#print(type(other_numbers))
print(len(my_list))

for item in range(len(my_list)):
    if type(item) == 'list':
        print(item)



#print(type(item))
#print()
#Tuples (immutable)

#print(my_list[0], my_list[1], my_list[2], my_list[3])
my_list2 = [2, 4, 5, 6]
my_list2.append(9)
print(my_list2)
'''
import random
for i in range(10):
    x = random.randrange(100000)
    print(f"My number:{x:,}")
