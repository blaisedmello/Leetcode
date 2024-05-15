class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = curr_len = 0
        seen = []
        
        for i in s:
            if i in seen:
                x = seen.pop(0)
                curr_len -= 1
                while x != i:
                    x = seen.pop(0)
                    curr_len -= 1
            seen.append(i)
            curr_len += 1

            max_len = max(max_len, curr_len)

        return max_len