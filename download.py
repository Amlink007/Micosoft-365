import pygame
import sys
import os

# Initialisation
pygame.init()
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu de Tank à 2 Joueurs")

# Couleurs
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE = (0, 0, 200)
BLACK = (0, 0, 0)

# Tanks
TANK_SIZE = (40, 40)
TANK_SPEED = 5
BULLET_SPEED = 8
BULLET_SIZE = (8, 8)

# Score
font = pygame.font.SysFont(None, 48)

def draw_window(tank1, tank2, bullets1, bullets2, score1, score2):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, RED, tank1)
    pygame.draw.rect(WIN, BLUE, tank2)
    for b in bullets1:
        pygame.draw.rect(WIN, RED, b)
    for b in bullets2:
        pygame.draw.rect(WIN, BLUE, b)
    score_text = font.render(f"Rouge: {score1}   Bleu: {score2}", True, BLACK)
    WIN.blit(score_text, (WIDTH//2 - score_text.get_width()//2, 10))
    pygame.display.update()

def main():
    tank1 = pygame.Rect(100, HEIGHT//2, *TANK_SIZE)
    tank2 = pygame.Rect(WIDTH-140, HEIGHT//2, *TANK_SIZE)
    bullets1 = []
    bullets2 = []
    score1 = 0
    score2 = 0
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Contrôles tank1 (ZQSD + espace)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_z] and tank1.top > 0:
            tank1.y -= TANK_SPEED
        if keys[pygame.K_s] and tank1.bottom < HEIGHT:
            tank1.y += TANK_SPEED
        if keys[pygame.K_q] and tank1.left > 0:
            tank1.x -= TANK_SPEED
        if keys[pygame.K_d] and tank1.right < WIDTH:
            tank1.x += TANK_SPEED
        if keys[pygame.K_SPACE] and len(bullets1) < 3:
            bullets1.append(pygame.Rect(tank1.right, tank1.centery-4, *BULLET_SIZE))

        # Contrôles tank2 (flèches + entrée)
        if keys[pygame.K_UP] and tank2.top > 0:
            tank2.y -= TANK_SPEED
        if keys[pygame.K_DOWN] and tank2.bottom < HEIGHT:
            tank2.y += TANK_SPEED
        if keys[pygame.K_LEFT] and tank2.left > 0:
            tank2.x -= TANK_SPEED
        if keys[pygame.K_RIGHT] and tank2.right < WIDTH:
            tank2.x += TANK_SPEED
        if keys[pygame.K_RETURN] and len(bullets2) < 3:
            bullets2.append(pygame.Rect(tank2.left-8, tank2.centery-4, *BULLET_SIZE))

        # Déplacement des balles
        for b in bullets1[:]:
            b.x += BULLET_SPEED
            if b.colliderect(tank2):
                score1 += 1
                bullets1.remove(b)
            elif b.x > WIDTH:
                bullets1.remove(b)
        for b in bullets2[:]:
            b.x -= BULLET_SPEED
            if b.colliderect(tank1):
                score2 += 1
                bullets2.remove(b)
            elif b.x < 0:
                bullets2.remove(b)

        draw_window(tank1, tank2, bullets1, bullets2, score1, score2)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()