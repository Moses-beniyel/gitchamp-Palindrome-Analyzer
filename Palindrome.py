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

arr=["moses","madam","noon","racecar","python"]

print("The longest palindrome is:",checklongestpalindrome(arr))