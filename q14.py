
# Convert two lists into a dictionary

#using zip function

keys=['a','b','c','d','e','f']
values={7,8,9,10,11}
mydict={key:value for key, value in zip(keys,values)}
print(mydict)