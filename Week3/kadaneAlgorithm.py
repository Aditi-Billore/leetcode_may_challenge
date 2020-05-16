#maximum sum subarray using kedane's algorithm

def maximumSubArray(list1):
    currentSum = 0
    currentStart = currentEnd = 0
    maxStart = maxEnd = 0
    maxSum = 0

    for currentEnd, value in enumerate(list1):
        if currentSum <= 0:
            currentStart = currentEnd
            currentSum += value
        else:
            currentSum += value

        if maxSum< currentSum:
            maxSum = currentSum
            maxStart = currentStart
            maxEnd = currentEnd + 1

    return maxSum, maxStart, maxEnd


def main():
    list1 = [1,-2,3,-2]
    print(maximumSubArray(list1))

if __name__ == "__main__":
    main()
