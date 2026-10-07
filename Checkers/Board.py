from Checkers.Checker import Checker


class Board:
    SIZE = 8



    def __init__(self):
        self.grid = [[None] * self.SIZE for _ in range(self.SIZE)]
        self._setup_grid()

    def _setup_grid(self):
        for row in range(self.SIZE):
            for column in range(self.SIZE):
                if self.is_dark(row,column):
                    if row < 3:
                        self.grid[row][column] = Checker("black", row, column)
                    elif row > 4:
                        self.grid[row][column] = Checker("white", row, column)



    def is_on_board(self,row,column):
        return 0 <= row < self.SIZE and 0 <= column < self.SIZE

    def get(self,row,column):
        return self.grid[row][column]

    @staticmethod
    def is_dark(row, column):
        return (row+column) % 2 == 1

    def print_board(self):
        letters = "abcdefgh"
        print("   " + " ".join(letters))
        for row in range(self.SIZE):
            cells = []
            for column in range(self.SIZE):
                piece = self.grid[row][column]
                if piece is not None:
                    cells.append(piece.symbol())
                else:
                    cells.append("." if self.is_dark(row,column) else " ")
            print(f"{self.SIZE -row:2} " + " ".join(cells))

    def get_moves(self, checker):
        moves = []
        for dr, dc in checker.get_directions():
            r, c = checker.row + dr, checker.column + dc
            if not self.is_on_board(r,c):
                continue
            target = self.grid[r][c]
            if target is None:
                moves.append((r,c,None))
            elif checker.is_enemy(target):
                jr,jc = r + dr, c + dc
                if self.is_on_board(jr,jc) and self.grid[jr][jc] is None:
                    moves.append((jr,jc,target))

        return moves

    def count(self, color):
        return sum(1 for row in self.grid for p in row if p and p.color == color)

    def move(self, checker, to_row, to_column, captured=None):
        self.grid[checker.row][checker.column] = None
        checker.move(to_row, to_column)
        self.grid[to_row][to_column] = checker
        if captured:
            self.grid[captured.row][captured.column] = None
        last_row = 0 if checker.color ==  Checker.WHITE else 7
        if to_row == last_row:
            checker.promote()


    def get_all_moves(self,color):
        moves = []
        for row in self.grid:
            for piece in row:
                if piece is not None and piece.color == color:
                    for r,c, captured in self.get_moves(piece):
                        moves.append((piece, r,c,captured))
        return moves
