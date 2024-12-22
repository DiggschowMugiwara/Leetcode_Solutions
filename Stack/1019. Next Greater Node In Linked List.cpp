/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    int number_of_nodes(ListNode* head){
        int length = 0;
        while(head){
            length ++;
            head = head->next;
        }
        return length;
    }


    vector<int> nextLargerNodes(ListNode* head) {
        vector<int> res(number_of_nodes(head),0);
        stack<pair<int,int>> stck;
        int index = 0;
        ListNode* currNode = head;
        while(currNode){
            int currval =currNode->val;
            while(!stck.empty() and stck.top().first<currval){
                auto [val,ind] = stck.top();
                stck.pop();
                res[ind] = currval;
            }
            stck.push({currval,index});
            index++;
            currNode = currNode->next;
        }
        return res;


    }
};

//TIME COMPLEXITY : O(N)
//SPACE COMPLEXIT: O(N)
