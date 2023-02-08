class Solution {
public:
    void reorderList(ListNode* head) {
    struct ListNode* temp,* t, *ptr=head;
    stack <ListNode*> s;  

    if(!head or !head->next or !head->next->next)
    return;

    while(ptr->next->next)
    ptr=ptr->next;
        
    temp = ptr->next;
    ptr->next= NULL;

    while(temp){
        s.push(temp);
        temp=temp->next;
    }
    temp =head;

    while(temp and !s.empty()){
        t = s.top();
        t->next=temp->next;
        temp->next =t;
        s.pop();
        temp = t->next;
    }
    return;
}
};
