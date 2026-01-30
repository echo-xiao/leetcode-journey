class Solution:
    def distMoney(self, money: int, children: int) -> int:
        
        # 1. 基础情况：钱不够分
        # 连每人 1 美元都满足不了
        if money < children:
            return -1
        
        # --- 从现在开始，我们知道 money >= children ---
        
        # 2. 理想情况：先给每人 1 美元
        # 剩下 money - children 美元，用来把 1 美元“升级”到 8 美元
        # 每次“升级”需要 7 美元
        
        # 3. 棘手情况 A：钱太多
        # 如果钱多到，给每个人 8 美元都还有剩 (money > 8 * children)
        # 为了把钱花完，必须至少有 1 个人拿的超过 8 美元
        # 所以最多只能有 children - 1 个人拿到 8 美元
        if money > 8 * children:
            return children - 1
            
        # 4. 棘手情况 B：唯一的“死局”
        # 这种情况是：你刚好能凑出 (children - 1) 份 8 美元，
        # 此时剩下 1 个孩子（拿着 $1），和 $3 的余钱。
        # 你必须把这 $3 给最后这个孩子，导致他拿到 $1 + $3 = $4，违反规则。
        #
        # 这种情况的 money 总数是：(children - 1) * 8 + 4 = 8 * children - 8 + 4 = 8 * children - 4
        #
        # 此时，我们不能让 children - 1 个人拿 $8，只能退一步，
        # 让 children - 2 个人拿 $8。
        if money == 8 * children - 4:
            return children - 2

        # 5. 所有其他“正常”情况
        # 除去以上所有特例，剩下的都可以用“贪心”策略解决：
        # 先给每人 $1，然后用剩下的钱 (money - children) 
        # 尽可能多地去“升级”（每次 $7）。
        #
        # 比如 money = 20, children = 3
        # 1. 每人 $1 (剩 $17)
        # 2. 升级第 1 个人 (花 $7, 剩 $10)
        # 3. 升级第 2 个人 (花 $7, 剩 $3)
        # 4. 剩下 $3 和 1 个孩子。把 $3 全给他，他总共 $1 + $3 = $4。
        #    -> 触发了情况 4 (8*3 - 4 = 20)，所以返回 children - 2 = 1
        #
        # 比如 money = 13, children = 3
        # 1. 每人 $1 (剩 $10)
        # 2. 升级第 1 个人 (花 $7, 剩 $3)
        # 3. 剩下 $3 和 2 个孩子。可以 1 个给 $1，1 个给 $2。
        #    他们最终拿到 $1+$1=$2 和 $1+$2=$3。都合法。
        #    (13 - 3) // 7 = 10 // 7 = 1。返回 1。
        
        return (money - children) // 7