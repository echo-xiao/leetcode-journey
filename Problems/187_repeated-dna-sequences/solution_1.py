class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        string = "".join(s)
        size = len(string)
        right = 9
        ans = []
        dic = {}
        right = 10


        if size < 10:
            return []

        while right <= size:
            res = string[right-10: right]
            if res not in dic:
                dic[res] = 1
            else:
                if dic[res] == 1:
                    ans.append(res)
                dic[res] += 1
            right += 1

        return ans
