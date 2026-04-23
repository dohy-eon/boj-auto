MOD = 1000000007

def mat_mul(a, b):
    return [
        [
            (a[0][0]*b[0][0] + a[0][1]*b[1][0]) % MOD,
            (a[0][0]*b[0][1] + a[0][1]*b[1][1]) % MOD
        ],
        [
            (a[1][0]*b[0][0] + a[1][1]*b[1][0]) % MOD,
            (a[1][0]*b[0][1] + a[1][1]*b[1][1]) % MOD
        ]
    ]

def mat_pow(matrix, n):
    if n == 0:
        return [[1, 0], [0, 1]]
    
    if n == 1:
        return matrix
    
    half = mat_pow(matrix, n // 2)
    result = mat_mul(half, half)
    
    if n % 2 == 1:
        result = mat_mul(result, matrix)
    
    return result

def fibonacci(n):
    if n == 0:
        return 0

    base = [[1, 1], [1, 0]]
    result = mat_pow(base, n - 1)
    return result[0][0]

n = int(input())
print(fibonacci(n))