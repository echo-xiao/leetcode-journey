class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        h = [8, 4, 2, 1]
        m = [32, 16, 8, 4, 2, 1]

        hmap = {}
        mmap = {}

        
        self.backtrack(h, 0, 0, hmap, 0)
        self.backtrack(m, 0, 0, mmap, 0)

        res = []

        for hcnt in range(turnedOn+1):
            mcnt = turnedOn - hcnt
            hlist = hmap.get(hcnt, [])
            mlist = mmap.get(mcnt, [])

            for h in hlist:
                if h < 12:
                    for m in mlist:
                        if m < 60:
                            res.append(f"{h}:{m:02d}")
        return res


    def backtrack(self, nums: List[int], idx: int, prev: int, res: dict, cnt: int):

        if idx == len(nums):
            if cnt not in res:
                res[cnt] = []
            res[cnt].append(prev)
            return 

        self.backtrack(nums, idx+1, prev, res, cnt)
        self.backtrack(nums, idx+1, prev + nums[idx], res, cnt+1)

        # 回溯函数，用递归
        # 判断H或者M，生成新的路径
        # 路径是否满足要求，不满足就stop
        # 生成一个变量来判断累积的和是多少
        # 如果可以，就加入到结果表里面