#5-8
name=['brian', 'admin', 'jessica', 'árden', 'kevin']
for i in name:
    if i == 'admin':
        print("Hello admim, would you like to see a status report?")
    else:
        print("Hello "+ i.title() +", thank you for logging in again.")

#5-9
name=[]
if name:
    for i in name:
        if i == 'admin':
            print("Hello admim, would you like to see a status report?")
        else:
            print("Hello "+ i.title() +", thank you for logging in again.")
else:
    print("We need to find some users!")

#5-10
current_users=['brian', 'andrew', 'jessica', 'árden', 'kevin']
new_users=['brian', 'EVANDER', 'jaSon', 'Jessica', 'shellin']
for i in new_users:
    if i.lower() in current_users:
        print("Sorry "+ i.title()+ ", name is not available")
    else:
        print("Nice, "+ i.title()+ " is available")

#5-11
list=list(range(1, 10))
for i in list:
    print(i)

for i in list:
    if i == 1:
        print("1st")
    if i == 2:
        print("2nd")
    if i == 3:
        print("3rd")
    if i > 3:
        print(str(i)+"th")


