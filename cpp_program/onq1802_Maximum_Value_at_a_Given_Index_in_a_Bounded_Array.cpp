class Solution {
public:
    int maxValue(int n, int index, int maxSum) {
        int sum = 0;
        for (int i = 0;i<n;i++){
            if (i <=index){
                sum+=i;
            }
            else{
                sum+=2*index-i;
            }
        }
        return (maxSum-sum)/n+index;
    }
};