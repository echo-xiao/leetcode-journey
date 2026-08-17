class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        tokens.sort()
        n = len(tokens)
        maxscore = 0
        left, right = 0, n-1
        score = 0
        while left <= right:
            if tokens[left] <= power:
                power -= tokens[left]
                score += 1
                left += 1
                maxscore = max(maxscore, score)
            elif score >= 1:
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break
        return maxscore