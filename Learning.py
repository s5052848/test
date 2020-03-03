#Importing
import os
os.system('clear')
####################
#Data Types
####################
print ("FINALLY from desktop!!!! Hello World!")
Credit = "by Hashim" #how to do string variable. It can be overwritten
age = 23 # number variable example
count = [1,2,3,4] #list example
names = ("Hashim", "Basle")#tuple example
print (Credit)
print(count[3])
print (names)
fav_color = {
	"Hashim": "Orange",
	"Basle" : "Blue"
}#Dictionary example key:variable
print (fav_color["Hashim"])# returns hashim's favorite color
###################
#Strings
###################
boss = 'My boss yelled "GET BACK TO WORK!"'# Works the other way around as well to include single quotes 
boss2 = "My boss yelled \n\"GET BACK TO WORK!\""#the escape character "\" can also be used before a value or symbol that means something

print (boss2)

#Concantinating

Name = "Hashim"
greetings = "Hello my name is: " + Name
#print (greetings + Name) # only works for two of the same data type.

#functions for strings
print (greetings.upper()) # upper was added to make all leter uppercase
print (len(greetings)) #counts letters
print (greetings[12]) #prints a certain letter
print (greetings [18:24])#prints the range of letters in greetings
print (greetings.split(" ")[4])#Splits everything seperated by a space in greetings and turns them into a list adding [] allows to print a piece of yhe list made
###################
#Numbers and Math
###################
num = 10
print (float(num))#the int num is turned into a float
#works the other way as well
num2 = 10.25
print (int(num2))#the float has turned to an  int
print(int(5/2))#this is how to convert the result
#################
#LISTS
#################
ages = [23, 19, 40, 50, 23]
namesl = ["Hashim", "Basle", "Mona", "Mofeed", ages]#list
namesl.append("Tohotmoss")# To add tohotmoss to the list
#namesl[0] = "Tohotmoss" #changes Hashim to Tohotmoss
print(namesl[4][0]) # Prints the element in ages by finding ages in namesl then the number in ages
#################
#Tuples
#################
tuple1 = ("Hashim", "Basle", "Mona", "Mofeed")
tuple2 = ("Tohotmoss",)#The comma at the end makes it a tuple not a string
tuple3 = tuple1 + tuple2 #This hack allows you to add to a tuple later on

print(tuple3)
print(tuple3[0:4])# Should remove the tohotmoss string when printing the tuple 
################
#Dictionaries
################
fav_color2 = {
	"Hashim": "Orange",
	"Basle" : "Blue",
	"Dad": "Green",
	"Mum": "Purple",
}#Dictionary example key:variable Doesn't need to be written this way but it is the convention