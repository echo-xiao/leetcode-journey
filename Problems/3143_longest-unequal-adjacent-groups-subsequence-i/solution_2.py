from typing import List, Tuple, Dict

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        
        ans = [words[0]]
        prev = groups[0]
        

        # for i in range(1, len(words)):
        #     curr = groups[i]
        #     if curr != prev:
        #         ans.append(words[i])
        #         prev = curr
        #     else:
        #         pass
        # return ans


        for i in range(1, len(words)):
            if groups[i] != groups[i-1]:
                ans.append(words[i])
            else:
                pass
        return ans