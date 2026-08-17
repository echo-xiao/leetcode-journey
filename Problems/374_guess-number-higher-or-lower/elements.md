# 374. 猜数字大小 · 要素

1. 区间定义：区间是[left, right]两端都闭，初始left=1，right=n，因为n是可能取到的最大数字

2. while 条件：while用left<=right（迭代版），因为闭区间里left==right时还有一个数没检查

3. 判定条件：判定条件是guess(mid)的返回值：0表示猜中，-1表示mid猜大了，1表示mid猜小了

4. 边界收缩：猜中(guess(mid)==0)直接返回mid；猜大了(-1)说明目标更小，right=mid-1；猜小了(1)说明目标更大，left=mid+1
