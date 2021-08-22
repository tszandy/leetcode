#include <iostream>
using namespace std;
// The API isBadVersion is defined for you.
// bool isBadVersion(int version);



class Solution {
    int bad;
public:
    Solution(int bad){
        bad(bad);
    }
    int firstBadVersion(int n) {
        long l=1,r=n;
        int m = (l+r)/2;
        while (l<r){
            if (isBadVersion(m)){
                l=l,r=m;
            }
            else{
                l=m+1,r=r;
            }
            m = (l+r)/2;
        }
        return m;
    }
private:
    bool isBadVersion(int version){
        return version>=bad
    }
};

int main(){
    cout << 123 << endl;
    //int n,bad;
    //n = 5;
    //bad = 4;
    //s1 = Solution(bad);
    //cout<<"test_case_1"<<s1.firstBadVersion(n)==bad<<endl;
    //n = 1;
    //bad = 1;
    //s1 = Solution(bad);
    //cout<<"test_case_1"<<s1.firstBadVersion(n)==bad<<endl;
    //n = 25;
    //bad = 3;
    //s1 = Solution(bad);
    //cout<<"test_case_1"<<s1.firstBadVersion(n)==bad<<endl;
}