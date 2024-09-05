func deleteGreatestValue(grid [][]int) int {
    for i := range grid {
        sort.Ints(grid[i])
    }    
    ans := 0
    for i := 0; i < len(grid[0]); i++ {
        max := grid[0][i]
        for _, row := range grid[1:] {
            if row[i] > max {
                max = row[i]
            }
        }
        ans += max
    }
    return ans
}
