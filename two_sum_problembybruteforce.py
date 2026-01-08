class Solution:
    def two_sum_bruteforce(self,nums,target):
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return[i,j]

solution = Solution()
nums=[2,5,7,4]
target=9
result=solution.two_sum_bruteforce(nums,target)
print(result)