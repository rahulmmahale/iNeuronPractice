#2. Write a Python program to accept the user's first and last name and then getting them
#printed in the the reverse order with a space between first name and last name.


firstname = input("Please enter first name : ")
lastname = input("Please enter last name : ")

print(firstname[-1::-1] +" "+lastname[-1::-1])