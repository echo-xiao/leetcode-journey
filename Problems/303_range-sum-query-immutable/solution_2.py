class NumArray:

    def __init__(self, nums: List[int]):
        self.curr = [0] * (len(nums)+1)
        for i in range(0, len(nums)):
            self.curr[i+1] = self.curr[i] + nums[i]
        

    def sumRange(self, left: int, right: int) -> int:
        res = self.curr[right+1] - self.curr[left]
        return res


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)