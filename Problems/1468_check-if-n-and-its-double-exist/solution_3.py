class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        i = 0
        n = len(arr)
        while i < n:
            j = 0
            while j < n:
                if i != j and arr[i] == 2 * arr[j]:
                    return True
                j += 1
            i += 1
        return False