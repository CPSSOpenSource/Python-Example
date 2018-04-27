import sys

def main():
    i = 1
    j = 1
    print('started')
    for i in range(1, 10):
        while j < 10:
            if(j % 2 == 0):
                print("%d x %d = %d" % (i, j , i*j))
            j = j + 1
        j = 1

if __name__ == "__main__":
    main()