def nextSmallerElement(arr, n):
    # Write your code here.
    ans = []
    s = []
    for i in range(n-1, -1, -1):
        if len(s) == 0:
            ans.append(-1)
        else:
            while len(s) > 0 and s[-1] >= arr[i]:
                s.pop()
            if len(s) == 0:
                ans.append(-1)
            else:
                ans.append(s[-1])
        s.append(arr[i])
    ans = ans[::-1]
    return ans
