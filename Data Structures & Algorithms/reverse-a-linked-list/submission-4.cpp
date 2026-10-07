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
    ListNode* reverseList(ListNode* head) {
        //how to reverse a linked list
        //you have head->next->next->next
        //so we can have a temporary node and a we have a new node i dont know why though? hmm ohh its because if we point head to some other node we would lose the information where head was pointing in the first place so we keep that information in temprorary node and when we're done pointing head to the new node we move to temporary next(which was head next) and store that node in temporary node. and we do this until temporary.next(it will be storing last node at that point ) will become null
    ListNode* curr = head;
    ListNode* prev = nullptr;
    ListNode* temp = nullptr;
    while (curr != nullptr) {
        temp = curr->next;
        curr->next = prev; 
        prev = curr;
        curr = temp;
    }
    return prev;
    }
    
};

