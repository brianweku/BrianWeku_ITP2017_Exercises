#4-10
#example
#4-1
pizza=['Pepperoni', 'Sausage', 'Mushroom', 'Onion', 'Meat Lovers']
for i in pizza:
    print(i)

for i in pizza:
    print("I love "+ i +" pizza.")

print("I really love pizza!")

print("The first three items in the list are:", pizza[0:3])
print("Three items in the middle of the list are:", pizza[1:4])
print("The last three items in the list are:", pizza[-3:])

#4-11
pizza=['Pepperoni', 'Sausage', 'Mushroom', 'Onion', 'Meat Lovers']
friend_pizzas=pizza[:]
pizza.append('Mayo')
friend_pizzas.append('Cheese')
print("My favorite pizzas are:")
for i in pizza:
    print(i)
print("My friend's favorite pizzas are:")
for i in friend_pizzas:
    print(i)

#4-12
my_foods = ['pizza', 'falafel', 'carrot cake']
for i in my_foods:
    print(i)
for i in my_foods:
    print(i, end=', ')
