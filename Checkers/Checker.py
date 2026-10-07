

class Checker:
    WHITE = "white"
    BLACK = "black"

    def __init__(self,color,row,column):
        if color not in (Checker.WHITE,Checker.BLACK):
            raise ValueError("Invalid color!")
        self.color = color
        self.is_king = False
        self.row = row
        self.column = column

    @property
    def position(self):
        return self.row, self.column

    def get_directions(self):
        if self.is_king:
            return [(-1,-1), (-1,1), (1,-1), (1,1)]
        if self.color == Checker.WHITE:
            return [(-1,-1), (-1,1)]
        return [(1,1),(1,-1)]

    def move(self,row, column):
        self.row = row
        self.column = column

    def upgrade(self):
        self.is_king = True

    def is_enemy(self,other):
        return other is not None and self.color != other.color

    def symbol(self):
        if self.is_king:
            return self.color[0].upper()
        return self.color[0].upper()

    @staticmethod
    def _get_symbol(color):
        if color == "white":
            return "*"
        elif color == "black":
            return "o"
        return None