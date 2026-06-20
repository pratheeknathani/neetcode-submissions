class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for word in strs:
            chars = [0] * 26
            for l in word:
                chars[ord(l)- ord('a')] +=1
            result[tuple(chars)].append(word)
        return list(result.values())