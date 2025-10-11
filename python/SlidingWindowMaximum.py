from collections import deque

def max_sliding_window(nums, k):
    dq = deque()
    res = []

    for i, num in enumerate(nums):
        # Remove smaller elements from the back
        while dq and nums[dq[-1]] < num:
            dq.pop()

        dq.append(i)

        # Remove elements outside the window
        if dq[0] <= i - k:
            dq.popleft()

        # Store max when window is at least size k
        if i >= k - 1:
            res.append(nums[dq[0]])

    return res

# Example
print(max_sliding_window([1,3,-1,-3,5,3,6,7], 3))  # [3,3,5,5,6,7]
