from enum import Enum


class Color(Enum):
    WHITE: int = 1
    BLACK: int = 0


class Position:
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y


class ChessBoard:
    boxes: list[list] = [[]]

    def __init__(self) -> None:
        self.reset()

    def getBox(self, x, y):
        if x < 0 or x > 7 or y < 0 or y > 7:
            raise Exception("Out of board")
        return self.boxes[x][y]

    def reset(self):
        w, h = 8, 8
        self.boxes = [[None for x in range(w)] for y in range(h)]


class ChessFigure():
    color: str
    title: str
    position: Position
    killed: bool

    def __init__(self, x: int, y: int, color: int) -> None:
        self.position.x = x
        self.position.y = y
        self.color = color
        self.killed = False

    @property
    def is_white(self):
        if self.color == 1:
            return True
        else:
            return False

    def move(self, end_x, end_y):

        if self.canMove():
            self.position.x = end_x
            self.position.y = end_y


class Rook(ChessFigure):
    def move():
        pass

    def beat():
        pass


class Knight(ChessFigure):
    def move():
        pass

    def beat():
        pass


class Bishop(ChessFigure):
    def move():
        pass

    def beat():
        pass


class Queen(ChessFigure):
    def move():
        pass

    def beat():
        pass


class King(ChessFigure):

    castling_done: bool = False

    def move():
        pass

    def beat():
        pass


class Pawn(ChessFigure):
    def move():
        pass

    def beat():
        pass
