# 1.1 Write a Python Program to implement your own myreduce() function which works exactly 
# like Python's built-in function reduce()


def do_sum(x1, x2): 
    return x1 + x2
	
def myreduce(r_func,iterable1):
	
	r = iterable1[0];
	
	for item in iterable1[1:]:
			r= r_func(r,item)
			
	return r;
	
list3 = [1,2,3,4,5]

r = myreduce(do_sum,list3)

print(r)

