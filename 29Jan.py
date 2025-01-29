arr, res = [], []
while True:
        ele = [int(i) for i in input().split()]
        if not ele: 
            break
        arr.append(ele)
print(arr)
top, bottom = 0, len(arr)-1
left, right = 0, len(arr[0])-1
while left<=right and top<=bottom:
        # top elements from left to right
        for i in range(left, right+1):
            res.append(arr[top][i])
        top += 1
        # right elements from top to bottom
        for i in range(top, bottom+1):
            res.append(arr[i][right])
        right -= 1
        # bottom elements from right to left
        for i in range(right, left-1, -1):
            res.append(arr[bottom][i])
        bottom -= 1
        # left elements from bottom to top
        for i in range(bottom, top-1, -1):
             res.append(arr[i][left])
        left += 1
print(* res)
