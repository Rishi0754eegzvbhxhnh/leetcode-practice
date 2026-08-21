class Solution:
    
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber > 0:
            columnNumber -= 1  # adjust for 1-based indexing
            result.append(chr(ord('A') + (columnNumber % 26)))
            columnNumber //= 26
        return "".join(reversed(result))