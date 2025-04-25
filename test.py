def find_squares(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    squares = []

    for i in range(rows):
        for j in range(cols):
            max_k = min(rows - i, cols - j)

            for k in range(2, max_k + 1):
                is_square = True

                for x in range(i, i + k):
                    for y in range(j, j + k):
                        if matrix[x][y] != 1:
                            is_square = False
                            break
                    if not is_square:
                        break

                if is_square:
                    squares.append((i, j, k))

    return squares


def remove_nested_squares(squares):
    squares.sort(key=lambda x: x[2], reverse=True)

    result = []

    for square in squares:
        i_A, j_A, k_A = square
        is_nested = False

        for i_B, j_B, k_B in result:
            if i_B <= i_A and j_B <= j_A and i_A + k_A <= i_B + k_B and j_A + k_A <= j_B + k_B:
                is_nested = True
                break

        if not is_nested:
            result.append(square)

    return result


matrix = [
    [1, 1, 1, 0],
    [1, 1, 1, 0],
    [1, 1, 1, 0],
    [0, 0, 0, 0]
]

result = remove_nested_squares(find_squares(matrix))
print("Найденные квадраты:", result)