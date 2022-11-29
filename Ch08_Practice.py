myList = [2, 10, 5, 98]  # [position 0, position 2]
myTuple = (255, 234, 212)
# lists = mutable <-- can change it
# tuples = immutable <-- can't change it (saves processing time)
print(type(myList))
print()  # ----------------
droids = [34, "C3PO", True, [1, 5, 6]]  # <-- remember there is no 3 spot ([position 0, 1, 2])
print(droids[0])
droids[1] = "K2SO"
print(droids)
for item in droids:
    print(item)
print()  # ----------------
print(len(droids))
print()  # ----------------
# if droids is changed to having 4 options, then range(3) must change to range(4)
for i in range(len(droids)):
    print(droids[i])
