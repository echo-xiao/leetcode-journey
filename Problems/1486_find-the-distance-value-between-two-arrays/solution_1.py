class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        cnt = 0
        for i in range(0, len(arr1)):
            val1 = arr1[i]
            high = val1 + d
            low = val1 - d

            insert = self.helper(arr2, 0, len(arr2)-1, low)
            
            within = False
            if insert < len(arr2) and arr2[insert] <= high:
                within = True
        
            if within == False:
                cnt += 1
        return cnt

    def helper(self, arr2: List[int], left: int, right: int, low: int) -> int:

        if left > right:
            return left

        mid = left + (right - left) // 2
        if arr2[mid] < low:
            return self.helper(arr2, mid+1, right, low)
        else:
            return self.helper(arr2, left, mid-1, low)





        