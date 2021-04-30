first_list = ['a', 'b', 'c', 'd']
second_list = []
n = len(first_list)
for i in range (n): 
    second_list.append(first_list[i])
    #print(first_list[i])
    #print(second_list)
    del first_list[i]