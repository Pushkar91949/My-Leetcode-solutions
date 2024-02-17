class Solution(object):
    def lengthOfLastWord(self, s):
        val=0
        x=s.strip()
        for i in range(len(x)):
            if(x[i]==" "):
                val=0
            else:
                val+=1
        return val
