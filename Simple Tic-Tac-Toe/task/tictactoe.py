def state(player, grid):
    winning = player + ' wins'
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


def print_grid(grid):
    print('---------')
    print('| ' + grid[0] + ' ' + grid[1] + ' ' + grid[2] + ' |')
    print('| ' + grid[3] + ' ' + grid[4] + ' ' + grid[5] + ' |')
    print('| ' + grid[6] + ' ' + grid[7] + ' ' + grid[8] + ' |')
    print('---------')


def enter_coords(player, grid):
    incorrect_input = True
    while incorrect_input:
        coords = input('Enter the coordinates: ').split()
        x = int(coords[0])
        y = int(coords[1])

        if isinstance(x, int) and isinstance(y, int):
            if 0 < x < 4 and 0 < y < 4:
                cell = (x - 1) * 3 + y - 1
                if grid[cell] == '_':
                    grid = grid[0:cell] + player + grid[cell+1:]
                    incorrect_input = False
                else:
                    print('This cell is occupied! Choose another one!')
            else:
                print('Coordinates should be from 1 to 3!')
        else:
            print('You should enter numbers!')
    print_grid(grid)
    return grid


def game_over(grid):
    if abs(grid.count('X') - grid.count('O')) > 1 or state('X', grid) and state('O', grid):
        print('Impossible')
        return True
    else:
        if state('X', grid):
            return True
        elif state('O', grid):
            return True
        elif '_' not in grid:
            return True


def print_result(grid):
    if state('X', grid):
        print('X wins')
    elif state('O', grid):
        print('O wins')
    elif '_' not in grid:
        print('Draw')


grid_play = '_________'
print_grid(grid_play)
player = 'X'

while not game_over(grid_play):
    grid_play = enter_coords(player, grid_play)
    game_over(grid_play)
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
else:
    print_result(grid_play)
