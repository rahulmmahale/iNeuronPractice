# 1.2 Write a Python program to implement your own myfilter() function which works exactly 
# like Python's built-in function filter()

def isEven(x1): 
	if x1%2 == 0 :
		return True
	else:
		return False
	
def myfilter(f_func,iterable1):
	
	filtered_values=[]
	for item in iterable1[1:]:
			r= f_func(item)
			if r == True:
				filtered_values.append(item)
			
	return filtered_values;
	
list3 = [1,2,3,4,5]

r = myfilter(isEven,list3)

print(r)

