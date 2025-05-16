
import pygame
from PIL import Image, ImageEnhance
from pygame import Rect
from game import C, P, Piece, Vec2


class PieceUi:
    image_src = None
    pygame_img = None
    color = None
    piece = None


    def __init__(self, image_src, piece):
        self.pygame_image = None
        self.image_src = image_src
        self.piece = piece
        # Create Pygame surface
       # self.pygame_image = pygame.image.fromstring(data, size, mode)

    def resize(self, ui):
        width = ui.board.width / 8 - ui.padding * 2
        height = ui.board.height / 8 - ui.padding * 2
        pil_image = Image.open(self.image_src).convert("RGBA")
        pil_image = pil_image.resize((int(width), int(height)))
       # enhancer = ImageEnhance.Brightness(pil_image)
       # pil_image = enhancer.enhance(0.6)
        mode = pil_image.mode
        size = pil_image.size
        data = pil_image.tobytes()
        self.pygame_img = pygame.image.fromstring(data, size, mode)



class CellUi:
    rect = None
    color = None

    def __init__(self,rect, color):
        self.rect = rect
        self.color = color

    def draw(self, screen, highlight = False):
        if highlight:
            r, g, b = self.color
            light_factor = 0.3
            lighter_color = (
                min(255, int(r + (255 - r) * light_factor)),
                min(255, int(g + (255 - g) * light_factor)),
                min(255, int(b + (255 - b) * light_factor))
            )
            # Draw the lighter rectangle
            pygame.draw.rect(screen, lighter_color, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)

        border = [0.0, 0.0, 0.0]
        a = 0
        for c in self.color:
            b = round(float(c) * 0.5)
            border[a] = b
            a += 1
        pygame.draw.rect(screen, border, self.rect, 2) # draw border

ASSETS = "assets/"
class Ui:
    pieces = [
        PieceUi(ASSETS + "pawn.png", P.Pawn),
        PieceUi(ASSETS + "queen.jpg", P.Queen),
        PieceUi(ASSETS + "king.jpg", P.King),
        PieceUi(ASSETS + "tower.jpg", P.Rook),
        PieceUi(ASSETS+ "bishop.jpg", P.Bishop ),
        PieceUi(ASSETS + "horse.png", P.Horse),

    ]
    def __init__(self, game):
        self.padding = 2
        self.color1=  (54, 188, 226)
        self.color2= (130,248,36)
        self.border_size = 2
        self.screen_width = 800
        self.screen_height = 600
        self.board = Rect(100,100,400,400)
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.cells = []
        self.game = game
        self.selected= None
        self.highlights: list[Vec2] = None
        for piece in self.pieces:
            piece.resize(self)

       # self.pygame_image = pygame.transform.scale(self.pygame_image, (32, 32))

    def draw_bg(self):
        width =  self.board.width /8 
        height = self.board.height /8
        x,y = (self.board.x,self.board.y)
        color1 = True
        for i in range(8):
            self.cells.append([])
            for j in range(8):
                rect = Rect(x,y,width,height)

                color = self.color1 if color1 else self.color2
                color1= not color1
                cell = CellUi(rect, color)
                cell.draw(self.screen)
                self.cells[i].append(cell)
                x+= width
            x=self.board.x
            y+= height
            color1 = not color1

        pygame.display.flip()

    def draw_board(self, game: Piece):
        width = self.board.width / 8
        height = self.board.height / 8
        x, y = (self.board.x, self.board.y)
        for row in game.board:
            for cell in row:
                if cell.piece== None:
                    x+= width
                    continue
                piece = self.pieces[cell.piece.p.value-1]
                if piece.pygame_img:
                    self.screen.blit(piece.pygame_img, (self.padding +x , self.padding + y) )
                x+= width
            y+=height
            x = self.board.x
        pygame.display.flip()

    def get_chess_pos(self, x,y):
        for i, row in enumerate(self.cells):
            for j, cell in enumerate(row):
                if cell.rect.collidepoint(x, y):
                    return Vec2(j,i)
        pass
    def remove_highlights(self):
        for vec in self.highlights:
            cell: CellUi = self.cells[vec.y][vec.x]
            cell.draw(self.screen)
        self.highlights = None



    def click(self,x,y):
        if self.selected is not None:
            vec = self.get_chess_pos(x,y)
            for pos in self.selected:
                if pos == vec:
                    old = self.selected
                    piece = self.game.board[old.y][old.x]
                    self.board.move(old, pos)
                    cell = self.cells[old.y][old.x]
                    cell.draw(self.screen)
                    cell = self.cells[pos.y][pos.x]
                    cell.draw(self.screen)
                    cell.draw_piece(piece)


        for i, row in enumerate(self.cells):
            for j,cell in enumerate(row):
                if cell.rect.collidepoint(x,y):
                    cell = self.game.board[i][j]
                    if self.highlights is not None:
                        self.remove_highlights()

                    if cell.piece is None:
                        return

                    piece = cell.piece
                    current_pos = Vec2(j,i)
                    moves = piece.available_moves(current_pos, self.game.board)
                    self.highlights = []
                    for move in moves:
                        pos = move + current_pos
                        self.highlights.append(pos)
                        cellui: CellUi = self.cells[pos.y][pos.x]
                        cellui.draw(self.screen, True)
                    pygame.display.flip()


                
                
        
    