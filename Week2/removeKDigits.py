def main():
    num = "10"
    k = 2
    if k == len(num):
        num = 0
    else:
        for i in range(k):
            j = 0
            while j< (len(num)-1) and num[j] <= num[j+1]:

                j+=1
            num = ''.join([num[k] for k in range(len(num)) if k != j])

        while len(num) > 0 and num[0] =='0':
            num = ''.join([num[k] for k in range(len(num)) if k != 0])

        if len(num) == 0:
            num = 0
    print(num)

if __name__ == "__main__":
    main()
