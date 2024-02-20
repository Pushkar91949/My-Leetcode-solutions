class Solution(object):
    def reverseWords(self, s):
        p=""
        s1=s.split()
        s1.reverse()
        for i in range(0,len(s1)):
            p=p+s1[i]+" "
        return p[0:len(p)-1]
        
