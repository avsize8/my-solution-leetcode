class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanstr = ''.join(c.lower() for c in s if c.isalnum())
        return cleanstr == cleanstr[::-1]