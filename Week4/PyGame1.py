import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Simple Game")
clock = pygame.time.Clock()

x, y = 320, 240
speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    screen.fill((255, 255, 255))  # Fill screen with white
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))  # Draw red square
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
