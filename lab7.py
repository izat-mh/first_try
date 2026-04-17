def triangle(n):
    result = [[1]]
    for _ in range(n - 1):
        prev = result[-1]
        new_row = [1]
        for i in range(len(prev) - 1):
            new_row.append(prev[i] + prev[i+1])
        new_row.append(1)
        result.append(new_row)
    return result
n = int(input())
print(triangle(n))