class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """

        slot = 0
        n = len(arr)
        for i in range(0, n):
            if arr[i] == 0:
                slot += 2
            elif arr[i] != 0:
                slot += 1
            if slot >= n:
                break

        j = n - 1

        if slot > n and arr[i] == 0:
            arr[j] = 0
            j -= 1    
            i -= 1    

        while i >= 0:
            if arr[i] == 0:
                arr[j] = 0
                j -= 1
                arr[j] = 0
                j -= 1
            else:
                arr[j] = arr[i]
                j -= 1
            i -= 1
        return arr

            
            
