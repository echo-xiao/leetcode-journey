# 745. 寻找比目标字母大的最小字母 · 解题思路与伪代码

1. **一句话直击本质：** 该算法的核心逻辑是利用二分查找在有序字符数组中寻找比目标字母大的最小字母。

2. **综合思路：**
   - **递归二分查找：** 通过递归的方式实现二分查找，逐步缩小查找范围，直到找到比目标字母大的最小字母。
   - **迭代二分查找：** 通过迭代的方式实现二分查找，使用循环来调整查找范围，最终找到目标字母。

3. **全量伪代码：**

   - **递归二分查找：**
     ```
     函数 nextGreatestLetter(letters, target):
         调用 helper(letters, target, 0, len(letters) - 1)
         返回 letters[index % len(letters)]

     函数 helper(letters, target, left, right):
         如果 left > right:
             返回 left
         
         mid = left + (right - left) // 2
         
         如果 letters[mid] > target:
             返回 helper(letters, target, left, mid - 1)
         否则:
             返回 helper(letters, target, mid + 1, right)
     ```

   - **迭代二分查找：**
     ```
     函数 nextGreatestLetter(letters, target):
         left = 0
         right = len(letters) - 1
         
         当 left < right:
             mid = left + (right - left) // 2
             
             如果 letters[mid] > target:
                 right = mid
             否则:
                 left = mid + 1
         
         如果 letters[left] > target:
             返回 letters[left]
         否则:
             返回 letters[0]
     ```

4. **复杂度：**
   - 时间复杂度：$O(\log n)$，因为二分查找的时间复杂度是对数级别的。
   - 空间复杂度：递归版本是 $O(\log n)$（由于递归调用栈），迭代版本是 $O(1)$。
