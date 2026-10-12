#include <vector>
#include <numeric>

class Solution {
    std::vector<int> subset;
    std::vector<std::vector<int>> res;
    std::vector<int> nums;
    int target;

public:
    std::vector<std::vector<int>> combinationSum(std::vector<int>& nums, int target) {
        this->nums = nums;
        this->target = target;
        subset.clear();
        res.clear();

        dfs(0);
        return res;
    }

private:
    void dfs(int i) {
        if (std::accumulate(subset.begin(), subset.end(), 0) == target) {
            res.push_back(subset);
            return;
        }
        else if (std::accumulate(subset.begin(), subset.end(), 0) > target || i >= nums.size()) {
            return;
        }

        subset.push_back(nums[i]);
        dfs(i);
        subset.pop_back();

        dfs(i + 1);
    }
};