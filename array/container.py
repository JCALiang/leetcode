

def maxArea(height):
    left = 0
    right = len(height) -1
    maximum_vol = 0

    while left < right:
        temp_vol = min(height[left], height[right]) * (right -left)
        if temp_vol > maximum_vol:
            maximum_vol = temp_vol

        if height[left] < height[right]:
            left+=1
        else:
            right-=1
    
    return maximum_vol



if __name__ == "__main__":
    test1=[5,1,2,3,4,5]
    test2=[3,5,1,2,5]
    ans1 = maxArea(test1)
    ans2=maxArea(test2)
    assert ans1 == 25
    assert ans2 == 15