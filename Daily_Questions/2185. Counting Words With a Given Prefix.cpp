class Solution {
public:
    bool startsWith(string pre,string word){
        if(word.find(pre) == 0){
            return true;
        }
        return false;
    }



    int prefixCount(vector<string>& words, string pref) {
        int ct = 0;
        for(int i = 0; i < words.size();i++){
            if(startsWith(pref,words[i])){
            ct++;
        }
    }
    return ct;
    }

};


// TIME COMPLEXITY : O(N.M)
// SPACE COMPLEXITY : O(1)
