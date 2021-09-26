def catalan(n, k):
    # base case
    if k == 1:
        return 1
    # calculate (n+k)/k for each number in the series
    return ((n + k) / k) * catalan(n, k - 1)


def main():
    # loop from 2 - 15
    for i in range(2, 16):
        # print the corresponding catalan number
        # I had to round to nearest integer because some values were
        # floats with a delta of .000000001
        print(f'Order {i} Catalan number = ' + str(int(round(catalan(i, i)))))


main()
