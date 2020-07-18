


print ('what is your name ?')
your_name = input()
print ('hello, '+ your_name)
print ("your name's length is : " + str(len(your_name)))

print ('what is your age ? ')
your_age = input()
print ('your age  is : ' + str(your_age))

print("here is a \n this is a new line")
#Backslash n \n introduces another line below the first section of the string
#Backslash quotation marks prints out a quotation mark
print("I love azure\" so much!")
#To print out a normal backslash in a code
print("Ya hi\john")

#CREATING A STRING VARIABLE
phrase = "Hello Twitch folks"
print(phrase)
#CONCATENATION - Taking a string and appending it in another string
print(phrase + " and is cool and i like it that way")

#Using of special things called functions - a block of code that w e can run to perform a specific operation
print(phrase.lower()) #converts phrase into lower case
print(phrase.upper()) #converts phrase into upper case
#Using function to check whether its true or false...you use isupper() or islower()
print(phrase.isupper())
print(phrase.islower())
#Using functions in combination with each other
print(phrase.upper().isupper())
print(phrase.lower().islower())
#Figuring out the length of a string
print(len(phrase))
#Grabbing a single character from a string/A string get indexed starting with zero
print(phrase[0])
#The index function- tells us where a specific character or a string is located inside of a string
print(phrase.index("o"))
print(phrase.index("love"))  #If you put a letter that is not in the string then it will return an error
#Replace function
print(phrase.replace("word", "word2"))

import pyperclip
pyperclip.copy('hello world!')
pyperclip.paste()

from math import *  #This is called math module

print(3)
print(6//2) #Does not give decimals
print(3 + 4)
print(5/2) #Gives decimals
print(4*5)
print(10%3) #This gives us the remainder. This is called modulus operator


#Storing numbers in variables
my_num = 5
print(my_num)

#I can convert my_num into string
print(str(my_num))
print(str(my_num) + " is my favorite number!")


#Absolute value of a number
my_num = -5
print(abs(my_num))


#Power function allows us to pass two pieces of information. The first value is a number and the second is the power in which is needs to be raised to
print(pow(3, 3))
#Max number
print(max(9,11,34,78,3,5,45,7))
#Min number
print(min(9,11,34,78,3,5,45,7))
#Rounding off
print(round(3.27))
print(round(3.67))

#Some functions need you to import external code into our file. To access them, we exportpython math
#The floor method can only be accessed by importing math. It chops off the decimal part of the number
print(floor(4.91))
#ceil function rounds the number up no matter what
print(ceil(3.1))
#sqrt is squareroot method
print(sqrt(31))

num_1 = input("Enter a number: ")
num_2 = input("Enter another number: ")
#Note that whatever input is got from the user is converted into a string by default.
#Therefore, we need to convert the strings that we get from a user into numbers using either int
#However, int won't work for decimals. Float is just basically a number that has decimals.
#sum = int(num_1) + int(num_2)
sum = float(num_1) + float(num_2)
print(sum)

#Open and closed square blackets are used to create lists
friends = ["Ali", "Beck", "James", "Meem", "Forty"]
print(friends[0+3])


'''
print(friends[1:])
print(friends[1:3])
friends[3] = "Habibi"
print(friends)
'''

lucky_number = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]


print(friends)
#Extend fubction allows you to take a list and append another list unto the end of it
friends.extend(lucky_number)
print(friends)
#Adding individual objects unto a list (at the end of the list)
friends.append("creed")
print(friends)
#Appends adds something at the end of the list
#If you want to add something at the middle of the list,you use insert function, it takes two parameters
friends.insert(1, "Kelly")
print(friends)
#To remove objects
friends.remove("Kelly")
print(friends)
#clear function removes all list parameters
#friends.clear()
print(friends)  #prints an empty list
#pop function pops an item off the list. It removes the last element in the list
friends.pop()
print(friends)
print(friends.index("Kevin"))

friends = ["Kevin", "Karen", "Jim", "Oscar", "Karen", "Toby", "Adam", "Sarah", "Anonymous", "Karen"]
print(friends. count("Karen"))

#sorting in ascending order
friends.sort()
print(friends)

#Sorting in descending order
friends.reverse()
print(friends)

#Making a copy of the list
friends_2 = friends.copy()
print(friends_2)

#Function is a collection of code that performs a specific task
#Help organize and break your code into different little chuncks that do different things
#Let create a function that says his to the user
#key word def is used and then the name of the function
#Parameter is a piece of information that we give to the function
#Parameters are entered inside the bracked of the def name

#def say_hi():    #This means that all the code that comes below this line is inside our function
#    name = input("Hi, what is your name: ")
#    print("Hello " + name + "!")
#say_hi() #This is calling the function

#def sayhi(name):
#    print("Hello " + name +  "!")
#sayhi("Mike") #mike was passed on here
#sayhi("Steve")

#You can put as many parameters as you may like
#def say_hi(name, age):
#    print("Hello " + name + "! You are " + age + " years old.")
#say_hi("Mike", "26")
#say_hi("Steve", "28")

def say_hi(name, age):
    print("Hello " + name + "! You are " + str(age) + " years old.")
say_hi("Mike", 26)
say_hi("Steve", 28)

def cube(num):
    return num*num*num #without the retrun statement the function cannot work whatsoever
#no code can be put after the return statement, it won't run anyway
result = cube(4)
print(result)

#If statements are used to help a programme make decisions(Conditions: or, and, else if (elif))
is_male = False
is_tall = True
#if is_male or is_tall: #using or operator
#    print("You are male or tall or both")
#else:
#    print("You are neither male not tall")

################### using and

if is_male and is_tall:
    print("Ypu are a tall male")
elif is_male and not(is_tall):#else if
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but tall")
else:
    print("You are not a male and not tall")

def max_num(num1, num2, num3): #We are passing in three numbers and the function will return the largest of the three
   if num1 >= num2 and num1 >= num3: #comparison operators /double == means equal and != means not equal
       return num1
   elif num2 >= num1 and num2 >= num3:
       return num2
   else:
       return num3
print(max_num(4, 18, 2))

#This is a special structure in python which allows us to store information in key value pairs.
#Can be used to do things like converting Jan to January
#The first step is to give the dictionary a name
#We use curly brackets to create dictionaries in python
#Inside the curly brackets we put key value pairs
#Three letter is the key and the other section is the value
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}
print(monthConversions["Nov"]) #also i can access it by:
#print(monthConversions.get("Lob")) #This is the best because if you put something not in the dictionary it returns none instead of an error
#.get also gives us a fallback value that we can get back to if the input is invalid instead of none
print(monthConversions.get("Luv", "Not a valid key!"))
#The keys don't have to be strings, they can also be numbers


#Loops through a block of code, executing it multiple times.
i = 1
while i <= 10:
    print(i)
    i += 1 #also written as i = i + 1
print("Done with loop")


#Helps us loop over different collections of items
#Mostly used to loop through array, letters inside a string, or loop through series of numbers
for letter in "I will make it alhamdulillah":
    print(letter)
for index in range(3):
    if index == 0:
        print("First itineration")
    else:
        print("Not first itineration")


import os

current_dir = os.getcwd('/home/cgh2/demo.txt')
change_dir = os.chdir('/home/cgh3')
new_dir = os.mkdir('/home/cgh4')

print (f'current_dir : {current_dir}')
print (f'change_dir : {change_dir}')
print (f'new_dir:{new_dir}')

import os

for  root, subfolders, files in os.walk('./'):
    print (root)
    for subfolder in subfolders:
        print (subfolder)
    for file in files:
        print (file)

