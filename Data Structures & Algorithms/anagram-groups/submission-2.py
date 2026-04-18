class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for word in strs:
            values = [0] * 26
            for w in word:
                values[ord(w)-ord('a')] +=1
            result[tuple(values)].append(word)
        return list(result.values())