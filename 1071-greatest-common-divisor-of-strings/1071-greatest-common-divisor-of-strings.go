func gcdOfStrings(str1 string, str2 string) string {                   
    len1, len2 := len(str1), len(str2)
    for len2 != 0 {
        len1, len2 = len2, len1 % len2
    }
    gcdLength := len1
    answer := str1[:gcdLength]
    if strings.Repeat(answer, len(str1)/gcdLength) == str1 && strings.Repeat(answer, len(str2)/gcdLength) == str2 {
        return answer
     }
    return ""
}