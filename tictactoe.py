# Returns True if a given player wins in a given grid
def is_winning(player, grid):
    if grid[4] == player:
        if grid[0] == player and grid[8] == player:
            return True
        if grid[1] == player and grid[7] == player:
            return True
        if grid[2] == player and grid[6] == player:
            return True
        if grid[3] == player and grid[5] == player:
            return True
    elif grid[0] == player:
        if grid[3] == player and grid[6] == player:
            return True
        if grid[1] == player and grid[2] == player:
            return True
    elif grid[8] == player:
        if grid[6] == player and grid[7] == player:
            return True
        if grid[2] == player and grid[5] == player:
            return True
    return False


# Prints a grid based on characters in a string input
def print_grid(grid):
    print('---------')
    print('| ' + grid[0] + ' ' + grid[1] + ' ' + grid[2] + ' |')
    print('| ' + grid[3] + ' ' + grid[4] + ' ' + grid[5] + ' |')
    print('| ' + grid[6] + ' ' + grid[7] + ' ' + grid[8] + ' |')
    print('---------')


# Checks if user's input is allowed
def are_coords_valid(x, y, grid):
    if isinstance(x, int) and isinstance(y, int):
        if 0 < x < 4 and 0 < y < 4:
            cell = (x - 1) * 3 + y - 1
            if grid[cell] == '_':
                return True
            else:
                print('This cell is occupied! Choose another one!')
                return False
        else:
            print('Coordinates should be from 1 to 3!')
            return False
    else:
        print('You should enter numbers!')
        return False


# Generates new grid by placing given player in a square indicated by entered coordinates
def enter_coords(player, grid):
    coords = input('Enter the coordinates: ').split()
    x = int(coords[0])
    y = int(coords[1])

    while not are_coords_valid(x, y, grid):
        coords = input('Enter the coordinates: ').split()
        x = int(coords[0])
        y = int(coords[1])
    else:
        cell = (x - 1) * 3 + y - 1
        grid = grid[0:cell] + player + grid[cell + 1:]

    print_grid(grid)
    return grid


# Returns True if given input represents any of the ending game states
def game_over(grid):
    if abs(grid.count('X') - grid.count('O')) > 1 or is_winning('X', grid) and is_winning('O', grid):
        print('Impossible')
        return True
    else:
        if is_winning('X', grid):
            return True
        elif is_winning('O', grid):
            return True
        elif '_' not in grid:
            return True


def print_winner(grid):
    if is_winning('X', grid):
        print('X wins')
    elif is_winning('O', grid):
        print('O wins')
    elif '_' not in grid:
        print('Draw')


# Gameplay - starts with empty grid and X as a player
current_grid = '_________'
print_grid(current_grid)
current_player = 'X'

while not game_over(current_grid):
    current_grid = enter_coords(current_player, current_grid)
    game_over(current_grid)
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'
else:
    print_winner(current_grid)
