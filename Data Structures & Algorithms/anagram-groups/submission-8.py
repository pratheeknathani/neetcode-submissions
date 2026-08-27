class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for word in strs:
            vals = [0] * 26
            for c in word:
                vals[ord(c)-ord('a')]+=1
            result[tuple(vals)].append(word)
        return list(result.values())