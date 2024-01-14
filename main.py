import random
import bullet
import fon
import pygame
import rocket
import asteroid

pygame.init()


window = pygame.display.set_mode((800, 500))
fps = pygame.time.Clock()

rocket = rocket.Rocket(105, 300, 95, 190, 5, "rocket.png")

game = True

asteroids = []
asteroids.append(asteroid.Asteroid( random.randint(0, 800), random.randint(-1000, 0), 60, 60, 5, "asteroid.png"))
asteroids.append(asteroid.Asteroid(random.randint(0, 800), random.randint(-1000, 0), 60, 60, 5, "asteroid.png"))
asteroids.append(asteroid.Asteroid(random.randint(0, 800), random.randint(-1000, 0), 60, 60, 5, "asteroid.png"))
asteroids.append(asteroid.Asteroid(random.randint(0, 800), random.randint(-1000, 0), 60, 60, 5, "asteroid.png"))
asteroids.append(asteroid.Asteroid( random.randint(0, 800), random.randint(-1000, 0), 60, 60, 5, "asteroid.png"))
asteroids.append(asteroid.Asteroid(random.randint(0, 800), random.randint(-1000, 0), 60, 60, 5, "asteroid.png"))
asteroids.append(asteroid.Asteroid(random.randint(0, 800), random.randint(-1000, 0), 60, 60, 5, "asteroid.png"))
asteroids.append(asteroid.Asteroid(random.randint(0, 800), random.randint(-1000, 0), 60, 60, 5, "asteroid.png"))

while game:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print(x, y)
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()








    window.fill((0, 0, 103))

    rocket.render(window)
    rocket.move()

    for asteroid in asteroids:
        asteroid.move()
        if asteroid.hit_box.y > 800:
            asteroid.hit_box.y = random.randint(-100, 0)
            asteroid.hit_box.x = random.randint(0, 800)
    for asteroid in asteroids:
        asteroid.render(window)


    pygame.display.flip()
    fps.tick(60)