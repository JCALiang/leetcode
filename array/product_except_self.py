'''
    break down the problem into sub-problems,
    product of pre-index position X product of post-index position
'''


def productExceptSelf(nums):
    N= len(nums)
    res =  [1] * N
    f, b = 1, 1

    for i in range(N):
        res[i] *= f
        res[N-1-i] *= b
        f *= nums[i]
        b *= nums[N-i-1]
        print(i, res, f, b)

    return res



if __name__ == "__main__":
    test1= [1,2,3,4]
    ans = productExceptSelf(test1)
    assert ans == [24,12,8,6]