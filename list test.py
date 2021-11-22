#Lists, mutable
#empty list favoritenumbers=[]
leastfavoritenums=[13,"OK",69,2.1,[1,2,3]]
#print(leastfavoritenums[1])
#print(len(leastfavoritenums))
#for item in leastfavoritenums: not index number
    #print(item)
#for i in range(len(leastfavoritenums)): index numbah
    #print(i)
#leastfavoritenums.append(9)
#Tuples, immutable
#empty tuple othernumbers=()
#lesserfavnums=(11,9,55)
import random
my_list=[]
#for i in range(1,101):
    #my_list.append(i)
#print( my_list)

for i in range(100):
    my_list.append(random.randint(0,100))
print (my_list)