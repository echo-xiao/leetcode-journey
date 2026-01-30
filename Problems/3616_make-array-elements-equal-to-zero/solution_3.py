class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        
        start = []
        for i in range(n):
            if nums[i] == 0:
                start.append(i)
        
        for i in start:
            if self.to_right(i, nums, n):
                cnt += 1
            if self.to_left(i, nums, n):
                cnt += 1
        return cnt


    def to_left(self, start: int, nums: List[int], n: int) -> bool:
        tmp = list(nums)
        curr = start
        direction = -1 

        while 0 <= curr < n:
            if tmp[curr] > 0:
                tmp[curr] -= 1
                direction *= -1
                curr += direction
            else:
                curr += direction

        return self.if_all_zeros(tmp)

    def to_right(self, start: int, nums: List[int], n: int) -> bool:
        tmp = list(nums)
        curr = start
        direction = 1

        while 0 <= curr < n:
            if tmp[curr] > 0:
                tmp[curr] -= 1
                direction *= -1
                curr += direction
            else:
                curr += direction

        return self.if_all_zeros(tmp)


    def if_all_zeros(self, arr: list[int]) -> bool:
        for number in arr:
            if number != 0:
                return False
        return True


