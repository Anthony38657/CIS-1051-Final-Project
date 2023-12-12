"""
* Tony L. Yang
* December 11, 2023
* Renju Game
*
* https://www.pygame.org/wiki/GettingStarted
* https://github.com/guanhui07/studyFiles/blob/master/python/Python%20和%20Pygame%20写游戏%20-%20从入门到精通.pdf
* https://thepythoncode.com/article/make-a-tic-tac-toe-game-pygame-in-python
"""
import pygame

# Constants representing different states on the board
NONE = 0
PLAYER_1 = 1
PLAYER_2 = 2

# Colors
BACKGROUND_COLOR = (240, 230, 140)
LINE_COLOR = (0, 0, 0)
PLAYER_1_COLOR = (0, 0, 0)
PLAYER_2_COLOR = (255, 255, 255)

class RenjuBoard(object):
    def __init__(self):
        """Initialize the Renju board."""
        self.board = [[NONE] * 15 for _ in range(15)]
        self.reset()

    def reset(self):
        """Reset the board to the initial state."""
        for row in range(15):
            for col in range(15):
                self.board[row][col] = NONE

    def move(self, row, col, black_color):
        """
        Make a move on the board.

        Args:
            row (int): Row index.
            col (int): Column index.
            black_color (bool): True if it's Player 1's turn, False for Player 2.

        Returns:
            bool: True if the move is valid and made successfully, False otherwise.
        """
        if self.board[row][col] == NONE:
            self.board[row][col] = PLAYER_1 if black_color else PLAYER_2
            return True
        return False

    def draw(self, screen):
        """Draw the Renju board on the screen using Pygame."""
        # Drawing lines for the board
        for h in range(1, 16):
            pygame.draw.line(screen, LINE_COLOR, [40, h * 40], [600, h * 40], 1)
            pygame.draw.line(screen, LINE_COLOR, [h * 40, 40], [h * 40, 600], 1)

        # Drawing the outer rectangle of the board
        pygame.draw.rect(screen, LINE_COLOR, [36, 36, 568, 568], 3)

        # Drawing center and corner circles
        circles = [[320, 320], [160, 160], [160, 480], [480, 160], [480, 480]]
        for circle in circles:
            pygame.draw.circle(screen, LINE_COLOR, circle, 5, 0)

         # Drawing player pieces on the board
        for row in range(15):
            for col in range(15):
                if self.board[row][col] != NONE:
                    color = PLAYER_1_COLOR if self.board[row][col] == PLAYER_1 else PLAYER_2_COLOR
                    pos = [40 * (col + 1), 40 * (row + 1)]
                    pygame.draw.circle(screen, color, pos, 18, 0)

def is_win(board):
    """
    Check if there is a winner on the board.

    Args:
        board (RenjuBoard): The Renju board object.

    Returns:
        bool: True if there is no winner yet, False otherwise.
    """
    for n in range(15):
        for seq in [board.board[n], [board.board[i][n] for i in range(15)]]:
            if seq.count(PLAYER_1) == 5:
                print('Player 1 Wins!')
                return False
            elif seq.count(PLAYER_2) == 5:
                print('Player 2 Wins!')
                return False
        for i in range(15):
            for j in range(15):
                # Check diagonals from top-left to bottom-right
                if i + 4 < 15 and j + 4 < 15:
                    if all(board.board[i + k][j + k] == PLAYER_1 for k in range(5)):
                        print('Player 1 Wins!')
                        return False
                    if all(board.board[i + k][j + k] == PLAYER_2 for k in range(5)):
                        print('Player 2 Wins!')
                        return False
                # Check diagonals from top-right to bottom-left
                if i + 4 < 15 and j - 4 >= 0:
                    if all(board.board[i + k][j - k] == PLAYER_1 for k in range(5)):
                        print('Player 1 Wins!')
                        return False
                    if all(board.board[i + k][j - k] == PLAYER_2 for k in range(5)):
                        print('Player 2 Wins!')
                        return False
                    
    return True

def main():
    # Main function to run the Renju game.
    pygame.init()
    pygame.display.set_caption('RENJU GAME')
    play_again = True

    while play_again:
        # Initialize the game board and Pygame screen
        board = RenjuBoard()
        black_color = True

        screen = pygame.display.set_mode((640, 640))
        screen.fill(BACKGROUND_COLOR)
        board.draw(screen)
        pygame.display.flip()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    play_again = False
                elif event.type == pygame.KEYUP:
                    pass
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    row = round((y - 40) / 40)
                    col = round((x - 40) / 40)
                    if board.move(row, col, black_color):
                        black_color = not black_color
                        screen.fill(BACKGROUND_COLOR)
                        board.draw(screen)
                        pygame.display.flip()
                        if not is_win(board):
                            running = False

        pygame.quit()

        # Ask the player if they want to play again
        play_again = input("Do you want to play again? (y/n): ").lower() == 'y'

if __name__ == '__main__':
    main()

