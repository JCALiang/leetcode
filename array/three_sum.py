'''
    sort array, then use 2 pointers to find sum
    remove duplicates by checking duplicates in both loop
'''


def threeSum(nums):
    nums.sort()
    result=[]

    
    # don't forget to check boundary condition
    if len(nums) < 3:
        return []
    

    for i in range(len(nums)-1):
        # check for duplicates
        if i > 0 and nums[i] == nums[i-1]:
            continue
        head = i+1
        tail = len(nums)-1
        
        while head < tail:
            sum = nums[i] + nums[head] + nums[tail]

            if sum == 0:
                result.append([nums[i],nums[head] , nums[tail]])
                # check for duplicates
                while head < tail and nums[head] == nums[head+1]:
                    head+=1
                while head < tail and nums[tail] == nums[tail-1]:
                    tail-=1
                head+=1
                tail-=1

                
            elif sum < 0 :
                head+=1
            else:
                tail-=1

    return result


if __name__ == "__main__":
    test1= [-1,0,1,2,-1,-4]
    test2= [0,0,0]
    ans = threeSum(test2)
    print(ans)
    assert ans == [[0,0,0]]