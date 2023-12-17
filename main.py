import fon
import pygame
import rocket

pygame.init()


window = pygame.display.set_mode((800, 500))
fps = pygame.time.Clock()

rocket = rocket.Rocket(105, 200, 70, 150, 5, "rocket.png")

game = True


while game:
    for event in pygame.event.get:
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print(x, y)
        if event



    window.fill((123, 123, 123))




    window.fill((123, 123, 123))

    rocket.render(window)
    rocket.move()
    for asteroid in asteroids:
        asteroid.render(window)

    pygame.display.flip()
    fps.tick(60)