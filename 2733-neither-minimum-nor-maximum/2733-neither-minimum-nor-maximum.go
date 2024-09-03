func findNonMinOrMax(nums []int) int {
    if len(nums) < 3 {
        return -1
    }
    sort.Ints(nums)
    return nums[1]
}