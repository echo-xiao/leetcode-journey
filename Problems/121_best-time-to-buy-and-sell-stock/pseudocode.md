# 121. 买卖股票的最佳时机 · 解题思路与伪代码

1. 一句话直击本质：通过遍历价格数组，记录到当前为止的最低价格，并计算可能的最大利润。

2. 综合思路：
   - **迭代法**：大多数版本采用迭代法，通过遍历价格数组，动态更新最低价格和最大利润。
   - **递归法**：版本 3 使用递归方法，通过递归调用计算每一天的最大利润，结合当前价格与历史最低价格。

3. 全量伪代码：
   - **迭代法伪代码**：
     ```
     初始化 minPrice 为正无穷
     初始化 maxProfit 为 0 或 -1
     对于每个价格 price 在数组 prices 中：
         更新 minPrice 为 min(minPrice, price)
         计算当前利润 currentProfit 为 price - minPrice
         更新 maxProfit 为 max(maxProfit, currentProfit)
     返回 maxProfit
     ```
   - **递归法伪代码**：
     ```
     定义函数 solve(prices, i, minPrice):
         如果 i 等于 prices 的长度:
             返回 0
         计算 profitToday 为 prices[i] - minPrice
         更新 newMinPrice 为 min(minPrice, prices[i])
         计算 profitLater 为 solve(prices, i+1, newMinPrice)
         返回 max(profitToday, profitLater)
     
     调用 solve(prices, 0, 正无穷)
     返回 max(0, solve 的结果)
     ```

4. 复杂度：
   - **时间复杂度**：对于所有版本，时间复杂度均为 $O(n)$，其中 $n$ 是价格数组的长度，因为每个价格只被访问一次。
   - **空间复杂度**：
     - **迭代法**：空间复杂度为 $O(1)$，因为只使用了常数个额外变量。
     - **递归法**：空间复杂度为 $O(n)$，因为递归调用栈的深度最多为 $n$。
