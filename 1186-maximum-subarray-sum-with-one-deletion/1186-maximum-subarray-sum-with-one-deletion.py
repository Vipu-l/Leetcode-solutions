class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        no_delete = arr[0]
        one_delete = float('-inf')
        result = arr[0]
        for i in range(1,n):
            prev_no_delete = no_delete
            prev_one_delete = one_delete
            no_delete = max(arr[i], prev_no_delete + arr[i])
            if(prev_one_delete == float('-inf')):
                v2 = arr[i]
            else:
                v2 = prev_one_delete + arr[i]
            one_delete = max(v2,prev_no_delete)
            result = max(result,max(one_delete,no_delete))
        return result