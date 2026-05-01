from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for word in strs:
            wordArr = [0] * 26
            for l in word:
                wordArr[ord('a')-ord(l)] +=1
            result[tuple(wordArr)].append(word)
        return list(result.values())