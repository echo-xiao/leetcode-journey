# 275. H 指数 II · 要素

1. 区间定义：区间是下标索引区间[left, right]，left=0，right=n-1，两端都闭

2. while 条件：用 while(left<=right)，因为闭区间要包含left==right这一个元素的情况

3. 判定条件：判定条件是citations[mid]与n-mid比较，看第mid个及之后共n-mid篇论文的引用数是否都够格，本质是找citations[mid]>=n-mid的最左位置

4. 边界收缩：citations[mid]==n-mid时命中直接返回n-mid；citations[mid]>n-mid说明答案可能更大，right=mid-1往左收缩；citations[mid]<n-mid说明不够格，left=mid+1往右收缩，循环结束后返回n-left
