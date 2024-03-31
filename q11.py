# Write a program to print multiplication table of a given number

def multiplication_table(num):
    i=1
    while i<=10:
        print(num*i)
        i+=1
num=int(input("enter number for table "))
multiplication_table(num)        