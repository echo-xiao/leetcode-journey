# 225. 用队列实现栈

**难度**: Easy | **标签**: `Stack` `Design` `Queue`

## 题目描述

<p>请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部四种操作（<code>push</code>、<code>top</code>、<code>pop</code> 和 <code>empty</code>）。</p>

<p>实现 <code>MyStack</code> 类：</p>

<ul>
	<li><code>void push(int x)</code> 将元素 x 压入栈顶。</li>
	<li><code>int pop()</code> 移除并返回栈顶元素。</li>
	<li><code>int top()</code> 返回栈顶元素。</li>
	<li><code>boolean empty()</code> 如果栈是空的，返回 <code>true</code> ；否则，返回 <code>false</code> 。</li>
</ul>

<p>&nbsp;</p>

<p><strong>注意：</strong></p>

<ul>
	<li>你只能使用队列的标准操作 —— 也就是&nbsp;<code>push to back</code>、<code>peek/pop from front</code>、<code>size</code> 和&nbsp;<code>is empty</code>&nbsp;这些操作。</li>
	<li>你所使用的语言也许不支持队列。&nbsp;你可以使用 list （列表）或者 deque（双端队列）来模拟一个队列&nbsp;, 只要是标准的队列操作即可。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
<strong>输出：</strong>
[null, null, null, 2, 2, false]

<strong>解释：</strong>
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // 返回 2
myStack.pop(); // 返回 2
myStack.empty(); // 返回 False
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= x &lt;= 9</code></li>
	<li>最多调用<code>100</code> 次 <code>push</code>、<code>pop</code>、<code>top</code> 和 <code>empty</code></li>
	<li>每次调用 <code>pop</code> 和 <code>top</code> 都保证栈不为空</li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>你能否仅用一个队列来实现栈。</p>


---
## 解题思路与复盘

1. 一句话直击本质：通过调整队列元素的顺序，使得队列的头部始终保持栈顶元素，从而实现栈的后进先出（LIFO）特性。

2. 综合思路：
   - 使用单个队列：在每次 `push` 操作时，将新元素插入队尾，然后将队列中前面的元素依次出队再入队，直到新元素成为队头，从而模拟栈的行为。
   - 使用列表模拟栈：直接利用列表的 `append` 和 `pop` 操作，天然支持栈的后进先出特性。

3. 全量伪代码：
   - 使用单个队列的实现：
     ```
     初始化队列 res
     
     方法 push(x):
         将 x 添加到队列尾部
         对于队列中除最后一个元素外的所有元素：
             将队头元素出队
             将该元素重新入队到队尾

     方法 pop():
         返回并移除队头元素

     方法 top():
         返回队头元素

     方法 empty():
         如果队列为空，返回 True
         否则返回 False
     ```

   - 使用列表模拟栈的实现：
     ```
     初始化列表 res

     方法 push(x):
         将 x 添加到列表尾部

     方法 pop():
         返回并移除列表尾部元素

     方法 top():
         返回列表尾部元素

     方法 empty():
         如果列表为空，返回 True
         否则返回 False
     ```

4. 复杂度：
   - 使用单个队列的实现：
     - 时间复杂度：`push` 操作为 $O(n)$，`pop`、`top` 和 `empty` 操作为 $O(1)$。
     - 空间复杂度：$O(n)$，其中 $n$ 是队列中元素的数量。

   - 使用列表模拟栈的实现：
     - 时间复杂度：`push`、`pop`、`top` 和 `empty` 操作均为 $O(1)$。
     - 空间复杂度：$O(n)$，其中 $n$ 是列表中元素的数量。