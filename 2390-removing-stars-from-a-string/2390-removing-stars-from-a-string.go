func removeStars(s string) string {
	stack := []byte{}
	for i := 0; i < len(s); i++ {
		char := s[i]
		if char == '*' {
			if len(stack) > 0 {
				stack = stack[:len(stack) - 1]
			}
		} else {
			stack = append(stack, char)
		}
	}
	return string(stack)
}