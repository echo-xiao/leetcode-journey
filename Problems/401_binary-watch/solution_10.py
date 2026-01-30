class Solution:
    # --- Class-level variables to hold state ---
    results: List[str]
    leds: List[tuple]
    target_count: int

    def _backtrack(self, start_index: int, count: int, hour: int, minute: int):
        """
        独立的回溯辅助函数
        start_index: 为避免重复，从该索引开始选择
        count:       当前已点亮的灯数
        """
        # 剪枝：如果时间和已选灯数无效，提前返回
        if hour > 11 or minute > 59:
            return

        # 基线条件：已经选够了 n 个灯
        if count == self.target_count:
            # 找到了一个完整的组合，保存结果
            self.results.append(format_time(hour, minute))
            return # 停止这一路的递归，因为我们只要 n 个

        # --- 决策循环 ---
        # 从 start_index 开始，到 9 结束
        for i in range(start_index, 10):
            val, type = self.leds[i]
            
            # 1. “选择” 第 i 个灯并 “探索”
            if type == "H":
                self._backtrack(i + 1, count + 1, hour + val, minute)
            else:
                self._backtrack(i + 1, count + 1, hour, minute + val)
            
            # 2. “撤销” 是隐式自动完成的

    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        # 1. 初始化类变量
        self.results = []
        self.leds = [
            (1, "H"), (2, "H"), (4, "H"), (8, "H"),
            (1, "M"), (2, "M"), (4, "M"), (8, "M"), (16, "M"), (32, "M")
        ]
        self.target_count = turnedOn
        
        # 2. 调用辅助函数
        self._backtrack(0, 0, 0, 0)
        
        # 3. 返回结果
        return self.results


from typing import List

def format_time(hour: int, minute: int) -> str:
    """辅助函数：将(h, m)格式化为 "h:mm" 字符串"""
    return f"{hour}:{minute:02d}"