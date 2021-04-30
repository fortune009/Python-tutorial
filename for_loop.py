nig_food = ['yam', 'rice', 'beans', 'plantain']
#for food in nig_food: 
    #print(food.title() + ' is one of my favorite food')
    #print('The first three items in the list are: \n', food[0:3])
nigerian_food = nig_food.copy()
nig_food.append('jollof')
nigerian_food.append('egusi')
#print(nig_food)
#print(nigerian_food)
print('My favorite food are:')
for food in nig_food:
    print(food)
print('\n')
print('My friend’s favorite pizzas are:')
for food in nigerian_food:
    print(food)
    