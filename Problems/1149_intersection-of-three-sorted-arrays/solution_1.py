class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        
        res = []
        p1, p2, p3 = 0, 0, 0

        while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3):
            val1, val2, val3 = arr1[p1], arr2[p2], arr3[p3]

            if val1 == val2 and val2 == val3:
                res.append(val1)
                p1 += 1
                p2 += 1
                p3 += 1
            else:
                if val1 < val2 or val1 < val3:
                    p1 += 1
                elif val2 < val1 or val2 < val3:
                    p2 += 1
                elif val3 < val1 or val3 < val2:
                    p3 += 1

        return res




            