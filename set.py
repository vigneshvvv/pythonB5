numbers = {10,20,30,40,10}
print(numbers)

numbers.add(50)
print(numbers)
numbers.add(20)
print(numbers)
numbers.remove(20)
print(numbers)

numbers.discard(60)
print(numbers)

print(numbers.pop())
print(numbers)
# numbers.clear()
# print(numbers)

sample = [120,122,120,122,230]
sample = set(sample)
print(sample)
sample = list(sample)
print(sample)

sample.reverse()
print(sample)

numbers1 = numbers.copy()
print(numbers1)

a= {1,2,3,4}
b= {3,4,5,6}
print(a.union(b))

print(a.intersection(b))

print(a.difference(b))

print(a.symmetric_difference(b))
