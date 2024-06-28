class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones_count = s.count('1')
        zeros_count = s.count('0')
        
        if ones_count > 1:
            result = '1' * (ones_count - 1) + '0' * zeros_count + '1'
        elif ones_count == 1:
            result = '0' * zeros_count + '1'
        else:
            result = s
        
        return result
  