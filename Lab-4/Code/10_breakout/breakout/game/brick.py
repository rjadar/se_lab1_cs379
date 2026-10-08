"""
Brick: a single block with different types and durability.
"""

import pygame


class Brick:
    def __init__(self, x, y, width, height, brick_type="normal"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.brick_type = brick_type

        if brick_type == "normal":
            self.hits_remaining = 1
            self.color = (200, 90, 90)
        elif brick_type == "strong":
            self.hits_remaining = 3
            self.color = (90, 120, 220)
        elif brick_type == "unbreakable":
            self.hits_remaining = float("inf")
            self.color = (130, 130, 130)
        else:
            raise ValueError(f"Unknown brick type: {brick_type}")

    def get_rect(self):
        return pygame.Rect(
            int(self.x),
            int(self.y),
            self.width,
            self.height,
        )