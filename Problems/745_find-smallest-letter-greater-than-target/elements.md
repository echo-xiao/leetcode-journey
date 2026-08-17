# 745. 寻找比目标字母大的最小字母 · 要素

1. 区间定义：用左闭右闭区间，left=0，right=letters.length-1，表示当前还没确定答案、需要继续判断的范围

2. while 条件：用while(left<right)，因为最终要让left和right收拢到同一个下标，表示找到了第一个大于target的位置

3. 判定条件：判定条件是letters[mid]是否大于target，这是个单调条件（一旦大于target，后面都大于target），不是判断等于target

4. 边界收缩：如果letters[mid]>target说明mid可能是答案也可能还有更小的满足条件的，收缩right=mid；否则letters[mid]<=target，答案在mid右边，收缩left=mid+1；循环结束后判断letters[left]是否大于target，是则返回它，否则说明没有比target大的字母，循环取第一个字母letters[0]
