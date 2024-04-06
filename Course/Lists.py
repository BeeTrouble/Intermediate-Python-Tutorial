## Lists


mylist1 = ["banana", "cherry", "apple"]
print(mylist1)

mylist2 = [5, True, "apple", "apple"]
print(mylist2)

item = mylist1[0]
print(item)

item = mylist1[2]
print(item)

item = mylist1[-1]
print(item)

for i in mylist1:
    print(i)

if "banana" in mylist1:
    print("yes")
else: 
    print("no")

print(len(mylist1))


mylist1.append("lemon")
print(mylist1)


mylist1.insert(1, "blueberry")
print(mylist1)


item = mylist1.pop()
print(item)
print(mylist1)


item = mylist1.remove("cherry")

print(mylist1)


item = mylist1.reverse()

print(mylist1)


mylist3 = [4, 3, 57, -9, -200]

item = mylist3.sort()

print(mylist3)


mylist4 = [4, 3, 57, -9, -200]

new_list = sorted(mylist4)
print(mylist4)
print(new_list)


mylist5 = [0] * 5
print(mylist5)


mylist6 = [1, 2, 3, 4, 5]

new_list2 = mylist5 + mylist6
print(new_list2)


mylist7 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

a1 = mylist7[1:5]
print(a1)

a2 = mylist7[::2]
print(a2)

a3 = mylist7[::-1]
print(a3)


list_org1 = ["banana", "cherry", "apple"]

list_cpy1 = list_org1

print(list_cpy1)


list_org2 = ["banana", "cherry", "apple"]

list_cpy2 = list_org2.copy()

list_cpy2.append("lemon")

print(list_cpy2)
print(list_org2)


list_org3 = ["banana", "cherry", "apple", "orange"]

list_cpy3 = list(list_org3)

list_cpy3.append("lemon")

print(list_cpy3)
print(list_org3)


list_org4 = ["banana", "cherry", "apple", "orange", "grape"]

list_cpy4 = list_org4[:]

list_cpy4.append("lemon")

print(list_cpy4)
print(list_org4)


mylist8 = [1, 2, 3, 4, 5, 6]
b = [x*x for x in mylist8]

print(mylist8)
print(b)
