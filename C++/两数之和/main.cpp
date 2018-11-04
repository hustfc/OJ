#include <iostream>
#include <vector>

using namespace std;

vector<int> towSum(vector<int> & nums, int target){
    vector<int> indexs;
    for(int i = 0;i < nums.size();i ++){
        for(int j = i + 1;j < nums.size();j ++){
            if(nums[i] + nums[j] == target){
                indexs.push_back(i);
                indexs.push_back(j);
            }
        }
    }
    return indexs;
}

int main()
{
    vector<int> nums;
    vector<int> indexs;
    int target;
    char t;
    int n;
    while((t = cin.get()) != '\n'){
        cin >> n;
        nums.push_back(n);
    }
    cin >> target;
    indexs = towSum(nums, target);
    cout << indexs[0] << ", " << indexs[1];
}
