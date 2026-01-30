class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        dis = []

        for i in range(0, len(mat)):
            lst = mat[i]
            self.last = -1
            self.helper(lst, 0, len(lst)-1)
            dis.append((self.last + 1, i))

        dis.sort()
        res = []
        for j in range(k):
            res.append(dis[j][1])
        return res

        

    def helper(self, lst: List[int], left: int, right: int) -> List[int]:
        if left > right:
            return

        mid = left + (right - left) // 2
        if lst[mid] == 1:
            self.last = mid
            return self.helper(lst, mid+1, right)
        elif lst[mid] == 0:
            return self.helper(lst, left, mid-1)
        


