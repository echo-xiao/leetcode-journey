class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []
        q = deque()          # 存的是下标，对应的值从队头到队尾单调递减

        for i in range(0, n):
            # 1. 队尾淘汰：比新来的还小(或相等)的，永远轮不到当最大值了
            while len(q) > 0 and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)

            # 2. 队头过期：已经滑出窗口了
            if q[0] <= i - k:
                q.popleft()

            # 3. 窗口满了就记账，队头就是当前窗口的最大值
            if i >= k - 1:
                res.append(nums[q[0]])

        return res