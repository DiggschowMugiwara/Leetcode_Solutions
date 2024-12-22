func maxDistinctElements(nums []int, k int) int {
    sort.Ints(nums)
    left_most := nums[0]-k;
    local_mini := nums[0]-k;
    res := 0;
    for i := 0;i<len(nums);i++{
        local_mini = nums[i]-k
        local_mini = max(local_mini,left_most);
        if local_mini > nums[i] + k{
            continue
        }
        local_mini += 1
        left_most = local_mini
        res += 1
    }
    return res


}

//TIME COMPLEXITY : O(NLOGN)
//SPACE COMPLEXITY : O(1)
