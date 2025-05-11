import pygame

def drawGameOver(screen):
    font = pygame.font.SysFont(None, 80)
    text = font.render("GAME OVER", True, (255, 0, 0))
    rect = text.get_rect(center=(400, 300))
    screen.blit(text, rect)

def drawGameStart(screen):
    font = pygame.font.SysFont(None, 60)
    title_text = font.render("BLOCK BREAKING", True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(400, 200))
    screen.blit(title_text, title_rect)

    # スタートボタン
    button_rect = pygame.Rect(300, 300, 200, 60)
    pygame.draw.rect(screen, (0, 255, 0), button_rect)
    button_text = font.render("START", True, (0, 0, 0))
    text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, text_rect)

    return button_rect