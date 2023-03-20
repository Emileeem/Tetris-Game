import pygame as pg

vec = pg.math.Vector2

FPS = 45 #fps ao decorrer do jogo
FIELD_COLOR = (255,182,193) #cor do fundo das grades
BG_COLOR = (176,224,230) # cor da tela do tetris ao lado

SPRITE_DIR_PATH = 'importante/sprites' #forma dos tetrominos
FONT_PATH = 'importante/fonte/EmilysCandy-Regular.ttf' #fonte 

ANIM_TIME_INTERVAL = 350  # millisegundos ao apertar os botoes direito e esquerdo
FAST_ANIM_TIME_INTERVAL = 15  #ao apertar para baixo

TILE_SIZE = 40 #tamanho da tela do jogo
FIELD_SIZE = FIELD_W, FIELD_H = 10, 20 #quanto por quanto
FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE #tamanho de tudo da tela 

FIELD_SCALE_W, FIELD_SCALE_H = 1.7, 1.0
WIN_RES = WIN_W, WIN_H = FIELD_RES[0] * FIELD_SCALE_W, FIELD_RES[1] * FIELD_SCALE_H

INIT_POS_OFFSET = vec(FIELD_W // 2 - 1, 0)
NEXT_POS_OFFSET = vec(FIELD_W * 1.3, FIELD_H * 0.45)
MOVE_DIRECTIONS = {'left': vec(-1, 0), 'right': vec(1, 0), 'down': vec(0, 1)}

#formatos dos tetrominós
TETROMINOES = {
    'T': [(0, 0), (-1, 0), (1, 0), (0, -1)],
    'O': [(0, 0), (0, -1), (1, 0), (1, -1)],
    'J': [(0, 0), (-1, 0), (0, -1), (0, -2)],
    'L': [(0, 0), (1, 0), (0, -1), (0, -2)],
    'I': [(0, 0), (0, 1), (0, -1), (0, -2)],
    'S': [(0, 0), (-1, 0), (0, -1), (1, -1)],
    'Z': [(0, 0), (1, 0), (0, -1), (-1, -1)]
}
