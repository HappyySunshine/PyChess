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
    AllyPiece=0,
    EnemyPiece=1,
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

class Vec2:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Adds two Vec2 objects component-wise"""
        if isinstance(other, Vec2):
            return Vec2(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Operands must be of type Vec2")

    def __repr__(self):
        """String representation of the vector"""
        return f"Vec2({self.x}, {self.y})"

    def __eq__(self, other):
        """Enable == operator to compare two Vec2 objects"""
        if isinstance(other, Vec2):
            return self.x == other.x and self.y == other.y
        return False
class Piece:
        color= None
        p = None
        def __init__(self, p, color):
            self.color = color
            self.p = p
            
        def __str__(self):
            return str(self.p.value)


        def get_move_status(self, pos: Vec2, board, dir: Vec2)-> MoveStatus:
            new_pos =pos + dir
            if new_pos.x < 0  or new_pos.x >7 or new_pos.y < 0 or new_pos.y >7:
                return MoveStatus.OutOfBounds
            cell = board[new_pos.y][new_pos.x]
            if cell.piece is None:
                return MoveStatus.Empty
            if cell.piece.color != self.color:
                return  MoveStatus.EnemyPiece
            return MoveStatus.AllyPiece
        def is_blocked(self, board,dir )-> bool:
            pass

        def enemy_piece(self, board, dir)-> bool:
            pass

        def available_moves(self, pos: Vec2, board)-> list[Vec2]:
            moves = []
            if self.p == P.Pawn:
                vert = 1
                if self.color == C.White:
                    vert = -1
                if self.get_move_status(pos, board, Vec2(0,vert)) == MoveStatus.Empty :
                    moves.append(Vec2(0,vert))
                    if self.color == C.White and pos.y == 6:
                        if self.get_move_status(pos, board,Vec2(0, -2)) == MoveStatus.Empty:
                            moves.append(Vec2(0,-2))
                    elif self.color == C.Black and pos.y == 1:
                        if self.get_move_status(pos, board, Vec2(0, 2)) == MoveStatus.Empty:
                            moves.append(Vec2(0, 2))
                if self.get_move_status(pos, board, Vec2(1, vert))== MoveStatus.EnemyPiece:
                    moves.append(Vec2(1, vert))
                if self.get_move_status(pos, board, Vec2(-1, vert))== MoveStatus.EnemyPiece:
                    moves.append(Vec2(-1, vert))
            return  moves





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
                    color = C.Black if i==0 else C.White
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
                    p.place(Piece(P.Pawn, C.Black))
                elif i ==6:
                    p.place(Piece(P.Pawn, C.White))

    def place(self, old_pos, new_pos:Vec2):
        cell = self.board[old_pos.x][old_pos.y]

        new_cell = new_pos[old_pos.x][old_pos.y]
        new_cell.piece = cell.piece
        cell.piece = None
        pass

    def move(self, pos: Vec2, dir: Vec2):
        pass
    def debug(self):
        for i in self.board:
            for j in i:
                if (j):
                    print(j, end=" ")
                else:
                    print(0, end=" ")
            print("")