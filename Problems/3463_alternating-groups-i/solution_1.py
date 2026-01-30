class Solution(object):
    def numberOfAlternatingGroups(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        
        arr = colors[:] + colors[0:2]
        cnt = 0
        
        for l in range(0, len(arr)-2):
            if arr[l] != arr[l+1] and arr[l+1] != arr[l+2]:
                cnt += 1
        return cnt
