class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d1 = {st1: i for i, st1 in enumerate(list1)}
        d2 = {st2: j for j, st2 in enumerate(list2)}

        common_keys = set(d1.keys()) & set(d2.keys())

        common = [key for key in common_keys if key in list1 and key in list2]

        sums = [d1[char] + d2[char] for char in common]
        x = min(sums)

        ans = [st for st in common if d1[st] + d2[st] == x]

        return ans
