#3-4
arr=['jokowi', 'obama', 'bagus']
for i in range (3):
    print(arr[i] + ", you are invited to dinner!")

#3-5
x=arr.pop(0)
print(x+" can't come:(")
arr.append('aldi')
print(arr[2]+ ", you are invited to dinner!")
for i in range (3):
    print(arr[i] + ", you are invited to dinner!")

#3-6
print("i found a biger table, yay")
arr.insert(0, 'mark')
arr.insert(2, 'john')
arr.append('john')
for i in range (6):
    print(arr[i] + ", you are invited to dinner!")

#3-7
print("I'm sorry but i can only invite 2 people right now")
message=", there is a problem with the table so i need to cancel my invitation."
for i in range (4):
    print(arr[-1]+message)
    arr.pop()
for i in range (2):
    print(arr[i]+", there is no changes you are still invited")

for i in range(2):
    del arr[0]
print(arr)
