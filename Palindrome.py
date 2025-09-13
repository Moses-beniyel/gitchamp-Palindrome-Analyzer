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

<<<<<<< HEAD

def checklongestpalindrome(arr):
    maxi=-1
    for i in arr:
        if checkpalindrome(i):
            if(len(i)>maxi):
                maxi=len(i)
                res=i
    return res

arr=["moses","PRADEEP","PINTOO","racecar","python"]

print("The longest palindrome is:",checklongestpalindrome(arr))

def totalpalindrome(arr):
    count=0
    for i in arr:
        if checkpalindrome(i):
            count+=1
    s=checkpalindrome(arr)
    print(s)
    return count
arr=["mom","dad","sister","brother","civic"]
print("The total number of palindromes in the list is:",totalpalindrome(arr))
=======
def longestPalindrome(arr):
    maxi=-1
    res=""
    for i in range(len(arr)):
        if(checkpalindrome(arr[i])):
            maxi=math.max(len(arr[i]),maxi)
            res=arr[i]

arr=["madam","moses","malayalam"]
longestPalindrome(arr)
    
    
>>>>>>> 82dbde8b8c63e94126bcd20c73270a9729f3c9ea
