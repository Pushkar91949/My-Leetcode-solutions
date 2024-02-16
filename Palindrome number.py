def isPalindrome(self, x):
    y=x
    r=0
    while(x>0):
        a=x%10
        r=r*10+a
        x//=10
    if(y==r):
        return True
    else:
        return False
