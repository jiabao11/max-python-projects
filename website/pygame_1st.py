import pygame
import random
pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Max's First Pygame!")
clock = pygame.time.Clock()

# player position and colour
x, y = 300, 200
color = (100, 180, 255)
speed = 5
score = 0

# coin position
coin_x = random.randint(30, 570)
coin_y = random.randint(30, 370)

font = pygame.font.SysFont('Arial', 24)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # arrow keys move the circle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]  and x > 30:
        x -= speed
    if keys[pygame.K_RIGHT] and x < 570:
        x += speed
    if keys[pygame.K_UP]    and y > 30:
        y -= speed
    if keys[pygame.K_DOWN]  and y < 370:
        y += speed

    # collect the coin
    dist = ((x - coin_x)**2 + (y - coin_y)**2) ** 0.5
    if dist < 40:
        score += 1
        coin_x = random.randint(30, 570)
        coin_y = random.randint(30, 370)
        color = (random.randint(100,255), random.randint(100,255), random.randint(100,255))

    # draw everything
    screen.fill((30, 30, 60))
    pygame.draw.circle(screen, (255, 220, 50), (coin_x, coin_y), 12)   # yellow coin
    pygame.draw.circle(screen, color,          (x, y),           30)   # player

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    hint = font.render("Arrow keys to move · collect coins!", True, (100, 100, 150))
    screen.blit(hint, (80, 370))

    pygame.display.flip()
    clock.tick(60)   # 60 frames per second

pygame.quit()
