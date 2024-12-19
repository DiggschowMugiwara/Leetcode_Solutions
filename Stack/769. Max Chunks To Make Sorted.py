class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        hsh = defaultdict(int)
        for i in range(len(arr)):
            hsh[arr[i]] = i
        arr2 = sorted(arr)
        no_of_chunks = 0
        max_ind = 0
        for i in range(len(arr)):
            curr_ind = hsh[arr2[i]]
            max_ind = max(max_ind,curr_ind)
            if max_ind == i:
                no_of_chunks += 1
            
        return no_of_chunks

  // Time Comlexity : O(nlogn)
  // Space Complexity : O(N)
