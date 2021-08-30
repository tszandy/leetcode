#include<iostream>
#include<vector>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    bool isSubPath(ListNode* head, TreeNode* root) {
        if (head == nullptr){
            return true;
        }
        if (root == nullptr){
            return false;
        }
        if(head->val == root->val){
            if (sub_path(head->next,root->left) || sub_path(head->next,root->right)){
                return true;
            }
        }
        return isSubPath(head,root->left) || isSubPath(head,root->right);
        
        
        
    }
    bool sub_path(ListNode* list_node,TreeNode* tree_node){
        if (list_node == nullptr){
            return true;
        }
        if (tree_node == nullptr){
            return false;
        }
        if(list_node->val == tree_node->val){
            if (sub_path(list_node->next,tree_node->left) || sub_path(list_node->next,tree_node->right)){
                return true;
            }
        }
        return false;
    }
};

int main(int argc, char *argv []){
    cout<<"Hello World"<<endl;
}