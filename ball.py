import pygame
from vector import *


class Ball:
    def __init__(self, surface, colour, diameter, position_x, position_y, velocity_x, velocity_y):
        self.surface = surface
        self.colour = colour
        self.diameter = diameter
        self.radius = diameter / 2
        self.position = Vector2(position_x, position_y)
        self.velocity = Vector2(velocity_x, velocity_y)
        self.mass = 1

    def display(self):
        pygame.draw.ellipse(self.surface, self.colour, (self.position.x, self.position.y, self.diameter, self.diameter))

    def move(self, dt=1):
        self.position += self.velocity * dt

    def x_wall_collision(self, screen_width):
        return self.position.x < 0 and self.velocity.x < 0 \
               or self.position.x > screen_width - self.diameter and self.velocity.x > 0

    def y_wall_collision(self, screen_height):
        return self.position.y < 0 and self.velocity.y < 0 \
               or self.position.y > screen_height - self.diameter and self.velocity.y > 0

    def check_wall_collision(self, screen_width, screen_height):
        if self.x_wall_collision(screen_width):
            self.velocity.x *= -1
        if self.y_wall_collision(screen_height):
            self.velocity.y *= -1

    def collides(self, ball_2):
        return self is not ball_2 and math.hypot((self.position.x - ball_2.position.x),
                                                 (self.position.y - ball_2.position.y)) <= (self.radius + ball_2.radius)

    # Simplified solution
    def collision_simple(self, ball_2):
        delta_position = self.position - ball_2.position
        delta_velocity = self.velocity - ball_2.velocity
        distance = math.hypot(delta_position.x, delta_position.y)
        impact = -2 / distance * (delta_position.x * delta_velocity.x + delta_position.y * delta_velocity.y)
        if distance == 0 or impact < 0:
            return
        delta_position /= distance
        impact /= self.mass + ball_2.mass
        self.velocity += impact * ball_2.mass * delta_position
        ball_2.velocity -= impact * self.mass * delta_position

    # Advanced solution
    def collision_advanced(self, obj2):
        v1 = self.velocity
        v2 = obj2.velocity
        p1 = self.position
        p2 = obj2.position
        m1 = self.mass
        m2 = obj2.mass

        unit_norm = p2 - p1
        unit_norm.normalize()
        unit_tan = Vector2(-unit_norm.y, unit_norm.x)

        v1n = dot_product(unit_norm, v1)
        v1t = dot_product(unit_tan, v1)
        v2n = dot_product(unit_norm, v2)
        v2t = dot_product(unit_tan, v2)

        v1t_prime_scal = v1t
        v2t_prime_scal = v2t

        v1n_prime_scal = (v1n * (m1 - m2) + 2 * m2 * v2n) / (m1 + m2)
        v2n_prime_scal = (v2n * (m2 - m1) + 2 * m1 * v1n) / (m1 + m2)

        v1n_prime = v1n_prime_scal * unit_norm
        v1t_prime = v1t_prime_scal * unit_tan
        v2n_prime = v2n_prime_scal * unit_norm
        v2t_prime = v2t_prime_scal * unit_tan

        v1_prime = v1n_prime + v1t_prime
        v2_prime = v2n_prime + v2t_prime

        self.velocity = v1_prime
        obj2.velocity = v2_prime

        # Check if balls have overlapped each other.
        v1 = v1_prime
        v2 = v2_prime
        norm = p1 - p2
        distance = norm.get_magnitude()
        overlap = obj2.radius + self.radius - distance
        if overlap > 0:
            # Re-set the positions so the balls don't get stuck, by passing a small amount of time for the two balls.
            a = (v1 - v2).get_magnitude() ** 2
            b = dot_product(p1 - p2, v1 - v2)
            c = (p1 - p2).get_magnitude() ** 2 - (obj2.radius + self.radius) ** 2
            solutions = quadratic_formula(a, b, c)
            if solutions[0] > 0:
                delta_t = solutions[0]
            else:
                delta_t = solutions[1]
            self.move(delta_t)
            obj2.move(delta_t)
