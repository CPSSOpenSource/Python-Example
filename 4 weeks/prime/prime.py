import sys


def prime_sum(n):
    sum = 0
    for i in range(2, n + 1):
        for j in range(i-1, 0, -1):
            if j == 1:
                sum = sum + i
            if i % j == 0:
                break
    return sum


def main():
    while True:
        n = int(input("숫자를 입력하세요: "))
        if n == 0 or n == 1:
            print("더할 숫자가 없습니다!")
            continue

        if n < 0 or n > 1000:
            print("범위를 벗어났습니다. 프로그램을 종료합니다.")
            sys.exit(0)

        print("2부터 %d까지의 모든 소수 합은 %d입니다." % (n, prime_sum(n)))


if __name__== "__main__":
    main()