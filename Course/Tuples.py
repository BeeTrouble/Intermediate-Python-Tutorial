## Tuples

mytuple1 = ("Max", 28, "Boston")
print(mytuple1)


mytuple2 = "Max", 28, "Boston"
print(mytuple2)


mytuple3 = ("Max")
print(type(mytuple3))


mytuple4 = ("Max",)
print(type(mytuple4))


mytuple5 = tuple(["Max", 28, "Boston"])
print(mytuple5)

item = mytuple5[0]
print (item)

# mytuple5[0] = "Tim"

for i in mytuple5:
    print(i)


if "Max" in mytuple5:
    print("yes")
else:
    print("no")

if "Tim" in mytuple5:
    print("yes")
else:
    print("no")

my_tuple1 = ('a', 'p', 'p', 'l', 'e')

print(len(my_tuple1))
print(my_tuple1.count('l'))
print(my_tuple1.index('p'))

my_list1 = list (my_tuple1)
print(my_list1)

my_tuple2 = tuple(my_list1)
print(my_tuple2)

a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

b = a[2:5]
print(b)

c = a[2::2]
print(c)

d = a[2::-1]
print(d)

my_tuple3 = "Max", 38, "Boston"

name, age, city = my_tuple3
print(name)
print(age)
print(city)


my_tuple4 = (0, 1, 2, 3, 4)

i1, *i2, i3 = my_tuple4
print(i1)
print(i3)
print(i2)


import sys
my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")


import timeit 
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5,]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5,)", number=1000000))
