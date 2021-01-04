''' 3 ways to achieve:
    a. brute force, n^2 complexity
    b. sort then find nlogn time complexity
    c. hash table
'''

def containsDuplicate(nums):
    sort_nums = nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True

    return False



if __name__ == "__main__":
    nums=[3, 0,1, 5 ,2,3, -2]
    ans = containsDuplicate(nums)
    assert ans  == True
