class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for word in strs:
            freq = {}
            for s in word:
                freq[s] = freq.get(s, 0) + 1
            key = tuple(sorted(freq.items()))
            if key in res:
                res[key].append(word)
            else:
                res[key] = [word]
        return list(res.values())

        


        