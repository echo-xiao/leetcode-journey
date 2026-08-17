# 74. 搜索二维矩阵 · 要素

1. 区间定义：left=0，right=m*n-1，把整个矩阵当成一维数组下标，区间两端都闭

2. while 条件：用 left<=right，因为闭区间里left==right时那个位置还没检查过

3. 判定条件：判定条件是mid映射回二维坐标(row=mid/n, col=mid%n)后matrix[row][col]和target是否相等

4. 边界收缩：midVal==target直接返回True，midVal>target说明target在左边把right=mid-1，midVal<target说明target在右边把left=mid+1
