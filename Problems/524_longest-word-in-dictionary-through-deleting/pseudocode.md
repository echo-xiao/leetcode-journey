# 524. 通过删除字母匹配到字典里最长单词 · 解题思路与伪代码

## 一句话本质
对字典中每个单词用**双指针贪心匹配**判断其是否为字符串 s 的子序列，在所有满足条件的单词中选取**最长且字典序最小**的那个。

## 综合思路

本题的 AC 解法本质上都是围绕"子序列匹配"展开，主要有以下几种实现思路：

1. **双指针法（主流做法，如本例）**  
   对字典中每个单词 word，用两个指针分别遍历 s 和 word，判断 word 是否是 s 的子序列；遍历全部字典单词后维护最优解（更长或同长度字典序更小）。

2. **排序 + 提前终止法**  
   先将字典按"长度降序、字典序升序"排序，然后依次检查每个单词是否为 s 的子序列，第一个匹配成功的即为答案，无需再遍历后续单词。

3. **动态规划预处理法（进阶优化）**  
   预处理字符串 s，构建 `dp[i][j]` 表示从位置 i 开始，字符 j 下一次出现的位置（即"下一字符索引"表），这样对字典中每个单词做子序列匹配时可以用二分或直接查表加速到 $O(1)$ 判断下一步跳转位置，从而将多次匹配的总复杂度降低。

## 全量伪代码

### 思路一：双指针遍历法
```
函数 findLongestWord(s, dictionary):
    res = ""
    对 dictionary 中每个 word:
        i = 0  // 指向 s
        j = 0  // 指向 word
        当 i < len(s) 且 j < len(word):
            如果 s[i] == word[j]:
                j += 1
            i += 1
        如果 j == len(word):  // word 是 s 的子序列
            如果 len(word) > len(res) 或 (长度相等且 word 字典序更小):
                res = word
    返回 res
```

### 思路二：排序+提前返回
```
函数 findLongestWord(s, dictionary):
    对 dictionary 按 (长度降序, 字典序升序) 排序
    对排序后的每个 word:
        如果 isSubsequence(word, s):
            返回 word
    返回 ""

函数 isSubsequence(word, s):
    i = 0, j = 0
    当 i < len(word) 且 j < len(s):
        如果 word[i] == s[j]:
            i += 1
        j += 1
    返回 i == len(word)
```

### 思路三：预处理DP加速匹配
```
函数 findLongestWord(s, dictionary):
    n = len(s)
    构建 next[n+1][26]：
        next[n][*] = n  // 边界，表示不存在
        for i from n-1 down to 0:
            for c in 0..25:
                if s[i] == c 对应字符:
                    next[i][c] = i
                else:
                    next[i][c] = next[i+1][c]
    
    res = ""
    对 dictionary 中每个 word:
        pos = 0
        match = True
        对 word 中每个字符 c:
            pos = next[pos][c - 'a']
            如果 pos == n:
                match = False
                跳出
            pos += 1
        如果 match:
            如果 len(word) > len(res) 或 (等长且字典序更小):
                res = word
    返回 res
```

## 复杂度分析

设 $s$ 长度为 $m$，字典单词数为 $n$，单词平均长度为 $k$（最大长度为 $L$）。

**思路一 / 思路二（双指针法）**
- 时间复杂度：$O(n \times m)$，对每个单词都需扫描一次 s
- 空间复杂度：$O(1)$（不计排序，若排序则为 $O(\log n)$ 或 $O(n)$）

**思路三（DP预处理）**
- 时间复杂度：预处理 $O(m \times 26)$，查询总共 $O(n \times k)$，整体为 $O(m \times 26 + n \times k)$
- 空间复杂度：$O(m \times 26)$ 用于存储 next 数组

**综合总结**：
$$\text{Time} = O(n \cdot m) \quad \text{或优化为} \quad O(m \cdot 26 + \sum k_i)$$
$$\text{Space} = O(1) \quad \text{或} \quad O(m \cdot 26)$$
