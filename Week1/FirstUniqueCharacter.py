# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
# Example
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.

def main():
    # string = "aabnaa"
    string = input()
    result = -1

    # for i in range(len(string)-1):
    #     if string[i] not in string[i+1: ] and i != len(string) -1:
    #         print("Value {} found at {}".format(string[i],i))
    #         result = i
    #         break
    #     elif string[len(string)-1] not in string[:-1]:
    #
    #         print("Value {} found at {}".format(string[len(string) -1],len(string) -1))
    #         result = len(string) -1
    #         break
    #
    # if len(string) == 1:
    #     result = 0

    # strdict = {}
    # strset = set(string)
    # for let in strset:
    #     strdict[let] = []
    #     strdict[let].append(string.count)

    for i in range(len(string)):
        if string.count(string[i]) == 1:
            result = i
            break

    print(result)

    # newarr = set(string)
    # sorted(string)
    # print(string)


if __name__ == "__main__":
    main()
