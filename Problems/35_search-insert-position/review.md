# 35. 搜索插入位置 · 复盘

找精确值+找边界，但是为什么是return left呢？因为while left≤right，当循环结束，就意味着left>right，左右两个指针交错了，这个时候left指针指向的位置其实就是第一个≥target的元素的位置，这个时候也就是target应该插入的位置。
