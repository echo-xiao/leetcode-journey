class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        

        left, right = 0, 0
        res = {}
        maxSum = 0
        while right < len(fruits):
            res[fruits[right]] = 1 + res.get(fruits[right], 0)
            right += 1

            while len(res) > 2:
                res[fruits[left]] -= 1

                if res[fruits[left]] == 0:
                    del res[fruits[left]]
                    
                left += 1

            maxSum = max(maxSum, right-left)
        return maxSum