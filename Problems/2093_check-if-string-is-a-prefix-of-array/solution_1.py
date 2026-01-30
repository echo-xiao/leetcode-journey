class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        j, i, w = 0, 0, ""
        while j < len(words):
            i += len(words[j])
            w += words[j]
            if len(s) == i and w == s:
                return True
            j += 1
        return False