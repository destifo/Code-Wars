def calcIslandPerimeter(coord, grid):
    perimeter = 4
    x, y = coord
    ROWS = len(grid)
    COLS = len(grid[x])
    
    if x > 0 and grid[x-1][y] == 'X':
        perimeter -=1
        
    if x < ROWS-1 and grid[x+1][y] == 'X':
        perimeter -=1
        
    if y > 0 and grid[x][y-1] == 'X':
        perimeter -=1
        
    if y < COLS-1 and grid[x][y+1] == 'X':
        perimeter -=1
        
    return perimeter
    

def land_perimeter(arr):
    ROWS = len(arr)
    COLS = len(arr[0])
    tot_perimeter = 0
    
    for row in range(ROWS):
        for col in range(COLS):
            if arr[row][col] == 'X':
                tot_perimeter +=calcIslandPerimeter((row, col), arr)
                
    return f'Total land perimeter: {tot_perimeter}'