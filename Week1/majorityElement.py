# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.

# Input: [3,2,3]
# Output: 3


import math
import collections
def main():
    arr = [3,2,3]

    result = 0
    count = collections.Counter(arr)
    for index, num in enumerate(arr):
        if count[num] >= math.ceil(len(arr)/2):
            result = num
            break

    print(result)

if __name__ == "__main__":
    main()
