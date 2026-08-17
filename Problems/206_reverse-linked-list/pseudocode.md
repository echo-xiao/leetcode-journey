# 206. 反转链表 · 解题思路与伪代码

### 一句话直击本质
通过逐步反转链表节点的指针方向，实现链表的逆序。

### 综合思路
1. **迭代法**：通过遍历链表，逐个反转节点的指针方向，直到遍历完整个链表。
2. **递归法**：通过递归调用，将链表分解为子问题，逐层反转指针方向，最终实现链表逆序。

### 全量伪代码

#### 迭代法
```plaintext
函数 reverseList(链表头节点 head):
    如果 head 是空:
        返回 head

    初始化 left 为 None
    初始化 right 为 head

    当 right 的下一个节点不为空时:
        保存 right 的下一个节点为 helper
        将 right 的下一个节点指向 left
        将 left 更新为 right
        将 right 更新为 helper

    将 head 更新为 right
    将 head 的下一个节点指向 left
    返回 head
```

#### 递归法
```plaintext
函数 reverseList(链表头节点 head):
    如果 head 是空或 head 的下一个节点是空:
        返回 head

    递归调用 reverseList(head 的下一个节点) 并保存为 newHead
    将 head 的下一个节点的下一个指针指向 head
    将 head 的下一个节点指向空
    返回 newHead
```

### 复杂度
- **时间复杂度**: $O(n)$，其中 $n$ 是链表的节点数量，因为每个节点都被访问一次。
- **空间复杂度**: 
  - 迭代法：$O(1)$，因为只使用了常数级别的额外空间。
  - 递归法：$O(n)$，因为递归调用栈的深度为 $n$。
