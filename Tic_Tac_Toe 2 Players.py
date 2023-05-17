# Tic-Tac-Toe 2-Player-Game

class TicTac_2Players():
    def __init__(self):
        self.board = [str(i) for i in range(1,10)]
        self.current_player = 'X'
        self.step = 0
        self.game_over = False

    # Function to display the board
    def display_board(self):

        print('-------------',self.step)
        print(f'| {self.board[0]} | {self.board[1]} | {self.board[2]} |')
        print('-------------')
        print(f'| {self.board[3]} | {self.board[4]} | {self.board[5]} |')
        print('-------------')
        print(f'| {self.board[6]} | {self.board[7]} | {self.board[8]} |')
        print('-------------')

    # Function to check if any player has won
    def check_win(self,player):
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] == player:
                return True
        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] == player:
                return True
        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] == player:
            return True
        if self.board[2] == self.board[4] == self.board[6] == player:
            return True
        return False

    # Main game loop
    def play_game(self):

        while not self.game_over:
            if self.step == 9:
                self.display_board()
                print("It's a tie!")
                self.game_over = True
                continue
            
            self.display_board()
                
            print("It's", self.current_player, "turn.")
            try:
                position = int(input('Choose a position (1-9): ')) - 1
            except:
                print("Invalid move!! Try again!\n")
                continue

            if self.board[position] == 'X' or self.board[position] == 'O':
                print('That position is already filled. Try again!\n')
                
            else:
                self.board[position] = self.current_player

                if self.check_win(self.current_player):
                    self.display_board()
                    print('Congratulations!', self.current_player, 'wins!')
                    self.game_over = True
                else:
                    self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.step += 1

# Start the game
if __name__ == "__main__":
    play = tic_tac()
    play_again = True
    print('-----Tic-Tac-Toe (2 Players) by Rajat Sharma-----')
    while play_again:
        play = TicTac_2Players()
        play.play_game()
        input_ = input("\nDo you want to play again(y/n)? ")
        if input_ == 'n' or input_ == 'N':
            play_again = False
    
