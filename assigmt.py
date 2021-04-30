'''my_list = [0, 5, 7, 9, 'all'] 
fred_list = []
for number in my_list:
    fred_list.append(number)
print(fred_list)
first_list = ['a', 'b', 'c', 'd'] 
second_list = []
for item in first_list:
    second_list.append(item)
    #first_list.remove(item)
print(first_list)
print(second_list)
my_list = [0, 1, 2, 3, 4, 5 ] 
squares = []
for number in my_list:
    squares.append(number**2)
print(my_list)
print(squares)'''
my_list = [0, 1, 2, 3, 4, 5 ] 
squares = [num**2 for num in my_list]
print(squares)