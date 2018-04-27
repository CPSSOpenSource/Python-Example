import sys

def main():
    i = 1
    j = 1
    print('started')
    while i < 10:
        while j < 10:
            print("%d x %d = %d" % (i, j , i*j))
            j = j + 1
        i = i + 1
        j = 1

if __name__ == "__main__":
    main()