class Solution:
    def maxDistance(self, colors: List[int]) -> int:

        i = 0
        j = len(colors)-1

        while i < len(colors):
            if colors[-1] != colors[i]:
                dis1 = abs(len(colors)-1-i)
                break
            i += 1

        while j > 0:
            if colors[0] != colors[j]:
                dis2 = j
                break
            j -= 1

        dis = max(dis1, dis2)
        return dis
