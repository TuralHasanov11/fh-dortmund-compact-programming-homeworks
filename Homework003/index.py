from classes import *


def main():
    board = ChessBoard

    player1_rook1 = Rook(x=0, y=0, color=Color.WHITE)
    player1_knight1 = Knight(x=0, y=1, color=Color.WHITE)
    player1_bishop1 = Bishop(x=0, y=2, color=Color.WHITE)
    player1_queen = Queen(x=0, y=3, color=Color.WHITE)
    player1_king = King(x=0, y=4, color=Color.WHITE)
    player1_bishop2 = Bishop(x=0, y=5, color=Color.WHITE)
    player1_knight2 = Knight(x=0, y=6, color=Color.WHITE)
    player1_rook2 = Rook(x=0, y=7, color=Color.WHITE)
    player1_pawn1 = Pawn(x=1, y=0, color=Color.WHITE)
    player1_pawn2 = Pawn(x=1, y=1, color=Color.WHITE)
    player1_pawn3 = Pawn(x=1, y=2, color=Color.WHITE)
    player1_pawn4 = Pawn(x=1, y=3, color=Color.WHITE)
    player1_pawn5 = Pawn(x=1, y=4, color=Color.WHITE)
    player1_pawn6 = Pawn(x=1, y=5, color=Color.WHITE)
    player1_pawn7 = Pawn(x=1, y=6, color=Color.WHITE)
    player1_pawn8 = Pawn(x=1, y=7, color=Color.WHITE)

    player2_rook1 = Rook(x=0, y=0, color=Color.BLACK)
    player2_knight1 = Knight(x=0, y=1, color=Color.BLACK)
    player2_bishop1 = Bishop(x=0, y=2, color=Color.BLACK)
    player2_queen = Queen(x=0, y=3, color=Color.BLACK)
    player2_king = King(x=0, y=4, color=Color.BLACK)
    player2_bishop2 = Bishop(x=0, y=5, color=Color.BLACK)
    player2_knight2 = Knight(x=0, y=6, color=Color.BLACK)
    player2_rook2 = Rook(x=0, y=7, color=Color.BLACK)
    player2_pawn1 = Pawn(x=1, y=0, color=Color.BLACK)
    player2_pawn2 = Pawn(x=1, y=1, color=Color.BLACK)
    player2_pawn3 = Pawn(x=1, y=2, color=Color.BLACK)
    player2_pawn4 = Pawn(x=1, y=3, color=Color.BLACK)
    player2_pawn5 = Pawn(x=1, y=4, color=Color.BLACK)
    player2_pawn6 = Pawn(x=1, y=5, color=Color.BLACK)
    player2_pawn7 = Pawn(x=1, y=6, color=Color.BLACK)
    player2_pawn8 = Pawn(x=1, y=7, color=Color.BLACK)


if __name__ == '__main__':
    main()
