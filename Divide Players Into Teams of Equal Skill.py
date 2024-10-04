class Solution:
    def dividePlayers(self, skl: List[int]) -> int:
        skl.sort()
        i, j = 1, len(skl) - 2
        prs = [(skl[0],skl[-1])]
        while i < j and skl[i] + skl[j] == prs[-1][0] + prs[-1][1]:
            prs.append((skl[i], skl[j]))
            i += 1
            j -= 1
        if len(prs) == len(skl) // 2:
            chem = 0
            for v1, v2 in prs:
                chem += v1 * v2
            return chem
        return -1
