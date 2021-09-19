def top(size, shift):
    for i in range(shift, size - shift):
        yield i


def right(size, shift):
    pass


def bottom(size):
    pass


def left(size):
    pass


def rotate(m):
    size = len(m)
    for shift in range(size // 2):
        for i in range(size - 1 - 2 * shift):
            m[shift][shift + i],\
            m[shift + i][size - 1 - shift],\
            m[size - 1 - shift][size - 1 - shift - i], \
            m[size - 1 - shift - i][shift]\
            =\
            m[size - 1 - i - shift][shift],\
            m[shift][shift + i],\
            m[shift + i][size - 1 - shift],\
            m[size - 1 - shift][size - 1 - i - shift]


def print_matrix(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(str(m[i][j]).zfill(2), end=' ')
        print()


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
    print_matrix(matrix)
    print()
    rotate(matrix)
    print()
    print_matrix(matrix)
