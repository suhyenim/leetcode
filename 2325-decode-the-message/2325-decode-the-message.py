class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        sub_table = {}
        i = 0
        for char in key:
            if char != ' ' and char not in sub_table.keys():
                sub_table[char] = alphabet[i] 
                i += 1     
        
        ans = []
        for char in message:
            if char == ' ':
                ans.append(' ')
            else:
                ans.append(sub_table[char])
        return ''.join(ans);