func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func maxScoreSightseeingPair(values []int) int {
    n := len(values)
    if n < 2{
        return -1
    }
    maxi := values[0]
    res := math.MinInt
    for i := 1;i<len(values);i++{
        res = max(res,maxi + values[i]-i)
        maxi = max(maxi,values[i]+i)
    }
    return res


}

// TIME COMPLEXITY : O(N)
// SPACE COMPLEXITY : O(1)
