import pygame

BLACK = (0, 0, 0)


def drawTic(screen, start_pos1, end_pos1, start_pos2, end_pos2):
    pygame.draw.line(screen, BLACK, start_pos1, end_pos1, 5)
    pygame.draw.line(screen, BLACK, start_pos2, end_pos2, 5)
    return True


def drawToc(screen, pos, radios):
    pygame.draw.circle(screen, BLACK, pos, radios, 5)
    return True


def drawTicToc(cell, player=None, screen=None, start_pos1=None, end_pos1=None, start_pos2=None, end_pos2=None, pos=None,
               radios=None):
    if cell == 1:
        drawTic(screen, start_pos1, end_pos1, start_pos2, end_pos2)
    else:
        drawToc(screen, pos, radios)
        player += 1
    return player + 1
