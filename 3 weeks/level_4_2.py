import sys

def main():
    i = 1
    j = 2
    print('started')
    for i in range(1, 10):
        while j < 10:
            print("%d x %d = %d" % (i, j , i*j))
            j = j + 2
        j = 2

if __name__ == "__main__":
    main()