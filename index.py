import pygame
import sys
import random
from ui import drawGameOver, drawGameStart, drawGameClear

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("ブロック崩し")
clock = pygame.time.Clock()

# BGMの読み込みと再生
pygame.mixer.music.load("sounds/bgm.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)  

# 効果音の読み込み
hit_sound = pygame.mixer.Sound("sounds/pi.wav")
hit_sound.set_volume(0.3)

pikopiko_sound = pygame.mixer.Sound("sounds/pikopiko.wav")
pikopiko_sound.set_volume(0.4)

up_sound = pygame.mixer.Sound("sounds/up.wav")
up_sound.set_volume(0.4)

# パドルの設定
paddle = pygame.Rect(400, 550, 100, 20)
PADDLE_COLOR = (0, 255, 255)
paddle_speed = 7

# ボールの設定
BALL_RADIUS = 16 
ball = pygame.Rect(400, 400, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_speed_x = random.choice([-4, 4])
ball_speed_y = -5
BALL_COLOR = (255, 255, 255)

# ブロックの設定
BLOCK_ROWS = 5
BLOCK_COLUMNS = 10
BLOCK_WIDTH = 60
BLOCK_HEIGHT = 20
BLOCK_MARGIN = 10
BLOCK_COLOR = (255, 165, 0)
blocks = []

# ゲーム状態
page = 1
is_game_over = False
has_played_clear_sound = False

# ゲーム初期化処理
def resetGame():
    global paddle, ball, ball_speed_x, ball_speed_y, is_game_over, page, blocks, has_played_clear_sound
    paddle.x = 400
    ball.x = 400
    ball.y = 400
    ball_speed_x = random.choice([-4, 4])
    ball_speed_y = -5
    is_game_over = False
    page = 2
    has_played_clear_sound = False

    blocks = []
    for row in range(BLOCK_ROWS):
        for col in range(BLOCK_COLUMNS):
            x = col * (BLOCK_WIDTH + BLOCK_MARGIN) + 50
            y = row * (BLOCK_HEIGHT + BLOCK_MARGIN) + 50
            blocks.append(pygame.Rect(x, y, BLOCK_WIDTH, BLOCK_HEIGHT))

# ゲーム中の処理
def gameStage():
    global ball_speed_x, ball_speed_y, is_game_over, page

    screen.fill(pygame.Color("BLACK"))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < 800:
        paddle.x += paddle_speed

    pygame.draw.rect(screen, PADDLE_COLOR, paddle)

    for block in blocks[:]:
        pygame.draw.rect(screen, BLOCK_COLOR, block)
        if ball.colliderect(block):
            blocks.remove(block)
            ball_speed_y *= -1
            hit_sound.play()
            break

    if not blocks:
        page = 4
        return

    if ball.left <= 0 or ball.right >= 800:
        ball_speed_x *= -1
    if ball.top <= 0:
        ball_speed_y *= -1

    if paddle.colliderect(ball):
        ball_speed_y = -abs(ball_speed_y)
        ball_speed_x = (ball.centerx - paddle.centerx) / 5
        hit_sound.play()

    ball.x += int(ball_speed_x)
    ball.y += int(ball_speed_y)

    if ball.bottom > 600:
        is_game_over = True
        page = 3
        pikopiko_sound.play()

    pygame.draw.ellipse(screen, BALL_COLOR, ball)

# メインループ
start_button_rect = None
restart_button_rect = None
clear_button_rect = None

while True:
    if page == 1:
        screen.fill(pygame.Color("BLACK"))
        start_button_rect = drawGameStart(screen)
    elif page == 2:
        gameStage()
    elif page == 3:
        screen.fill(pygame.Color("BLACK"))
        restart_button_rect = drawGameOver(screen)
    elif page == 4:
        screen.fill(pygame.Color("BLACK"))
        clear_button_rect = drawGameClear(screen)
        if not has_played_clear_sound:
            up_sound.play()
            has_played_clear_sound = True

    pygame.display.update()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if page in [1, 3, 4]:
                resetGame()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if page == 1 and start_button_rect and start_button_rect.collidepoint(event.pos):
                resetGame()
            if page == 3 and restart_button_rect and restart_button_rect.collidepoint(event.pos):
                resetGame()
            if page == 4 and clear_button_rect and clear_button_rect.collidepoint(event.pos):
                resetGame()
