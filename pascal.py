def pascal(n, k):
    # base case
    # if we are at the first element OR if we are at the last element
    if k == 0 or k == n:
        return 1
    # Recursive call
    # using pascals rule    |n| = |n-1| + |n-1|  Imagine that's all on the same line
    #                       |k| = |k-1| + | k |  and the pipes are multiline parens
    else:
        return pascal(n - 1, k - 1) + pascal(n - 1, k)


def main():
    # loop from 0 to however many rows we have - here its 10
    for i in range(10):
        row = []
        # loop our elements plus 1 since the next line will grow by one in length
        for j in range(i + 1):
            # we are returned the current positions value so we append it to a list
            row.append(pascal(i, j))
        # print the current row of our calculated values
        print(row)


main()
