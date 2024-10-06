def pascal_triangle(n):
    big = []
    
    if n <= 0:
        return big
    else:
        big = [[1]]
        
        if n >= 2:
            for i in range(1, n):
                row = [1]
                for j in range (1, i):
                    row.append(big[i-1][j-1] + big[i-1][j])
                row.append(1)
                big.append(row)
                        # big[i][j] = big[i-1][j-1] + big[i-1][j]
    return big