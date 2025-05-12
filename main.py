import pygame
from ui import Ui
from game import Game
# Initialize pygame
pygame.init()

# Set up the display window
game = Game()
ui = Ui(game)


# Main game loop
running = True
print(game.debug())
ui.screen.fill((135, 206, 235)) 
ui.draw_bg()
ui.draw_board(game)
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            ui.click(x,y)
    
    # Fill the screen with a color (RGB)
     # Light blue
    
    # Update the display
    

# Quit pygame when the loop ends
pygame.quit()