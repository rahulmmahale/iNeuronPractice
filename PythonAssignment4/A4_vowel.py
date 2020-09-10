#2.2 Write a Python function which takes a character (i.e. a string of length 1) and returns True if
#it is a vowel, False otherwise.

str1 = input("input a letter ")
str1=str1.lower()

vowels = ['a','e','i','o','u']

if(str1 in vowels):
	print("True")
else:
	print("False")






