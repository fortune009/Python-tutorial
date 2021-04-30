# print 1 to 20
'''odds = []
numbers = range(1,21)
for number in numbers:
    print(numbers)'''
#print 1 to 1000
numbers = range(1,1001)
for number in numbers:
    print(number)
print(min(numbers))
print(max(numbers))
print(sum(numbers))
#odd numbers from 1 to 20
'''odd_numbers = range(1,20,2)
for number in odd_numbers:
    print((number)'''
#multiple of 3
'''numbers = range(3,20,3)
for number in numbers:
    print(number)'''
#cube from 1 to 10
'''numbers = [1, 2, 3, 4 ,5 ,6, 7, 8, 9, 10]
for number in numbers:
    cube = number**3
    print(cube)'''
# cube compresention
cube_comprehension = [value**3 for value in range(1,11)]
print((cube_comprehension))