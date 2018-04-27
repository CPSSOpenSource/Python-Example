import sys

def main():
    print('started')
    for i in range(1, 10):
        for j in range(1, 10):
            print("%d x %d = %d" % (i, j , i*j))

if __name__ == "__main__":
    main()