twitch_friends = ["alex", "greg", "danz", "ridley"]
print (twitch_friends[:])

lucky_numbers = [23, 52, 6, 13]
print (lucky_numbers[:])

print (twitch_friends)

#twitch_friends.extend(lucky_numbers)
twitch_friends.append('ren')
twitch_friends.insert(3, "kelly")
twitch_friends.remove('kelly')
#twitch_friends.clear()
twitch_friends.pop()
twitch_friends.sort()
twitch_friends.reverse()

new_twitch_friends = twitch_friends.copy()
#print (twitch_friends)
#print (twitch_friends.index('greg'))

#print (lucky_numbers)

### end of list

def hello():
    print('hello world')

#hello()

def sayhelloto():
    name = input("what is your name")
    print("your name is " + name)


sayhelloto()

def sayhelloto2(name):
    print("your name is " + name)

sayhelloto2("greg")
sayhelloto2("ben")

def sayhelloto3(name, age):
    print("your name is " + name + "\n your age is " + str(age))


sayhelloto3("BrianMakes", 25)

def cube(num):
    return num*num*num


print(cube(4))

is_awesome = True
is_cool = False

if is_cool or is_awesome:
    print('you are awesome and cool or both')
else:
    print('you are neither awesome or cool')


is_male = False
is_tall = False

if is_male and is_tall:
    print('you are male and tall')
elif is_male and not(is_tall):
    print('you are not tall')
elif not(is_male) and is_tall:
    print('you are not male but tall')
else:
    print('you are neither male or tall')