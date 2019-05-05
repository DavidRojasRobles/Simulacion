import numpy as np
import math

def num_ways(N, X):
    if N == 0: return 1
    nums = np.zeros(len(X)+1)
    nums[0] = 1
    for i in range(1, N+1):
        total = 0
        for j in X:
            if i-j >= 0:
                total += nums[i-j]
            nums[j] = total
    return total



N = 8
ps = [1,2]

print num_ways(N, ps)
