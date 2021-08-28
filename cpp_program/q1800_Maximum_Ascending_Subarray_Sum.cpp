#include <iostream>
using namespace std;

#include <vector>

class Solution {
public:
    int maxAscendingSum(vector<int>& nums) {
        int n = nums.size();
        int largest = 0;
        int cur_sum = nums[0];
        for (int i=1;i<n;i++){
            largest = max(largest,cur_sum);
            if (nums[i]<=nums[i-1]){
                cur_sum = nums[i];
            }
            else{
                cur_sum += nums[i];
            }
        }
        largest = max(largest,cur_sum);
        return largest;
    }
};
// [10,20,30,5,10,50]
// [10,20,30,40,50]
// [12,17,15,13,10,11,12]
// [100,10,1]

int main(int argc, char *argv []){
    cout<<"Hello World"<<endl;
}