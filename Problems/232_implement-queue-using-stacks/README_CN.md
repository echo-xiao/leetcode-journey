# 232. 用栈实现队列

**难度**: Easy | **标签**: `Stack` `Design` `Queue`

## 题目描述

<p>请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（<code>push</code>、<code>pop</code>、<code>peek</code>、<code>empty</code>）：</p>

<p>实现 <code>MyQueue</code> 类：</p>

<ul>
	<li><code>void push(int x)</code> 将元素 x 推到队列的末尾</li>
	<li><code>int pop()</code> 从队列的开头移除并返回元素</li>
	<li><code>int peek()</code> 返回队列开头的元素</li>
	<li><code>boolean empty()</code> 如果队列为空，返回 <code>true</code> ；否则，返回 <code>false</code></li>
</ul>

<p><strong>说明：</strong></p>

<ul>
	<li>你 <strong>只能</strong> 使用标准的栈操作 —— 也就是只有&nbsp;<code>push to top</code>,&nbsp;<code>peek/pop from top</code>,&nbsp;<code>size</code>, 和&nbsp;<code>is empty</code>&nbsp;操作是合法的。</li>
	<li>你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
<strong>输出：</strong>
[null, null, null, 1, 1, false]

<strong>解释：</strong>
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
</pre>

<ul>
</ul>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= x &lt;= 9</code></li>
	<li>最多调用 <code>100</code> 次 <code>push</code>、<code>pop</code>、<code>peek</code> 和 <code>empty</code></li>
	<li>假设所有操作都是有效的 （例如，一个空的队列不会调用 <code>pop</code> 或者 <code>peek</code> 操作）</li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong></p>

<ul>
	<li>你能否实现每个操作均摊时间复杂度为 <code>O(1)</code> 的队列？换句话说，执行 <code>n</code> 个操作的总时间复杂度为 <code>O(n)</code> ，即使其中一个操作可能花费较长时间。</li>
</ul>


---
## 解题思路与复盘

### 1. 一句话直击本质

利用两个栈来实现队列的先进先出（FIFO）特性，通过将一个栈的元素转移到另一个栈来实现元素的顺序反转。

### 2. 综合思路

所有版本的实现逻辑基本一致，均采用两个栈（`input` 和 `output`）来模拟队列的行为。主要思路如下：

- **栈的转移**：当需要从队列中弹出或查看队首元素时，如果 `output` 栈为空，则将 `input` 栈中的所有元素依次弹出并压入 `output` 栈，这样就实现了元素顺序的反转。
- **入队操作**：直接将元素压入 `input` 栈。
- **出队和查看队首操作**：通过 `transfer` 方法确保 `output` 栈中有元素，然后从 `output` 栈中弹出或查看栈顶元素。
- **判空操作**：检查两个栈是否都为空。

### 3. 全量伪代码

```plaintext
类 MyQueue:
    方法 __init__():
        初始化 input 栈为空列表
        初始化 output 栈为空列表

    方法 push(x):
        将 x 压入 input 栈

    方法 transfer():
        如果 output 栈为空:
            当 input 栈不为空时:
                将 input 栈顶元素弹出并压入 output 栈

    方法 pop():
        调用 transfer 方法
        从 output 栈弹出并返回栈顶元素

    方法 peek():
        调用 transfer 方法
        返回 output 栈顶元素

    方法 empty():
        返回 input 栈和 output 栈是否都为空
```

### 4. 复杂度

- **时间复杂度**：
  - `push` 操作：$O(1)$
  - `pop` 和 `peek` 操作：摊销时间复杂度为 $O(1)$，因为每个元素最多只会被转移一次。
  - `empty` 操作：$O(1)$

- **空间复杂度**：$O(n)$，其中 $n$ 是队列中元素的总数，因为需要两个栈来存储元素。