

def unique_number(list_of_numbers):
	print list_of_numbers

	for item in list_of_numbers:
		count1 = 0
		for item2 in list_of_numbers:
			if item == item2:
				count1 = count1 + 1

		if count1 == 1:
			print item
def try_new(numbers):
	mapping = [0] * (int(len(numbers)/2) + 2)
	for item in numbers:
		mapping[item] +=  1
	print mapping

	for index in range(len(mapping)):
		if mapping[index] == 1:
			print index	

def doit(numbers):
	mapping = dict()
	
	for item in numbers:
		if mapping.get(item):
			mapping[item] += 1
		else:
			mapping[item] = 1

	print mapping	


def foo(numbers):
	out = 0
	for i in numbers:
		out ^= i

	print out

if __name__ == '__main__':
	list_of_numbers = [1,2,1,2,3,3,4,5,6,5,6]
	#	unique_number(list_of_numbers)
	#try_new(list_of_numbers)
	#doit(list_of_numbers)
	#doit([1,99999999, 1])
	foo(list_of_numbers)

