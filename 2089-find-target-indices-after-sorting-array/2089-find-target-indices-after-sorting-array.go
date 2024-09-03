func targetIndices(nums []int, target int) []int {
    var ans []int
    sort.Ints(nums)
    for i := 0; i < len(nums); i++ {
        if nums[i] == target {
            ans = append(ans, i)
        }
    }
    return ans
}