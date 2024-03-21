class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        sc = Counter(secret)
        sg = Counter(guess)
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
                sc[secret[i]] -= 1
                sg[guess[i]] -= 1
                
        for char in sg:
            cows += min(sc[char], sg[char])
            
        return str(bulls) + "A" + str(cows) + "B"  #Question link: https://leetcode.com/problems/bulls-and-cows/
