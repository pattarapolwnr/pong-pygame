import pygame


class Paddle:
    def __init__(self, screen, x, y, width, height, screen_width, screen_height, number):
        self.screen = screen

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.dy = 0

        self.number = number

        self.s_width = screen_width
        self.s_height = screen_height

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self, dt):
        if self.dy > 0:
            if self.rect.y + self.height < self.s_height:
                self.rect.y += self.dy*dt
        else:
            if self.rect.y >= 0:
                self.rect.y += self.dy*dt

    def render(self):
        if self.number == 1:
            pygame.draw.rect(self.screen, (51, 255, 255), self.rect)
        elif self.number == 2:
            pygame.draw.rect(self.screen, (255, 51, 51), self.rect)
