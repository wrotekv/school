def get_binary_num(input):
    binarylist = []

    while input > 0:
        if input % 2 == 0:
            binarylist.append(0)
        else:
            binarylist.append(1)
        input //= 2


    binarylist.reverse()
    return binarylist

def get_8_num(input):
    list = []

if __name__ == '__main__':
    userinput = input("Insert the value that you want to convert to binary: ")
    

    print(get_binary_num(int(userinput)))