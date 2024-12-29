class Solution {
public:
    bool isPerfectSquare(int num) {
        if(num == 1){
            return true;
        }
        int n = num / 2;
        printf("%d",n);
        int l = 0;
        int r = n;
        while(l<=r){
            long int mid = (l+r)/2;
            if(mid*mid>num){
                r = mid - 1;
            }
            else if(mid*mid == num){
                return true;
            }
            else{
                l = mid + 1;
            }
        }
        return false;



    }
};

// TIME COMPLEXITY : O(LOGN)
// SPACE COMPLEXITY : O(1)
