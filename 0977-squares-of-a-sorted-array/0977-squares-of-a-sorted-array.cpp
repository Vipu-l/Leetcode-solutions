class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        vector<int> a;
        vector<int> b;
        for(int i=0;i<nums.size();i++){
            if(nums[i] >= 0){
                b.push_back(nums[i]);
            }
            else{
                a.push_back(nums[i]);
            }
        }
        if(a.size()==0){
            for(int i=0;i<nums.size();i++){
                nums[i] = nums[i] * nums[i];
            }
            return nums;
        }
        else if(b.size()==0){
            for(int i=0;i<nums.size();i++){
                nums[i] = nums[i]*nums[i];
            }
            reverse(nums.begin(),nums.end());
            return nums;
        }
        int i=0;
        int j=0;
        int id=0;
        int m = a.size();
        int n = b.size();
        vector<int> res(m+n);
        for(int i=0;i<m;i++)
        a[i]=a[i]*a[i];
        reverse(a.begin(),a.end());
        for(int i=0;i<n;i++)
        b[i]=b[i]*b[i];
        while(i<m and j<n){
            if(a[i] <= b[j]){
                res[id]=a[i];
                id++;
                i++;
            }
            else{
                res[id]=b[j];
                id++;
                j++;
            }
        }
        while(j<n){
            res[id] = b[j];
            id++;
            j++;
        }
        while(i<m){
            res[id]=a[i];
            id++;
            i++;
        }
        return res;
    }
};