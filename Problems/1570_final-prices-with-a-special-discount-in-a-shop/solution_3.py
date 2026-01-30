class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = list(prices)
        stack = []

        for i in range(len(prices)-1, -1, -1):
            while len(stack) > 0 and stack[-1] > prices[i]:
                    stack.pop()
                    
            if len(stack) == 0:
                pass
            else:
                discount = stack[-1]
                res[i] = prices[i] - discount
                
            stack.append(prices[i])
        return res



    def calculateGreaterElement(nums):
        n = len(nums)
        # 存放答案的数组
        res = [0]*n
        s = []
        # 倒着往栈里放
        for i in range(n-1, -1, -1):
            # 判定个子高矮
            while s and s[-1] <= nums[i]:
                # 矮个起开，反正也被挡着了。。。
                s.pop()
            # nums[i] 身后的更大元素
            res[i] = -1 if not s else s[-1]
            s.append(nums[i])
        return res