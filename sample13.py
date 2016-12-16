#lets define a function that will return new list without duplicates
def removedupl(inputList):
#we need empty list before the loop
	secondList = []
	for element in inputList:
		if element not in secondList:
			secondList.append(element)
	return secondList

myList = [1, 2, 3, 2, 3, 1, 2, 3, 4]
myList = removedupl(myList)
print myList
