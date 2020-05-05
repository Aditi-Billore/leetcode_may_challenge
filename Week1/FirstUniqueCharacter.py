# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
# Example
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.

def main():
    string = input()
    result = -1

    for i in range(len(string)):
        if string.count(string[i]) == 1:
            result = i
            break

    print(result)

if __name__ == "__main__":
    main()
