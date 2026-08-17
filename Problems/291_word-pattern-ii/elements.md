# 291. 单词规律 II · 要素

1. 路径：路径是当前已经处理到的pattern下标pidx和s下标sidx，也就是charToStr这个字符到子串的映射表所记录的已分配方案

2. 选择列表：选择列表是当pattern当前字符char没有映射时，s从sidx开始所有可能的结尾位置end（sidx+1到len(s)），对应的候选子串sub，且sub不能已被usedStrs占用

3. 结束条件：结束条件是pidx等于pattern长度，此时若sidx也正好等于s长度则匹配成功返回True，否则返回False（还有剩余字符没匹配完）

4. 撤销：撤销的是给char新建立的映射（从charToStr中删除char）以及把对应子串sub从usedStrs集合中移除，恢复到选择前的状态
