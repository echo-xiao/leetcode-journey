class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        sumArr = sum(arr)
        if sumArr % 3 != 0:
            return False

        targetSum = sum(arr) / 3

        curr = 0
        cnt = 0

        for num in arr:
            curr += num
            if curr == targetSum:
                cnt += 1
                curr = 0
            if cnt == 3:
                return True

        return cnt == 3

            