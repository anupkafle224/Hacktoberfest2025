import bisect

def length_of_LIS(nums):
    sub = []
    for num in nums:
        idx = bisect.bisect_left(sub, num)
        if idx == len(sub):
            sub.append(num)
        else:
            sub[idx] = num
    return len(sub)

# Example
print(length_of_LIS([10,9,2,5,3,7,101,18]))  # 4
