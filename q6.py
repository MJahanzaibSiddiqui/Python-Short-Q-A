# Python program to check whether the string is Palindrome
def palindrome(j):
    j=j.replace("","").lower()
    return j==j[::-1]


for_check=input("Enter word")
if palindrome(for_check):
    print("yes it is ")
else:
    print("No")    