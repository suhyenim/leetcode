func maximumOddBinaryNumber(s string) string {
    ones_count := 0
    zeros_count := 0
    for i := 0; i < len(s); i++ {
        if s[i] == '1'{
            ones_count++
        } else {
            zeros_count++
        }
    }
    return strings.Repeat("1", ones_count-1) + strings.Repeat("0", zeros_count) + "1"
}