func countSubarrays(nums []int) int {
    res := 0
for i := 0;i < len(nums)-2;i++{

    if(nums[i+1]%2 == 0 && nums[i]+nums[i+2] == nums[i+1]/2){
        res = res + 1
    } 

}
return res
}
