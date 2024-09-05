func countStudents(students []int, sandwiches []int) int {
    passed := 0
    for len(students) != 0 && passed != len(students) {
        if students[0] != sandwiches[0] {
            passed++
            students = append(students[1:], students[0])
        } else {
            passed = 0
            students = students[1:]
            sandwiches = sandwiches[1:]
        }
    }
    return passed
}