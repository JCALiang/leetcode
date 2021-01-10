
'''
    use nlogn to search for medium
    then search for target
'''

def search_slow(nums, target):

    result=-1
    start = 0
    end = len(nums)-1
    rotate = 0


    while start <= end:
        middle = (start + end )//2
        
        if target == nums[middle]:
            return middle
        # if left is sort and lie in left
        
        elif nums[start] <= nums[middle]:
            if target<nums[middle] and target>=nums[start]:
                end=middle -1
            else:
                start=middle +1
            
        else:
            if target>nums[middle] and target<=nums[end]:
                start=middle +1
            else:
                end=middle -1
            

    return result



def search(nums, target):

    low, high= 0, len(nums)-1

    while low < high:
        mid = (low + high )//2
        if nums[high] < nums[mid]:
            low = mid + 1
        else:
            high = mid

    rotate = low

    nnums = nums[rotate:]+nums[:rotate]
    print(nnums)

    low, high= 0, len(nums)-1
    while low <= high :
        mid = (low + high )//2
        if nnums[mid] == target:
            return (mid+rotate)%len(nums)
        elif (target > nnums[mid]):
            low = mid + 1
        else:
            high = mid -1
    return -1




if __name__ == "__main__":
   test= [4,5,6,7,0,1,2]
   test2=[1]
   ans=search(test, 0)
   assert ans == 4
   ans2 = search(test2, 0)
   assert ans2 == -1