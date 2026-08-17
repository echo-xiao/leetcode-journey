# 225. 用队列实现栈 · 复盘

queue和deque的区别，queue是一种概念，deque（双端队列）是一种具体实现，可以双端进行push和pop操作，一般python中，用deque这个数据结构来实现一个queue。popleft是deque的一个方法，remove并且返回队伍的top元素，deque如果直接pop的话，就是从尾部一处并且返回元素。这个题目比较简单，queue可以popleft，也就是pop头部，queue的头部就是stack的头部，但是queue是push到尾部的，但是stack只能从头部push，那么需要一个for loop到size-1的的这个循环来解决。
