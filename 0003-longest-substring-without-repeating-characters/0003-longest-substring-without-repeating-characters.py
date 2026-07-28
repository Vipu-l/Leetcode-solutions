class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
         
        left = 0
        last_index = {}
        max_len = 0

        for right, ch in enumerate(s):
            # If character is already inside current window,
            # move left just after its previous position
            if ch in last_index and last_index[ch] >= left:
                left = last_index[ch] + 1

            # Store/update latest position of character
            last_index[ch] = right

            # Calculate current window length
            max_len = max(max_len, right - left + 1)

        return max_len