class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        result = 0
        my_dict = {}
        maxf = 0
        for i in range(len(s)):
            my_dict[s[i]] = my_dict.get(s[i], 0) + 1
            maxf = max(maxf, my_dict[s[i]])
            while (i-l+1) - maxf > k:
                my_dict[s[l]] -= 1
                l += 1
            result = max(result, i-l+1)
        return result

        