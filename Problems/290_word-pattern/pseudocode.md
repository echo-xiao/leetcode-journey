# 290. 单词规律 · 解题思路与伪代码

1. 一句话直击本质：使用双向映射验证模式字符串和单词序列之间的一一对应关系。

2. 综合思路：
   - 双向映射：使用两个字典分别记录模式字符到单词的映射和单词到模式字符的映射，确保每个字符和单词之间的映射是唯一且一致的。

3. 全量伪代码：
   ```
   定义函数 wordPattern(pattern, s):
       将字符串 s 按空格分割成单词列表 words
       如果 pattern 的长度不等于 words 的长度:
           返回 False

       初始化两个空字典 charToStr 和 strToChar

       对于 pattern 和 words 中的每一对字符 c 和单词 w:
           如果 c 在 charToStr 中且 charToStr[c] 不等于 w:
               返回 False
           如果 w 在 strToChar 中且 strToChar[w] 不等于 c:
               返回 False

           将 c 映射到 w (charToStr[c] = w)
           将 w 映射到 c (strToChar[w] = c)

       返回 True
   ```

4. 复杂度：
   - 时间复杂度：$O(n)$，其中 $n$ 是字符串 $s$ 中单词的数量，因为我们需要遍历每个单词和对应的模式字符。
   - 空间复杂度：$O(m)$，其中 $m$ 是模式字符串和单词列表中不同字符和单词的数量，因为我们需要存储这些映射关系。
