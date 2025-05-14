import pygame

def drawGameOver(screen):
    font = pygame.font.SysFont(None, 80)
    text = font.render("GAME OVER", True, (255, 0, 0))
    rect = text.get_rect(center=(400, 200))
    screen.blit(text, rect)

    # リスタートボタン
    button_font = pygame.font.SysFont(None, 60)
    button_rect = pygame.Rect(300, 300, 200, 60)
    pygame.draw.rect(screen, (0, 255, 0), button_rect)  # 緑色のボタン
    button_text = button_font.render("RESTART", True, (0, 0, 0))
    text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, text_rect)

    return button_rect


def drawGameStart(screen):
    font = pygame.font.SysFont(None, 60)
    title_text = font.render("BLOCK BREAKING", True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(400, 200))
    screen.blit(title_text, title_rect)

    # スタートボタン
    button_rect = pygame.Rect(300, 300, 200, 60)
    pygame.draw.rect(screen, (0, 255, 0), button_rect)  # 緑色のボタン
    button_text = font.render("START", True, (0, 0, 0))
    text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, text_rect)

    return button_rect

def drawGameClear(screen):
    font = pygame.font.SysFont(None, 80)
    text = font.render("GAME CLEAR!", True, (0, 255, 0))
    rect = text.get_rect(center=(400, 200))
    screen.blit(text, rect)

    button_font = pygame.font.SysFont(None, 60)
    button_rect = pygame.Rect(300, 300, 200, 60)
    pygame.draw.rect(screen, (0, 255, 255), button_rect)  # 水色のボタン
    button_text = button_font.render("RESTART", True, (0, 0, 0))
    text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, text_rect)

    return button_rect