'''
sum of subarray,
as long as subarray is positive, we can make it bigger,
so only look for positive subarray, otherwise skip (start from current element)
'''


def maxSubArray(nums):

    for i in range(1, len(nums)):
        if(nums[i-1]>0):
            nums[i] = nums[i-1] + nums[i]

    return max(nums)

        



if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    ans = maxSubArray(nums)
    assert ans == 6