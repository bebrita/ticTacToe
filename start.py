import pygame
import random
from pygame.color import THECOLORS

from Tic import drawTicToc

def button(screen):
    button_color = (0, 255, 0)
    button_text_color = (255, 255, 255)
    button_font = pygame.font.Font(None, 24)
    button_surface = pygame.Surface((180,50))
    button_surface.fill(button_color)
    button_text_surface = button_font.render( "Сыграть еще раз", True, button_text_color)
    screen.blit(button_surface, (90,400))
    screen.blit(button_text_surface, (110, 410))


def draw_screen():
    screen.fill(WHITE)
    r = pygame.Rect(90, 180, 180, 180)
    pygame.draw.rect(screen, BLACK, r, 5)
    pygame.draw.line(screen, BLACK, (90, 240), (270, 240), 5)
    pygame.draw.line(screen, BLACK, (90, 300), (270, 300), 5)
    pygame.draw.line(screen, BLACK, (150, 180), (150, 360), 5)
    pygame.draw.line(screen, BLACK, (210, 180), (210, 360), 5)
    font1 = pygame.font.SysFont('couriernew', 30)
    text1 = font1.render(str('Крестики-нолики'), True, THECOLORS['red'])
    screen.blit(text1, (40, 50))


WIDTH = 360
HEIGHT = 480
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

player = 1
game = True

cell1 = 0
cell2 = 0
cell3 = 0
cell4 = 0
cell5 = 0
cell6 = 0
cell7 = 0
cell8 = 0
cell9 = 0

click_cell1 = pygame.Rect(90, 180, 60, 60)
click_cell2 = pygame.Rect(150, 180, 60, 60)
click_cell3 = pygame.Rect(210, 180, 60, 60)
click_cell4 = pygame.Rect(90, 240, 60, 60)
click_cell5 = pygame.Rect(150, 240, 60, 60)
click_cell6 = pygame.Rect(210, 240, 60, 60)
click_cell7 = pygame.Rect(90, 300, 60, 60)
click_cell8 = pygame.Rect(150, 300, 60, 60)
click_cell9 = pygame.Rect(210, 300, 60, 60)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
running = True
draw_screen()
pygame.display.flip()

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
                if click_cell1.collidepoint(event.pos) and cell1 == 0 and game:
                    cell1 = player % 3
                    player = drawTicToc(cell1, player, screen, (90, 180), (150, 240), (90, 240), (150, 180), (120, 210),
                                        30)
                if click_cell2.collidepoint(event.pos) and cell2 == 0 and game:
                    cell2 = player % 3
                    player = drawTicToc(cell2, player, screen, (150, 180), (210, 240), (150, 240), (210, 180),
                                        (180, 210), 30)
                if click_cell3.collidepoint(event.pos) and cell3 == 0 and game:
                    cell3 = player % 3
                    player = drawTicToc(cell3, player, screen, (210, 180), (270, 240), (210, 240), (270, 180),
                                        (240, 210), 30)
                if click_cell4.collidepoint(event.pos) and cell4 == 0 and game:
                    cell4 = player % 3
                    player = drawTicToc(cell4, player, screen, (90, 240), (150, 300), (90, 300), (150, 240), (120, 270),
                                        30)
                if click_cell5.collidepoint(event.pos) and cell5 == 0 and game:
                    cell5 = player % 3
                    player = drawTicToc(cell5, player, screen, (150, 240), (210, 300), (150, 300), (210, 240),
                                        (180, 270), 30)
                if click_cell6.collidepoint(event.pos) and cell6 == 0 and game:
                    cell6 = player % 3
                    player = drawTicToc(cell6, player, screen, (210, 240), (270, 300), (210, 300), (270, 240),
                                        (240, 270), 30)
                if click_cell7.collidepoint(event.pos) and cell7 == 0 and game:
                    cell7 = player % 3
                    player = drawTicToc(cell7, player, screen, (90, 300), (150, 360), (90, 360), (150, 300), (120, 330),
                                        30)
                if click_cell8.collidepoint(event.pos) and cell8 == 0 and game:
                    cell8 = player % 3
                    player = drawTicToc(cell8, player, screen, (150, 300), (210, 360), (150, 360), (210, 300),
                                        (180, 330), 30)
                if click_cell9.collidepoint(event.pos) and cell9 == 0 and game:
                    cell9 = player % 3
                    player = drawTicToc(cell9, player, screen, (210, 300), (270, 360), (210, 360), (270, 300),
                                        (240, 330), 30)
                if cell1 == cell2 == cell3 == 1 or cell4 == cell5 == cell6 == 1 or cell7 == cell8 == cell9 == 1 or cell1 == cell4 == cell7 == 1 or cell2 == cell5 == cell8 == 1 or cell3 == cell6 == cell9 == 1 or cell1 == cell5 == cell9 == 1 or cell3 == cell5 == cell7 == 1:
                    font2 = pygame.font.SysFont('couriernew', 30)
                    text2 = font2.render(str('Крестики выиграли!'), True, THECOLORS['red'])
                    screen.blit(text2, (30, 100))
                    game = False
                elif cell1 == cell2 == cell3 == 2 or cell4 == cell5 == cell6 == 2 or cell7 == cell8 == cell9 == 2 or cell1 == cell4 == cell7 == 2 or cell2 == cell5 == cell8 == 2 or cell3 == cell6 == cell9 == 2 or cell1 == cell5 == cell9 == 2 or cell3 == cell5 == cell7 == 2:
                    font2 = pygame.font.SysFont('couriernew', 30)
                    text2 = font2.render(str('Нолики выиграли!'), True, THECOLORS['red'])
                    screen.blit(text2, (40, 100))
                    game = False
                elif cell1!=0 and cell2!=0 and cell3!=0 and cell4!=0 and cell5!=0 and cell6!=0 and cell7!=0 and cell8!=0 and cell9!=0:
                    font2 = pygame.font.SysFont('couriernew', 30)
                    text2 = font2.render(str('Ничья!'), True, THECOLORS['red'])
                    screen.blit(text2, (60, 100))
                    game = False
                if game == False:
                    button(screen)
                    click_button = pygame.Rect(90, 400, 180, 50)
                    if click_button.collidepoint(event.pos):
                        game = True
                        draw_screen()
                        cell1 = cell2 = cell3 = cell4 = cell5 = cell6 = cell7 = cell8 = cell9 = 0
                        player = 1
    pygame.display.flip()
pygame.quit()
