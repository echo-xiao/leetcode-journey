class Solution(object):
    def dietPlanPerformance(self, calories, k, lower, upper):
        """
        :type calories: List[int]
        :type k: int
        :type lower: int
        :type upper: int
        :rtype: int
        """
        

        T = sum(calories[0:k])
        cnt = 0
        left = 0
        if T < lower: cnt -= 1
        elif T > upper: cnt += 1

        for right in range(k, len(calories)):
            T = T + calories[right] - calories[left]
            if T < lower:
                cnt -= 1
            elif T > upper:
                cnt += 1
            left += 1
        return cnt