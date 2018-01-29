grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def x_y_1(grid):
    for y in range(9):
        for x in [0]:
            print(grid[y][x],end='')
    print(end='\n')
def x_y_2(grid):
    for y in range(9):
        for x in [1]:
            print(grid[y][x],end='')
    print(end='\n')
def x_y_3(grid):
    for y in range(9):
        for x in [2]:
            print(grid[y][x],end='')
    print(end='\n')
def x_y_4(grid):
    for y in range(9):
        for x in [3]:
            print(grid[y][x],end='')
    print(end='\n')
def x_y_5(grid):
    for y in range(9):
        for x in [4]:
            print(grid[y][x],end='')
    print(end='\n')
def x_y_6(grid):
    for y in range(9):
        for x in [5]:
            print(grid[y][x],end='')
    print(end='\n')
x_y_1(grid)
x_y_2(grid)
x_y_3(grid)
x_y_4(grid)
x_y_5(grid)
x_y_6(grid)


