class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) < 2:
            return len(arr)

        left, right = 0, 0
        maxLen = 1
        isBroken = False

        while right < len(arr)-1:
            right += 1

            curr = self.compare(arr, right)

            if curr == 0:
                isBroken = True
            elif right > 1:
                prev = self.compare(arr, right-1)
                if curr == prev:
                    isBroken = True
            
            while isBroken == True:
                if curr == 0:
                    left = right
                else:
                    left = right - 1
                isBroken = False

            maxLen = max(maxLen, right-left+1)
        return maxLen


    def compare(self, arr: List[int], i: int) -> int:
        
        if arr[i] > arr[i-1]:
            return 1
        elif arr[i] < arr[i-1]:
            return -1
        else:
            return 0