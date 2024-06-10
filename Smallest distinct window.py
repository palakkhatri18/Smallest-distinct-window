class Solution:
    def findSubString(self, str):
        # Your code goes here
        from collections import defaultdict
        
        # Step 1: Find all unique characters in the string
        unique_chars = set(str)
        unique_count = len(unique_chars)
        
        # Step 2: Use sliding window to find the smallest window containing all unique characters
        left = 0
        right = 0
        char_count = defaultdict(int)
        formed = 0
        min_length = float('inf')
        
        while right < len(str):
            # Add the current character to the window
            char_count[str[right]] += 1
            
            # If this character was needed and is now satisfied, increment the formed count
            if char_count[str[right]] == 1:
                formed += 1
            
            # While we have all unique characters in the window, try to shrink the window
            while formed == unique_count:
                # Update the minimum length if this window is smaller
                min_length = min(min_length, right - left + 1)
                
                # Remove the leftmost character from the window
                char_count[str[left]] -= 1
                if char_count[str[left]] == 0:
                    formed -= 1
                
                left += 1
            
            # Expand the window to the right
            right += 1
        
        return min_length if min_length != float('inf') else 0
  