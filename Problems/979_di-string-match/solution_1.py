class Solution:
    def diStringMatch(self, s: str) -> List[int]:


        arr = []
        left = 0
        right = len(s)
        

        for i in s:
            if i == 'I':
                arr.append(left)
                left += 1
            elif i == 'D':
                arr.append(right)
                right -= 1
        
        arr.append(left)
        return arr
