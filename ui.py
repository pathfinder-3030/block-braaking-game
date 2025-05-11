import pygame

def drawGameOver(screen):
    font = pygame.font.SysFont(None, 80)
    text = font.render("GAME OVER", True, (255, 0, 0))
    rect = text.get_rect(center=(400, 300))
    screen.blit(text, rect)
