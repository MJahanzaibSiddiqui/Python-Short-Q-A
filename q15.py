#merging dictionaries by using unpacking


mydict1 = {'a': 3, 'b': 4}
mydict2 = {'c': 3, 'd': 4}

mydict3 = {**mydict1, **mydict2}

print(mydict3)