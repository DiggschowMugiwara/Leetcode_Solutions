class Solution {
public:
    int maxScore(string s) {
        int tzeroes,tones,zeroes,ones;
        tzeroes = 0;
        tones = 0;
        for(int i = 0;i < s.size();i++){
            if(s[i] == '0'){ 
                tzeroes++;
                }
            else{
                tones ++;
            }
        }
        zeroes = 0;
        ones = tones;
        int max_score = 0;
        for(int i = 0;i < s.size()-1;i++){
            if(s[i] == '0'){
                zeroes ++;
            }
            else{
                ones--;
            }
            max_score = max(max_score,ones+zeroes);
        }
        return max_score;
        }
        
    };

// TIME COMPLEXITY : O(N)
// SPACE COMPLEXITY: O(1)
