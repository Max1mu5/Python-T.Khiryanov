def dot_product(N, vec1, vec2):
    result = 0
    for i in range(N):
        result += vec1[i] * vec2[i]

    return result

print(dot_product(3, [1, 2, 3], [4, 5, 6]))