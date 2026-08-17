# 658. 找到 K 个最接近的元素 · 要素

1. 区间定义：left=0，right=arr.length-k，表示子数组起始下标的搜索范围，两端都闭（left和right都是可取到的合法起始位置）

2. while 条件：用left<right，因为是在收缩找唯一的最优起始点，不需要单点判断相等的情况

3. 判定条件：判定条件是比较x-arr[mid]和arr[mid+k]-x哪个更大：如果x-arr[mid]>arr[mid+k]-x说明左边这个元素太远，起点该往右移

4. 边界收缩：如果x-arr[mid]>arr[mid+k]-x，说明mid这个起点太靠左，令left=mid+1；否则说明mid+k这一侧更远或相等，令right=mid（收缩到更靠左的位置），最终left==right就是答案的起始下标，不存在“命中即返回”的情况，因为这里找的是最优位置而非精确匹配值
