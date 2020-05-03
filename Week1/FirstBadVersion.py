# Given n = 5, and version = 4 is the first bad version.
#
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
#
# Then 4 is the first bad version.
# goal: acheive first bad version, with least calls to isBadVersion


def isBadVersion(list,version):
    return list[version]


def main():
    list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1]
    n = len(list)

    # initialise counters
    start = 0
    end = n
    ans = -1

    #binary search to find first bad version
    while (start <= end):
        mid = start + (end - start)//2

        if isBadVersion(list,mid):
            ans = mid
            end = mid -1
        else:
            start = mid+1
    print(ans)


if __name__ == "__main__":
    main()
