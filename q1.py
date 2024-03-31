# Python program to interchange first and last elements in a list
print("Given List")
mylist=[1,2,3,4,5]
print(mylist)
print("After interchange")
mylist[0],mylist[-1]=mylist[-1],mylist[0];
print(mylist)