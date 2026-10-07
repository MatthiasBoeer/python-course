import time

from Checkers.Board import Board
from Checkers.Checker import Checker
from Checkers.Player import Player

class Game:

    def __init__(self, player1: Player, player2: Player):
        self.players = [player1, player2]
        self.board = Board()
        self.index = 0
        self.total_moves = 0
        self.start_time = None
        self.end_time = None
        self.winner: Player | None = None
        self.is_finished = False

    @property
    def active_player(self) -> Player:
        return self.players[self.index]

    @property
    def opponent(self) -> Player:
        return self.players[1-self.index]

    @property
    def duration(self):
        end = self.end_time if self.end_time is not None else time.time()
        return end - self.start_time

    def play(self):
        self.start_time = time.time()
        print("\nGame On!\n")
        self.board.print_board()

        while not self.is_finished:
            player = self.active_player
            print(f"\nIt is {player.name}({player.color}) to move.")

            player.start_turn()
            if self.ask_action() == "quit":
                self.finish(winner=self.opponent, loser=player, loser_result=Player.RESIGN)
                break

            checker, row, column, captured = self.ask_move()
            self.board.move(checker, row, column, captured)
            player.end_turn()
            self.total_moves += 1

            self.print_status(captured)
            self.is_game_over()
            self.index = 1 - self.index

        self.end_time = time.time()
        self.final_print()


    @staticmethod
    def ask_action():
        while True:
            choice = input("[m]ove or [e]nd").strip().lower()
            if choice in ["m", "move"]:
                return "move"
            if choice in ["e", "end"]:
                return "end"
            print("Please enter 'm' or 'e' stupid.")

    def ask_move(self):
        available_moves = self.board.get_all_moves(self.active_player.color)
        while True:
            text = input("Your move: ").strip().lower().split()
            if len(text) != 2:
                print("Need source AND target ya dingus.")
                continue
            start, end = self.get_square_from_input(text[0]), self.get_square_from_input(text[1])
            if start is None or end is None:
                print("Invalid move.")
                continue
            for checker, row, column, captured in available_moves:
                if checker.position == start and (row,column) == end:
                    return checker, row, column, captured

            print("DEBUG Farbe:", repr(self.active_player.color))
            print("DEBUG start/end:", start, end)
            print("DEBUG Züge:", available_moves)

            options = [self.square_name((r, c)) for ch, r, c, _ in available_moves
                       if ch.position == start]
            if options:
                print(f"Not Allowed. Valid targets are {', '.join(options)}")
            else:
                print("Not Allowed. There is no piece of yours here.")

    def get_square_from_input(self, text):
        if len(text) < 2 or not text[1:].isdigit():
            return None
        column = ord(text[0]) - ord('a')
        row = self.board.SIZE - int(text[1:])
        if not self.board.is_on_board(row, column):
            return None
        return row, column

    def print_status(self, captured):
        print()
        if captured is not None:
            print(f"Piece captured on {self.square_name(captured.position)}.")
        for p in self.players:
            print(f"{p.name} | pieces: {self.board.count(p.color)}")
        print()
        self.board.print_board()

    def square_name(self, position):
        row, column = position
        return f"{chr(ord('a') + column)}{8 - row}"

    def is_game_over(self):
        opponent = self.opponent
        if self.board.count(opponent.color) == 0:
            reason = "is all out of pieces"
        elif not self.board.get_all_moves(opponent.color):
            reason = "has no moves left"
        else:
            return
        print(f"\n{opponent.name} {reason}.")
        self.finish(winner=self.active_player, loser=opponent,loser_result=Player.LOSS)

    def finish(self, winner, loser, loser_result):
        self.winner = winner
        winner.set_result(Player.WIN)
        loser.set_result(loser_result)
        self.is_finished = True

    def final_print(self):
        print("\nGame is over: ")
        print(f"Winner: {self.winner.name if self.winner else '-'}")
        print(f"After {self.total_moves} moves played")
        print(f"Game lasted for {Player.format_time(self.duration)}")

if __name__ == "__main__":
    name1 = input("Player 1 (White): ")
    name2 = input("Player 2 (Black): ")
    game = Game(Player(name1,Checker.WHITE),Player(name2,Checker.BLACK))
    game.play()





