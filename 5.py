import random
def randomize(n):
	array = [random.randrange(1,10,2) for i in range(n)]
	print('Array:',array)
	print('Sum  :',sum(array))