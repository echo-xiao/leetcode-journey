class Solution:
        
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        m = len(baskets)
        
        # 标记哪些篮子已经被使用，初始都为 False
        is_basket_used = [False] * m
        
        unplaced_count = 0
        
        # 从左到右遍历每一种水果
        for fruit_quantity in fruits:
            fruit_placed = False
            
            # 从左到右遍历每一个篮子
            for i in range(m):
                # 找到第一个可用的且容量足够的篮子
                if not is_basket_used[i] and baskets[i] >= fruit_quantity:
                    # 分配成功，将篮子标记为已使用
                    is_basket_used[i] = True
                    fruit_placed = True
                    break  # 找到后立即跳出内层循环，进入下一个水果的分配
            
            # 如果遍历完所有篮子都没有找到合适的
            if not fruit_placed:
                unplaced_count += 1
                
        return unplaced_count