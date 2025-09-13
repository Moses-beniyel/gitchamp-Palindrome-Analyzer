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