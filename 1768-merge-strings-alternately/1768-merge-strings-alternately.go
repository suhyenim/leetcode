func mergeAlternately(word1 string, word2 string) string {
    var answer string
    var length int
    
    if len(word1) <= len(word2) {
        length = len(word1)
    } else {
        length = len(word2)
    }

    for i := 0; i < length; i++ {
        answer += string(word1[i])
        answer += string(word2[i])
    }

    answer += word1[length:]
    answer += word2[length:]

    return answer
}