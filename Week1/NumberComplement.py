# Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.
# Input: 5
# Output: 2
# Explanation: Input: 101 (5) Output: 010 (2) (in decimal)

def main():
    decimalNum = int(input("Enter number"))

    #converting decimal to binary
    binaryNum = bin(decimalNum).replace("0b", "")

    #inverting binary number
    invertedBinary = 0
    for i in binaryNum:
        temp = 0 if int(i) == 1 else 1
        invertedBinary = invertedBinary*10 + temp

    #converting binary back to decimal
    decimalComplemented = int(str(invertedBinary),2)
    print (decimalComplemented)


if __name__ == "__main__":
    main()
