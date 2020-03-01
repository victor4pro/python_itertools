#Itertools
import itertools

# counter = itertools.count(start=5, step=5)

# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

# counter = itertools.cycle([1,2,3])

# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

# counter = itertools.cycle(('ON','OFF'))

# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

# counter = itertools.repeat(2,times=5)

# for i in counter:
# 	print(counter)

# data = [100, 200, 300, 400]
# dayly_data = list(itertools.zip_longest(range(10),data))

# data = [100, 200, 300, 400]
# dayly_data = list(zip(range(10),data))


# print(dayly_data)
# print(dayly_data[0])

# def hola(x):
# 	return x*x
# squares = list(map(hola,range(10)))
# print(squares)

# squares = itertools.starmap(pow,[(0,1),(2,3),(4,5),(6,7)])
# print(list(squares))

letters = ['a','b','c','d','e']
numbers = [2,3,4,5]
names = ['Victor','Landaeta','Jimenez']

# result = itertools.combinations(letters,3)

# for item in result:
# 	print(item)

result2 = itertools.combinations(numbers,2)
for item in result2:
	print(item)

# result = itertools.permutations(letters,5)
# for item in result:
# 	print(item)

# result = itertools.permutations(numbers,4)
# for item1 in result:
# 	for valor in range(1,len(item1)):
# 		array1 = item1[:valor]
# 		array2 = item1[valor:]
# 		suma = abs(sum(array1)-sum(array2))
# 		print(suma)

# result = itertools.product(numbers, repeat=3)
# for item in result:
# 	print(item)