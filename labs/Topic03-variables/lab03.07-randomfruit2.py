import random

fruitlist = ('Apple', 'Kiwi', 'Grape', 'Tomato', 'Orange', 'Banana', 'Peach', 'Grapefruit', 'Fig', 'Melon', 'Mango', 'Pomegranate', 'Lemon')

index = random.randint(0, len(fruitlist) - 1)

fruit = fruitlist[index]
print("Here is a random fruit: {}".format(fruit))

