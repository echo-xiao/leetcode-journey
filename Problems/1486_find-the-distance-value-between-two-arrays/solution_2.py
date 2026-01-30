class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        

        arr2.sort()
        cnt = 0
        for i in range(0, len(arr1)):
            left, right = 0, len(arr2)-1
            low = arr1[i] - d
            high = arr1[i] + d

            while left <= right:
                mid = left + (right - left) // 2
                if arr2[mid] >= low:
                    right = mid-1
                elif arr2[mid] < low:
                    left = mid+1
            inserction = left
            is_close = False
            if inserction < len(arr2) and arr2[inserction] <= high:
                is_close = True
            if not is_close:
                cnt+=1
        return cnt




        