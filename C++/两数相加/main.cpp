#include <iostream>

using namespace std;

struct ListNode{
    int val;
    ListNode * next;
    ListNode(int x) : val(x), next(NULL);
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        carry = 0;
        l3 = ListNode(0);
        tmp1 = l1;
        tmp2 = l2;
        tmp3 = l3;
        while(tmp1 != NULL && tmp2 != NULL){

        }
    }
};

int main()
{
    cout << "Hello world!" << endl;
    return 0;
}
