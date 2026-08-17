class Solution {
public:
    int sumOfSquares(vector<int>& nums) {
        int64_t ans = 0;

        for (int i = 1; i <= nums.size(); i++)
            ans += (nums.size() % i) == 0 ? nums[i-1] * nums[i-1] : 0;
        
        return ans;
    }
};