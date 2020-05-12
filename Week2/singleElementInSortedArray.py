# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
# Find this single element that appears only once.

import collections

def main():
    list1 = [1,1,2,2,3,3,4,5,5]
    dict1 = collections.Counter(list1)
    for index, num in enumerate(list1):
        if dict1[num] == 1:
            result = num
            break

    print(result)

if __name__ == "__main__":
    main()
