# 69. x 的平方根 · 要素

1. 区间定义：区间是两端都闭的[left, right]，初始left=0（或1），right=x，表示在这个闭区间里找平方根

2. while 条件：用<=，因为闭区间[left,right]里left==right时那个数还没检查，必须再判一次

3. 判定条件：判定条件是mid*mid和x比较：相等直接就是答案，大于说明mid偏大，小于说明mid可能是答案但还要往右找更大的

4. 边界收缩：mid*mid==x时直接返回mid；mid*mid>x时right=mid-1；mid*mid<x时先把res记为mid（因为要的是不超过x的最大整数，mid是候选答案）再left=mid+1继续找更大的
