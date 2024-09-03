class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        while len2:
            len1, len2 = len2, len1 % len2
        gcd_length = len1
        answer = str1[:gcd_length]
        if answer * (len(str1) // gcd_length) == str1 and answer * (len(str2) // gcd_length) == str2:
            return answer
        return ""