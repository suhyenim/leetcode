class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = ""
        length = len(word1) if len(word1) <= len(word2) else len(word2)
        for i in range(length):
            answer += word1[i]
            answer += word2[i]
        answer += word1[length:]    
        answer += word2[length:]    
        return answer

