# 220. 存在重复元素 III · 要素

1. 定长还是变长：定长窗口，窗口大小固定为indexDiff（按下标差限制，最多同时维护indexDiff个元素）

2. 进窗口更新：每处理一个新元素x（下标i）就把它加入窗口：算出它的桶号b=x//(valueDiff+1)，存入buckets[b]=x

3. 出窗口时机：当i>=indexDiff时，要把下标i-indexDiff对应的旧元素从buckets里删除（把它所在的桶清空），以保证窗口内只保留最近indexDiff个下标的元素

4. 记结果时机：在插入新元素之前先检查：自身桶b、左桶b-1、右桶b+1是否已有值且与x的差<=valueDiff，一旦满足立即返回True，遍历完都没命中则返回False
