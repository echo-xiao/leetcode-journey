class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for i in range(0, len(words)):
            word = words[i]
            left, right = 0, len(word)-1
            is_palindromic = True

            while left < right:
                if word[left] != word[right]:
                    is_palindromic = False
                    break
                elif word[left] == word[right]:
                    left += 1
                    right -= 1

            if is_palindromic == True:
                return word
        return ""
        