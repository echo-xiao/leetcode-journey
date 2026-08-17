# 254. 因子的组合 · 要素

1. 路径：path 里存已经确定的一串从小到大的因子，比如对 12 走到 path=[2] 表示已经拆出一个 2，剩下 6 待拆。

2. 选择列表：从 start（上一次用的因子，保证不递减）到 sqrt(target) 之间能整除 target 的 i，选它就把 target 变成 target/i 继续拆。

3. 结束条件：i 超过 sqrt(target) 就没得选了，循环自然结束返回；每次找到能整除的 i 时，直接把 path+[i, target/i] 作为一个完整答案记下来。

4. 撤销：递归回来后把刚 append 进 path 的那个因子 i pop 掉，让 path 回到进入这层前的样子。
