import time

from Checkers.Checker import Checker

class Player:
    WIN = "won"
    LOSS = "lost"
    RESIGN = "resigned"
    DRAW = "tied"

    def __init__(self,name,color):
        def __init__(self, name, color):
            if color not in (Checker.WHITE, Checker.BLACK):
                raise ValueError(f"Invalid Color: {color}")
        self.move_count = 0
        self.name = name
        self.color = color
        self.result = None
        self.time_played = 0.0
        self._turn_start = None

    def start_turn(self):
        self._turn_start = time.time()

    def end_turn(self):
        if self._turn_start is None:
            raise RuntimeError("must call start_turn() before end_turn()")
        self.time_played = self.time_played + time.time() - self._turn_start
        self.move_count += 1
        self._turn_start = None

    def set_result(self, result):
        if result not in (Player.WIN, Player.LOSS, Player.RESIGN, Player.DRAW):
            raise ValueError("Invalid outcome")
        self.result = result

    @staticmethod
    def format_time(seconds):
        minutes, seconds = divmod(int(seconds), 60)
        return f"{minutes:02d}:{seconds:02d}"

    def to_string(self):
        return (f"{self.name} ({self.color})\n"
                f"  Result: {self.result}\n"
                f"  Time: {self.format_time(self.time_played)}\n")

