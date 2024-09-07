class Solution:
    def finalValueAfterOperations(self, operations) -> int:
        return sum(44 - ord(o[1]) for o in operations)