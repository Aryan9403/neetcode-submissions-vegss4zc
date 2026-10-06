class Solution {
public:
    int search(vector<int>& nums, int target) {
        //so you're given an array and target, array is already ascending, and we know this is binary search, the question here comes, is binary search only applied on ascending? hmm
        // so we declare a middle 
        // then we see if middle is greater and target, then right of middle eliminated
        //if middle is smaller than target, left of middle eliminated
        //if middle is equal to target then return True 
        // when we find middle, how is middle found in c++? 
        // so it is zero indexed, so we can find the length of array       
        int pointer2 = nums.size() - 1;
        int pointer1 = 0;
        
        // now how we code this
        while (pointer1 <= pointer2) {
            int mid = pointer1 + (pointer2 - pointer1) / 2;

            if (nums[mid] == target) {
                return mid;
            }         
            else if (nums[mid] > target) {
                pointer2 = mid - 1;
            }

            else if (nums[mid] < target) { 
                pointer1 = mid + 1;
            }
        }
        return -1;
}

};
 