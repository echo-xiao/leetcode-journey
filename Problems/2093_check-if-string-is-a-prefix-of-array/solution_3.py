class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        i, j = 0, 0
        tmp_str = ""
        while i < len(words):
            tmp_str += words[i]
            if tmp_str == s:
                return True
            i += 1
        return False