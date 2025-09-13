import math
def checkpalindrome(s):
   
    l=0
    r=len(s)-1
    while l<r:
        if s[l]!=s[r]:
            return False
        l+=1
        r-=1
    return True
s=input("Enter a string: ")
if checkpalindrome(s):
    print("The given string is palindrome")
else:
    print("it is not a palindome")

def longestPalindrome(arr):
    maxi=-1
    res=""
    for i in range(len(arr)):
        if(checkpalindrome(arr[i])):
            maxi=math.max(len(arr[i]),maxi)
            res=arr[i]

arr=["madam","moses","malayalam"]
longestPalindrome(arr)
    
    