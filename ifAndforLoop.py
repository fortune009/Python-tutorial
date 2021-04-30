foods = ['rice', 'bean', 'spagethi', 'plaintain']
food_cart = ['pizza', 'fritata', 'rice']
for food in food_cart:
    if food in foods:
        print('Your order is placed on', food)
    else:
        print("Sorry we don't sell", food)
