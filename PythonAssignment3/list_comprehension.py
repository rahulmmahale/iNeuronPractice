#2. Implement List comprehensions to produce the following lists. 
#Write List comprehensions to produce the following Lists
#['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
#['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz'] 
#['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz'] 

#[[2], [3], [4], [3], [4], [5], [4], [5], [6]] [[2, 3, 4, 5], [3, 4, 5, 6], 
#[4, 5, 6, 7], [5, 6, 7, 8]]

#[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]


letters = [letter for letter in "ACADGILD"]
print (letters)

pattern1 = [ x*i  for x in ['x','y','z'] for i in range(1,5) ]
print(pattern1)

pattern2 = [ (x*i) for i in range(1,5) for x in ['x','y','z'] ]
print(pattern2)

list5 = [ [x] for a in range(2,5) for x in range(a,a+3) ]
list7 = [ [x for x in range (a,a+4)] for a in range(2,6)]
list8 = list5+list7
print(list8)

list6 = [(a,b) for a in range(1,4) for b in range (1,4)]
print(list6)