#1.2 Write a function filter_long_words() that takes a list of words and an #integer n and returns
#the list of words that are longer than n.

def filter_long_words(list_of_words,n=0):
	
	longer_words = []
	
	for word in list_of_words:
		if len(word) > n:
			longer_words.append(word)
			
	return longer_words
	

list_of_words = ['abcd','efgh','df','dfg','rahul']
longerList = filter_long_words(list_of_words,3)

print(longerList)


