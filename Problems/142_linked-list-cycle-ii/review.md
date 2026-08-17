# 142. 环形链表 II · 复盘

**犯了几个错误**，a. 误判了相遇点，需要知道fast和slow指针先相交再环内，然后如果重制某一个指针，然后就会相遇在环的入口点。b. 循环关系依赖错误，另外就是要while嵌套，因为一个loop是另外一个loop的延续。c. 在循环一开始就判断 if slow == fast，指针还没有移动就直接跳出了循环；d. 空指针报错，就是while loop条件如何写，核心原则就是需要判断指针往后走几步，如果是走一步那就是fast is not none，如果是走两步 那就是 fast.next is not none。e. 死循环风险，找到了环 slow == fast，但是没有 break 跳出循环。
