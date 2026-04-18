class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for word in strs:
            temp = [0] * 26
            for l in word:
                temp[ord(l)-ord('a')] +=1
            result[tuple(temp)].append(word)
        return list(result.values())