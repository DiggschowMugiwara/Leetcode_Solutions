class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        forward_sums = [0]*len(boxes)
        backward_sums = [0]*len(boxes)
        balls = int(boxes[0])
        for i in range(1,len(boxes)):
            # if boxes[i-1] == "1":
            #     forward_sums[i] += (forward_sums[i-1]+balls)
            # else:
            forward_sums[i] += (forward_sums[i-1]+balls)
            # print(f"{i} and {forward_sums[i-1]+balls} and {boxes[i]}")
            if boxes[i] == "1":
                # print("hi")
                balls += 1
        balls = int(boxes[-1])
        for i in range(len(boxes)-2,-1,-1):
            # if boxes[i+1] == "1":
                # backward_sums[i] += (backward_sums[i+1]+1+balls)
            # else:
            backward_sums[i] += (backward_sums[i+1]+balls)
            if boxes[i] == "1":
                balls += 1
        print(backward_sums)
        print(forward_sums)
        return [a+b for a,b in zip(backward_sums,forward_sums)]




# TIME COMPLEXITY : O(N)
# SPACE COMPLEXITY : O(N)
