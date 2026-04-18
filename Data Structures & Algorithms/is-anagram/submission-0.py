class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        my_dict = {}
        temp = {}
        for i in s:
            my_dict[i] = my_dict.get(i,0) + 1
        for i in t:
            temp[i] = temp.get(i,0) + 1
        return my_dict == temp