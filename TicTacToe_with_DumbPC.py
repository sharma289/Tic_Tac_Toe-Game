import random

class TicTac_withComputer():
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

    # Function for the user's turn
    def user_turn(self):
        try:
            position = int(input('Choose a position (1-9): ')) - 1
        except:
            print("Invalid move!! Try again")
            self.user_turn()

        if self.board[position] != 'O':
            self.board[position] = 'X'
            self.step += 1
        else:
            print('That position is already filled. Try again.')
            self.user_turn()

    def computer_turn(self):
        available_positions = [int(i) for i, value in enumerate(self.board) if value != 'X' and value != 'O']
        if available_positions:
            position = random.choice(available_positions)
            self.board[position] = 'O'
            self.step +=1

    # Main game loop
    def play_game(self):

        while not self.game_over:
            self.display_board()
            self.user_turn()

            if self.check_win('X'):
                self.display_board()
                print('Congratulations! You win!')
                self.game_over = True
            elif self.step == 9:
                self.display_board()
                print("It's a tie!")
                self.game_over = True
            else:
                self.computer_turn()
                if self.check_win('O'):
                    self.display_board()
                    print('The computer wins!')
                    self.game_over = True

if __name__ == "__main__":
    play_again = True
    print('-----Tic-Tac-Toe (with Computer) by Rajat Sharma-----')
    while play_again:
        play = TicTac_withComputer()
        play.play_game()
        input_ = input("\nDo you want to play again(y/n)? ")
        if input_ == 'n' or input_ == 'N':
            play_again = False
