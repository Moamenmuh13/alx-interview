def pascal_triangle(n):
    if n <= 0:
        return []
    
    triangle = [[1]]  # Starting with the first row
    
    for i in range(1, n):
        prev_row = triangle[i - 1]
        row = [1]  # Start with 1
        
        # Fill in the middle values by summing two adjacent values from the previous row
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        
        row.append(1)  # End with 1
        triangle.append(row)
    
    return triangle
