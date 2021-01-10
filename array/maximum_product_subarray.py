
'''
    max product logic as follow:
        product can either be 0 or +ve or -ve
        so need to keep track of min and max possible sub_products
'''

def maxProduct(nums):
    sub_min = sub_max = max_product = nums[0]
    
    for i in range(1, len(nums)):
        curr = nums[i]
        temp_max = sub_max
        sub_max = max(sub_min * curr , sub_max * curr , curr)
        sub_min = min(sub_min * curr , temp_max * curr , curr)
      
        if sub_max > max_product: max_product = sub_max
    return max_product



if __name__ == "__main__":
    test= [2,3,-2,4]
    test2=[-4,-3,-2]
    ans = maxProduct(test2)
    assert ans == 12

    