import json
import random
import bullet
import fon
import pygame
import rocket
import asteroid

pygame.init()

def start_game():
    def write_data():
        global settings
        with open("settings.json", "w", encoding="utf-8") as file:
            json.dump(settings, file)
    def read_data():
        global settings
        with open("settings.json", "r", encoding="utf-8") as file:
            settings = json.load(file)
    read_data()

    window = pygame.display.set_mode((800, 500))
    fps = pygame.time.Clock()

    r = rocket.Rocket(105, 300, 95, 190, 5, settings["skin"])
    patrons = []
    game = True

    asteroids = []
    asteroids.append(asteroid.Asteroid( random.randint(0, 800), random.randint(-1000, 0), 60, 60, 2, "asteroid.png"))
    asteroids.append(asteroid.Asteroid(random.randint(0, 800), random.randint(-1000, 0), 60, 60, 2, "asteroid.png"))
    asteroids.append(asteroid.Asteroid(random.randint(0, 800), random.randint(-1000, 0), 60, 60, 2, "asteroid.png"))
    asteroids.append(asteroid.Asteroid(random.randint(0, 800), random.randint(-1000, 0), 60, 60, 2, "asteroid.png"))
    asteroids.append(asteroid.Asteroid( random.randint(0, 800), random.randint(-1000, 0), 60, 60, 2, "asteroid.png"))
    asteroids.append(asteroid.Asteroid(random.randint(0, 800), random.randint(-1000, 0), 60, 60, 2, "asteroid.png"))
    asteroids.append(asteroid.Asteroid(random.randint(0, 800), random.randint(-1000, 0), 60, 60, 2, "asteroid.png"))
    asteroids.append(asteroid.Asteroid(random.randint(0, 800), random.randint(-1000, 0), 60, 60, 2, "asteroid.png"))

    while game:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                print(x, y)
            if event.type == pygame.QUIT:
                game = False
                pygame.quit()
                write_data()
                return








        window.fill((0, 0, 103))

        r.render(window)
        r.move()
        for patron in patrons:
            patron.move()


        for a in asteroids:
            a.move()
            if a.hit_box.y > 800:
                a.hit_box.y = random.randint(-100, 0)
                a.hit_box.x = random.randint(0, 800)

        for a in asteroids:
            a.render(window)

        for a in asteroids:
            for b in r.patrons:
                if a.hit_box.colliderect(b.hit_box):
                    r.patrons.remove(b)
                    a.hit_box.y = -500
                    settings["money"] += 1
                    break


        pygame.display.flip()
        fps.tick(60)