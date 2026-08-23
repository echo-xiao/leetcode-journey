class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen1, seen2 = {}, {}
        for i in s:
            if i not in seen1:
                seen1[i] = 1
            else:
                seen1[i] += 1
        for j in t:
            if j not in seen2:
                seen2[j] = 1
            else:
                seen2[j] += 1
        return seen1 == seen2