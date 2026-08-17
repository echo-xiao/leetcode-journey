# 816. 设计哈希集合 · 复盘

init里面要装的是初始化的东西，装的是n个linked list，所以那么写。add、remove、contain都是要定好。然后index，以及每个linked list对应的head是啥。然后就是正常的add、remove、contain的实现了。这个方法被称为拉链法（chaining），解决哈希冲突最常用最经典的方法。
