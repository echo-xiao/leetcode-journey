class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        n1 = len(arr1)
        n2 = len(arr2)
        i, j, k = 0, 0, n1

        for i in range(0, n1):
            for j in range(0, n2):
                dis = abs(arr1[i] - arr2[j])
                if dis <= d:
                    k -= 1
                    break
        return k
