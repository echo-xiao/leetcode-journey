class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count, s2Count = {}, {}
        
        for char in s1:
            s1Count[char] = 1 + s1Count.get(char, 0)

        left, right = 0, 0


        while right < len(s2):
            s2Count[s2[right]] = 1 + s2Count.get(s2[right], 0)
            right += 1

            while right - left > len(s1):
                
                s2Count[s2[left]] -= 1
                if s2Count[s2[left]] == 0:
                    del s2Count[s2[left]]

                left += 1

            if s1Count == s2Count:
                return True
        return False
