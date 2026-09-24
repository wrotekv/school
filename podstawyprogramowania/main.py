import time

def print_name(name):
    for i in range(len(name)):
        print(name[i], end="")
        time.sleep(0.5)

def generate_heart():
    # Loop through 6 rows
    for i in range(6):
        # Loop through 7 columns
        for j in range(7):
            # Evaluate the boundary conditions of the heart shape
            if (i == 0 and j % 3 != 0) or \
               (i == 1 and j % 3 == 0) or \
               (i - j == 2) or \
               (i + j == 8):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        # Advance to the next line after completing a row
        print()

if __name__ == '__main__':
    generate_heart()