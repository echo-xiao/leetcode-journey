# 278. 第一个错误的版本 · 要素

1. 区间定义：搜索区间是[left, right]两端都闭，初始left=1，right=n，覆盖所有版本号

2. while 条件：用<=，因为闭区间里left==right时那个版本还没检查过，得继续判断

3. 判定条件：判定条件是isBadVersion(mid)，这是一个单调的check函数（一旦为true后面全为true），不是判断等于某个target

4. 边界收缩：如果mid是错误版本，说明第一个错误版本在mid或更前面，right=mid-1；如果mid不是错误版本，第一个错误版本在mid之后，left=mid+1；没有命中就直接返回的情况，最后left就是第一个错误版本
