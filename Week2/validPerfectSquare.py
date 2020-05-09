# Given a positive integer num, write a function which returns True if num is a perfect square else False.
#
# Note: Do not use any built-in library function such as sqrt.


# using binary search to check for perfect square
def isPrefectSquare(num):
    start = 1
    end = num
    while (start <= end) :
        mid = (start + end) // 2

        if (mid*mid == num) :
            return True

        if (mid * mid < num) :
            start = mid + 1
        else :
            # If mid*mid is greater than x
            end = mid-1

    return False



def main():
    num = int(input().strip())
    result = True if isPrefectSquare(num) else False
    print(result)


if __name__ == "__main__":
    main()
