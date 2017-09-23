#4-14
#https://python.org/dev/peps/pep-0008


#4-15
#4-6
odd=list(range(1, 21, 2))
for i in odd:
    print(i)

#4-7
threes=list(range(3, 31, 3))
for i in threes:
    print(i)

#4-8
cubes=list(range(1, 11))
for i in cubes:
    print(i**3)

#4-9
cubes = [number**3 for number in range(1,11)]

for cube in cubes:
    print(cube)
