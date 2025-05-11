import pygame
import sys
import random
from ui import drawGameOver

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Block Breaking Game")
clock = pygame.time.Clock()

# パドルの設定
paddle = pygame.Rect(400, 550, 100, 20)
PADDLE_COLOR = (0, 255, 255)
paddle_speed = 7

# ボールの設定
BALL_RADIUS = 15
ball = pygame.Rect(400, 400, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_speed_x = random.choice([-4, 4])
ball_speed_y = -5
BALL_COLOR = (255, 255, 255)

# ゲーム状態
is_game_over = False

# ゲームステージ処理
def gameStage():
    global ball_speed_x, ball_speed_y, is_game_over

    # 画面の初期化
    screen.fill(pygame.Color("BLACK"))

    if is_game_over:
        drawGameOver(screen)
        return

    # キー入力でパドルを移動
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < 800:
        paddle.x += paddle_speed

    # パドル描画
    pygame.draw.rect(screen, PADDLE_COLOR, paddle)

    # 壁反射処理
    if ball.left <= 0 or ball.right >= 800:
        ball_speed_x *= -1
    if ball.top <= 0:
        ball_speed_y *= -1

    # パドルとの衝突処理
    if paddle.colliderect(ball):
        ball_speed_y = -abs(ball_speed_y)
        ball_speed_x = (ball.centerx - paddle.centerx) / 5 

    # ボールの移動
    ball.x += int(ball_speed_x)
    ball.y += int(ball_speed_y)

    # 画面下に落ちたらゲームオーバー
    if ball.bottom > 600:
        is_game_over = True

    # ボールを描画
    pygame.draw.ellipse(screen, BALL_COLOR, ball)

# メインループ
while True:
    gameStage()
    pygame.display.update()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
