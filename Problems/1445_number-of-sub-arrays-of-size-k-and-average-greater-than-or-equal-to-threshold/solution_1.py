class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        num = sum(arr[0: k])
        if num >= threshold * k:
            cnt = 1
        else:
            cnt = 0

        for i in range(k, len(arr)):
            num = num + arr[i] - arr[i-k]
            if num >= threshold * k:
                cnt += 1
        return cnt