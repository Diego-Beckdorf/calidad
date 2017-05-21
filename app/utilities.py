from console import Console

def is_integer(value):
    try:
        _ = int(value)
        return True
    except ValueError:
        return False


def is_coordinates_inside_bounds(board, row, column):
    console = Console()
    if row >= board.dimension:
        console.write_line(message='Error: Row index outside board bounds.')
        return False
    if column >= board.dimension:
        console.write_line(message='Error: Column index outside board bounds.')
        return False
    return True

