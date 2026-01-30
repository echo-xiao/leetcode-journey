class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        dis = [] * len(mat)
        for i in range(0, len(mat)):
            lst = mat[i]

            if lst[0] == 0:
                dis.append((0, i))
                continue
                
            left, right = 0, len(lst)-1
            first, last = 0, 0
            
            while left <= right:
                mid = left + (right - left) // 2
                if lst[mid] == 1:
                    last = mid
                    left = mid + 1
                elif lst[mid] == 0:
                    right = mid - 1
            dis.append((last - first + 1, i))
        dis.sort()

        res=[]
        for i in range(k):
            res.append(dis[i][1])
        return res


