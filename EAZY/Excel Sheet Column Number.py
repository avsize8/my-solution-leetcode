class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0 
        for i , char in enumerate(reversed(columnTitle)):
            num = ord(char) - ord('A') + 1
            result += num * (26 ** i)
        return result



        