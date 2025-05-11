import pygame
import sys

# 初期化
pygame.init()

# 画面サイズ
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Block Breaking Game")

# FPS制御用クロック
clock = pygame.time.Clock()

# パドルの設定
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 15
PADDLE_COLOR = (0, 255, 255)
paddle_speed = 7
paddle = pygame.Rect((WIDTH - PADDLE_WIDTH) // 2, HEIGHT - 40, PADDLE_WIDTH, PADDLE_HEIGHT)

# メインループ
while True:
    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # キー入力取得
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.x += paddle_speed

    # 描画
    screen.fill((0, 0, 0))  # 背景を黒に
    pygame.draw.rect(screen, PADDLE_COLOR, paddle)  # パドル描画

    # 画面更新
    pygame.display.flip()

    # FPS制御
    clock.tick(60)


