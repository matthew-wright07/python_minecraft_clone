import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Minecraft")

points = [(250,250),(350,250),(350,350),(250,350)]

def draw_polygon():
    screen.fill((0, 0, 0))  # Clear screen
    pygame.draw.polygon(screen, (255, 0, 0), points)
    pygame.display.update()

def scale_polygon(scale_factor):
    global points

    cx = sum(x for x, y in points) / len(points)
    cy = sum(y for x, y in points) / len(points)

    points = [((x - cx) * scale_factor + cx, (y - cy) * scale_factor + cy) for x, y in points]

draw_polygon()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                scale_polygon(0.9)
                draw_polygon()
            if event.key == pygame.K_UP:
                scale_polygon(1.1)
                draw_polygon()


pygame.quit()