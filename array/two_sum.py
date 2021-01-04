

def twoSum( nums, target):
    hash_table = dict()
    for i in range(len(nums)):
        if nums[i] in hash_table.keys() :
            return [ i, hash_table[nums[i]]]
        else:
            hash_table[target-nums[i]] = i



if __name__ == "__main__":
    nums = [3,2,4]
    target = 6
    print(twoSum(nums, target))