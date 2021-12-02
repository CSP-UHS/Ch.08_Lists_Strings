#lists(mutable)
#favoritenumbers = [13, 42, 7]
#tuples(immutable)
#othernumbers = (10, 66, 79)
'''
my_list = [13, "Marc",42.0, 7]
for i in my_list:
    if type(i)=='tuple':
        print(i)
    print(i)
    print(type(i))
    print()




my_list = []

for i in range(1,101):
    my_list.append(i)
'''

my_list=[5,6,2,4,0,9]

#for i in range(len(my_list)):
 #   print(my_list[i])

for item in my_list:
    print(item)

for i in range(len(my_list)):
    my_list[i]*=10

print(my_list)