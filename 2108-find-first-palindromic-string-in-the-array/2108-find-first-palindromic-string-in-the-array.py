class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def is_palindrome(s):
            left = 0
            right = len(s) - 1

            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1

            return True
        
        for i in words:
            if is_palindrome(i):
                return i
        return  ""