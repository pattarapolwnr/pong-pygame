import pygame


class Ball:
    def __init__(self, screen, x, y, width, height, screen_width, screen_height):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.s_width = screen_width
        self.s_height = screen_height

        self.dx = 0
        self.dy = 0

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def Collides(self, paddle):
        # first, check to see if the left edge of either is farther to the right
        # than the right edge of the other
        if self.rect.x > paddle.rect.x + paddle.width or paddle.rect.x > self.rect.x + self.width:
            return False
    # then check to see if the bottom edge of either is higher than the top
    # edge of the other
        if self.rect.y > paddle.rect.y + paddle.height or paddle.rect.y > self.rect.y + self.height:
            return False
        return True

    def Reset(self):
        self.x = self.s_width / 2 - 6
        self.y = self.s_height / 2 - 6
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.dx = 0
        self.dy = 0

    def update(self, dt):
        self.rect.x += self.dx*dt
        self.rect.y += self.dy*dt

    def render(self):
        pygame.draw.rect(self.screen, (51, 255, 51), self.rect)
