#include <iostream>

using namespace std;
class Solution{
public:
    listNode* reverseList(listNode* head){
        ListNode* tmp;
        ListNode* pre=Null;
        ListNode* cur=head;
        while(cur){
            tmp = cur->next;//存储cur向右的指向
            cur->next=pre;//此时cur指向左侧啦？
            //现在更新pre的cur，都向后移动一下
            pre = cur;
            cur = temp;//再把cur的指向->
        }
        return pre;
    }

}
