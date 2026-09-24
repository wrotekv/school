def get_binary_num(input):
    binarylist = []

    while input > 0:
        if input % 2 == 0:
            binarylist.append(0)
        elif input % 2 == 1:
            binarylist.append(1)
        input //= 2


    binarylist.reverse()
    return binarylist

if __name__ == '__main__':
    userinput = input("Insert the value that you want to convert to binary: ")
    

    print(get_binary_num(int(userinput)))