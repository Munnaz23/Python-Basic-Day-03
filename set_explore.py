#set is a unique items collection. No duplicate
numbers=[12,56,98,78,56,12,6,98]
print(numbers)


numbers_set = set(numbers)
print(numbers_set)
numbers_set.add(55)
print(numbers_set)

# print(numbers_set.remove(6))
numbers_set.remove(6)
print(numbers_set)

for items in numbers_set:
    print(items)

if 9 in numbers_set:
    print("9 exists")
elif 98 in numbers_set:
    print('98 exists')

A = {1,3,5,7}
B = {1,2,3,4,5}
print(A & B)
print(A|B)

numbers={12,56,98,78,56,12,6,98}
print(numbers)