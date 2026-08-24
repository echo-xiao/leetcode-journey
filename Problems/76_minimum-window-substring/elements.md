# 76. 最小覆盖子串 · 要素

1. 定长还是变长：变长窗口，右指针一直扩到覆盖t，左指针在覆盖时收缩，窗口大小随内容动态变化

2. 进窗口更新：每次j右移一格就把s[j]计入win（win[c]+=1），扩大窗口纳入新字符

3. 出窗口时机：当win已经覆盖need（covered返回True）时就移动left收缩，移出s[i]时win[s[i]]-=1，若减到0就从win里删掉这个key，然后i+=1

4. 记结果时机：在while covered(win,need)为真的循环体里，每次收缩前先比较当前窗口长度j-i+1和minres，更短就更新minres和besti
