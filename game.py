import pygame
from pygame_utils.game.window import Window


class Game(Window):

    def __init__(self):
        super().__init__(background_color="white")

    def handle_event(self, event: pygame.event.Event):
        pass

    def update(self):
        pass

    def render(self):
        pass
