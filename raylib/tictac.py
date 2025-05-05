import pyray
import time

# Constants
WIDTH = 600
HEIGHT = 600
CELL_SIZE = WIDTH // 3
FPS = 60
GRID_COLOR = pyray.Color(0, 0, 0, 255)
BG_COLOR = pyray.Color(255, 255, 255, 255)
X_COLOR = pyray.Color(255, 0, 0, 255)
O_COLOR = pyray.Color(0, 0, 255, 255)
TEXT_COLOR = pyray.Color(0, 0, 0, 255)

# Game state
board = [[' ' for _ in range(3)] for _ in range(3)]
current_player = 'X'
game_over = False
winner = None

def init_window():
    pyray.init_window(WIDTH, HEIGHT, "Tic-Tac-Toe")
    pyray.set_target_fps(FPS)

def draw_grid():
    for i in range(1, 3):
        # Vertical lines
        pyray.draw_line(i * CELL_SIZE, 0, i * CELL_SIZE, HEIGHT, GRID_COLOR)
        # Horizontal lines
        pyray.draw_line(0, i * CELL_SIZE, WIDTH, i * CELL_SIZE, GRID_COLOR)

def draw_symbols():
    for row in range(3):
        for col in range(3):
            x = col * CELL_SIZE + CELL_SIZE // 2
            y = row * CELL_SIZE + CELL_SIZE // 2
            symbol = board[row][col]
            if symbol == 'X':
                pyray.draw_line(x - 50, y - 50, x + 50, y + 50, X_COLOR)
                pyray.draw_line(x + 50, y - 50, x - 50, y + 50, X_COLOR)
            elif symbol == 'O':
                pyray.draw_circle_lines(x, y, 50, O_COLOR)

def draw_text(text, x, y, size):
    pyray.draw_text(text, x, y, size, TEXT_COLOR)

def check_winner():
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    # Check draw
    if all(board[row][col] != ' ' for row in range(3) for col in range(3)):
        return 'Draw'
    return None

def handle_input():
    if pyray.is_mouse_button_pressed(pyray.MOUSE_BUTTON_LEFT) and not game_over:
        mouse_x = pyray.get_mouse_x()
        mouse_y = pyray.get_mouse_y()
        row = mouse_y // CELL_SIZE
        col = mouse_x // CELL_SIZE
        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
            board[row][col] = current_player
            return True
    return False

def reset_game():
    global board, current_player, game_over, winner
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    game_over = False
    winner = None

def main():
    init_window()
    
    while not pyray.window_should_close():
        # Handle input
        if handle_input():
            global current_player
            current_player = 'O' if current_player == 'X' else 'X'
        
        # Check for winner
        global game_over, winner
        winner = check_winner()
        if winner:
            game_over = True
        
        # Draw
        pyray.begin_drawing()
        pyray.clear_background(BG_COLOR)
        
        draw_grid()
        draw_symbols()
        
        if game_over:
            if winner == 'Draw':
                draw_text("It's a Draw!", WIDTH//2 - 80, HEIGHT//2, 40)
            else:
                draw_text(f"{winner} Wins!", WIDTH//2 - 80, HEIGHT//2, 40)
            draw_text("Click to restart", WIDTH//2 - 100, HEIGHT//2 + 50, 20)
        
        pyray.end_drawing()
        
        # Handle restart
        if game_over and pyray.is_mouse_button_pressed(pyray.MOUSE_BUTTON_LEFT):
            time.sleep(0.2)  # Small delay to prevent immediate re-click
            reset_game()
    
    pyray.close_window()

if __name__ == "__main__":
    main()