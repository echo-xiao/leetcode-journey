# 861. 翻转图像 · 复盘

这个题目一看也不是典型的双指针问题，flip两次，一次是reverse each row，一次是invert the image，invert比较简单，就是0-1互换就行了，所以主要看如何reverse。然后发现其实这个里面的reverse更多是array里面每个index里面的内容需要对撞双指针，然后互换就好了，所以这样看来，逻辑就会很简单。
