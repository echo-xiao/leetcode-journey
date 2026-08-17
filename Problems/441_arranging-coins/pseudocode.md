# 441. 排列硬币 · 解题思路与伪代码

### 一句话直击本质
该算法的核心逻辑是使用二分查找法确定可以完全排列的最大行数。

### 综合思路
1. **二分查找法**：通过二分查找的方法，计算中间行数 `mid` 的硬币总数 `cnt`，并与 `n` 进行比较，调整搜索范围，最终找到最大完整行数。
   - **递归实现**：通过递归调用来实现二分查找。
   - **迭代实现**：通过循环迭代来实现二分查找。

### 全量伪代码
```plaintext
函数 arrangeCoins(n):
    初始化 left = 1, right = n

    // 迭代版本
    当 left <= right 时:
        mid = left + (right - left) // 2
        cnt = (1 + mid) * mid / 2  // 计算前 mid 行硬币总数
        如果 cnt == n:
            返回 mid
        否则如果 cnt > n:
            right = mid - 1  // 缩小右边界
        否则:
            left = mid + 1  // 增大左边界
    返回 right  // 返回最大完整行数

函数 helper(n, left, right):
    // 递归版本
    如果 left > right:
        返回 right

    mid = left + (right - left) // 2
    cnt = (1 + mid) * mid / 2  // 计算前 mid 行硬币总数
    如果 cnt == n:
        返回 mid
    否则如果 cnt > n:
        返回 helper(n, left, mid - 1)  // 缩小右边界
    否则:
        返回 helper(n, mid + 1, right)  // 增大左边界
```

### 复杂度
- **时间复杂度**: $O(\log n)$，因为二分查找每次将搜索空间减半。
- **空间复杂度**: 
  - 迭代版本：$O(1)$，因为只使用了常数空间。
  - 递归版本：$O(\log n)$，因为递归调用栈的深度为 $\log n$。
