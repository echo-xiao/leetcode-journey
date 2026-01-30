class Solution:
    def diStringMatch(self, s: str) -> List[int]:


        arr = []
        left = 0
        right = len(s)+1
        lst = list(range(0, right+1))

        for i in s:
            if i == 'I':
                arr.append(lst[left])
                left += 1
            elif i == 'D':
                arr.append(lst[right-1])
                right -= 1
        
        arr.append(lst[left])
        return arr
