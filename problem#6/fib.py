def fibonacci(n):
    #write your code here
    if n < 0:
        return -1
    if n == 0:
        return 0
    if n == 1:
        return 1
    first = 0
    second = 1
    result = 0
    while n >= 2:
        result = first + second
        first = second
        second = result
        n -= 1
    return result


if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')