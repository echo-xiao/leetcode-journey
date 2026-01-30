class Solution(object):
    def longestNiceSubstring(self, s):
        max_res = ""

        for k in range(1, 27):
            seen = {}
            left = 0
            matched = 0

            for right in range(0, len(s)):
                char_right = s[right]
                char_right_lower = char_right.lower()
                is_lower_right = char_right.islower()

                if char_right_lower not in seen:
                    seen[char_right_lower] = [0, 0]

                was_matched = seen[char_right_lower][0] > 0 and seen[char_right_lower][1] > 0

                if is_lower_right:
                    seen[char_right_lower][0] += 1
                else:
                    seen[char_right_lower][1] += 1
                    
                is_now_matched = seen[char_right_lower][1] > 0 and seen[char_right_lower][0] > 0

                if not was_matched and is_now_matched:
                    matched += 1
                

                while len(seen) > k:
                    
                    char_left = s[left]
                    char_left_lower = char_left.lower()
                    is_lower_left = char_left.islower()

                    was_matched = seen[char_left_lower][1] > 0 and seen[char_left_lower][0] > 0

                    if is_lower_left:
                        seen[char_left_lower][0] -= 1
                    else:
                        seen[char_left_lower][1] -= 1

                    is_now_matched = seen[char_left_lower][1] > 0 and seen[char_left_lower][0] > 0

                    if was_matched and not is_now_matched:
                        matched -= 1

                    if seen[char_left_lower][1] == 0 and seen[char_left_lower][0] == 0:
                        del seen[char_left_lower]


                    left += 1

                if matched == k and len(seen) == k:
                    res = s[left: right+1]
                    if len(res) > len(max_res):
                        max_res = res

        return max_res
                
                


                    



            