# 441. 排列硬币 · 要素

1. 区间定义：搜索区间是[left, right]两端都闭，初始left=1，right=n，因为最少可能是第1行，最多不会超过n行

2. while 条件：用<=，因为区间是闭区间，left==right时mid这个值还没检查过，必须继续循环

3. 判定条件：判定条件是比较前mid行硬币总数cnt=(1+mid)*mid/2和n的大小关系，是单调递增的check函数

4. 边界收缩：cnt==n时直接返回mid（找到恰好排满的行数）；cnt>n说明mid行数多了，right=mid-1；cnt<n说明还能排更多行，left=mid+1，循环结束后返回right作为最大完整行数
