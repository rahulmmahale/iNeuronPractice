#1.1 Write a Python Program(with class concepts) to find the area of the #triangle using the below formula.
#area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
#Function to take the length of the sides of triangle from user should be #defined in the parent
#class and function to calculate the area should be defined in subclass.

class TriangleShape:
	a=0;
	b=0;
	c=0;
	
	def inputSides(self):
		self.a= int(input("Input Side 1 Length : "))
		self.b= int(input("Input Side 2 Length : "))
		self.c= int(input("Input Side 3 Length : "))
		
class AreaTraingle(TriangleShape):
	
	area =0;
	
	def getAreaTraingle(self):
		s = (self.a+self.b+self.c) / 2
		self.area = (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5
		
		return self.area
		
triangle1 = AreaTraingle()
triangle1.inputSides()
area = triangle1.getAreaTraingle()

print(area)

		
		
	
	
	