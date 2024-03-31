# Count the total number of digits in a number

#there are two methods 
# 1. convert it to string 

def count_Digits(number):
    num_str=str(number)
    return(len(num_str))
number= input("Enter any number to find it's length")
total_digits= count_Digits(number)
print("the length is ",total_digits)

#2 method is to divide the number by 10 until it becomes 0

def count_digitsb(numberb):
    count=0
    while numberb !=0:
        numberb//=10
        count+=1
    return count
numberb=int(input("enter any number to find it's length"))
total_digitsb=count_digitsb(numberb)
print("the lenght is ", total_digitsb)
    