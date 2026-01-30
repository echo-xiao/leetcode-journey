class Solution(object):
    def findIndices(self, nums, indexDifference, valueDifference):
        """
        :type nums: List[int]
        :type indexDifference: int
        :type valueDifference: int
        :rtype: List[int]
        """
        answer = []
        for i in range(0, len(nums)):
            for j in range(i+indexDifference, len(nums)):
                if abs(i-j) >= indexDifference and abs(nums[i]-nums[j]) >= valueDifference:
                    answer = [i, j]


        if answer == []:
            return [-1, -1]
        else:
            return answer 