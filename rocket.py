import pygame

import bullet


class Rocket:

    def __init__(self, x, y, w, h, speed, texture):
        self.speed = speed
        self.texture = pygame.image.load(texture)
        self.hit_box = self.texture.get_rect()
        self.hit_box.x = x
        self.hit_box.y = y
        self.texture = pygame.transform.scale(self.texture, (w, h))
        self.patrons = []
    def render(self, window):
        window.blit(self.texture, (self.hit_box.x, self.hit_box.y))

        for patron in self.patrons:
            patron.render(window)


    def move(self):


        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.hit_box.x += self.speed
        if keys[pygame.K_s]:
            self.hit_box.x -= self.speed
        if keys[pygame.K_e]:
            self.patrons.append(bullet.Bullet(self.hit_box.x, self.hit_box.y, 20, 40, 5, "bullet.png"))
        for patron in self.patrons:
            patron.move()