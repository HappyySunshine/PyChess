from enum import Enum
class P(Enum):
    Empty = 0
    Pawn = 1
    King = 2
    Queen = 3
    Rook = 4
    Bishop = 5
    Horse = 6

class C(Enum):
    White = 0
    Black = 1
class MoveStatus(Enum):
    WhitePiece=0,
    BlackPiece=1,
    OutOfBounds=2,
    Empty = 3,


class Cell:
    piece = None
    def __init__(self, piece):
        self.piece = piece
       
    def place(self, piece):
        self.piece = piece
        
    def __str__(self):
        if self.piece:
            return str(self.piece)
        else:
            return "0"

class Piece:
        color= None
        p = None
        def __init__(self, p, color):
            self.color = color
            self.p = p
            
        def __str__(self):
            return str(self.p.value)


        def get_move_status(self, board, dir)-> MoveStatus:
            pass
        def is_blocked(self, board,dir )-> bool:
            pass

        def enemy_piece(self, board, dir)-> bool:
            pass

        def available_moves(self, pos, board):
            moves = []
            if self.p == P.Pawn:
                if self.color == C.White:
                    if self.get_move_status(board, [0,-1]) == MoveStatus.Empty :
                        moves.append([0,-1])
                    if self.get_move_status(board, [1, -1])== MoveStatus.BlackPiece:
                        moves.append([1, -1])
                    if self.get_move_status(board, [-1, -1])== MoveStatus.BlackPiece:
                        moves.append([1, -1])
                    if pos.y == 6:
                        if not self.get_move_status(board, [0,-2])== MoveStatus.Empty:
                            moves.append([0,-2])

                if pos.y==0:
                    return
                if board[pos.x][pos.y-1]
                moves.append()





class Color:
    White = 0
    Black = 1
    
tupla = ()

class Game:
    def __init__(self):
        self.board = [[Cell(None) for _ in range(8)] for _ in range(8)]
        self.board[0][0].place(Piece(P.Rook, C.White))
        for i in range(0,8):
            for j in range(0,8):
                p = self.board[i][j]
                if i==0 or i==7:
                    color = C.White if i==0 else C.Black
                    if j==0 or j==7:
                        p.place(Piece(P.Rook, color))
                    if j==1 or j==6:
                        p.place(Piece(P.Horse, color))
                    if j==2 or j==5:
                        p.place(Piece(P.Bishop, color))
                    if j ==3:
                        p.place(Piece(P.King, color))
                    if j ==4:
                        p.place(Piece(P.Queen, color))
                elif i==1:
                    p.place(Piece(P.Pawn, C.White))
                elif i ==6:
                    p.place(Piece(P.Pawn, C.Black))

 
    def debug(self):
        for i in self.board:
            for j in i:
                if (j):
                    print(j, end=" ")
                else:
                    print(0, end=" ")
            print("")