class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tail = [nums[0]]

        for i in range(0, len(nums)):
            num = nums[i]

            if num > tail[-1]:
                tail.append(num)
            else:
                self.insertToTail(tail, num)
        return len(tail)

    def insertToTail(self, tail: List[int], num: int) -> int:
        left, right = 0, len(tail)-1
        while left <= right:
            mid = left + (right - left) // 2
            if tail[mid] >= num:
                right = mid - 1
            elif tail[mid] < num:
                left = mid + 1

        tail[left] = num
        return tail
            