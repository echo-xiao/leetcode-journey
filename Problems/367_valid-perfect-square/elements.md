# 367. 有效的完全平方数 · 要素

1. 区间定义：区间定义为左右都闭的[left, right]，初始left=1，right=num，表示可能的平方根候选范围

2. while 条件：while条件用left<=right（迭代版）或者对应地递归版用left>right作为终止判断，因为闭区间在left==right时还要检查这个值

3. 判定条件：判定条件是mid*mid和num的比较：相等就是完全平方数，mid*mid>num说明mid偏大，mid*mid<num说明mid偏小

4. 边界收缩：mid*mid==num时直接返回True；mid*mid>num时说明根在mid左边，right=mid-1；mid*mid<num时说明根在mid右边，left=mid+1；循环结束还没找到就返回False
