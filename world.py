from random import choice, random, uniform
from ball import *
from controls import *


class World(Controls):
    def __init__(self):
        super().__init__()
        # PyGame window
        screen_height = self.window.winfo_screenheight()
        self.surface_height = round(0.75 * screen_height)
        self.surface_width = self.surface_height
        pygame.init()
        pygame.display.set_caption("Elastic Collisions of Balls")
        self.surface_size = [self.surface_width, self.surface_height]
        self.screen = pygame.display.set_mode(self.surface_size, pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.bounce = True
        self.balls = []
        self.number = 30
        self.number_change = self.number
        self.velocity = 1.5
        self.radius = 20
        self.colour = 'blue'
        self.colours = ['red', 'green', 'blue', 'orange', 'yellow', 'purple']
        self.create_balls()
        self.initialize_balls()
        # Controls window
        self.number_scale.config(command=self.update_balls_number)
        self.number_scale.set(self.number)
        self.radius_scale.config(command=self.update_balls_radius)
        self.radius_scale.set(self.radius)
        self.velocity_scale.config(command=self.update_balls_velocity)
        self.velocity_scale.set(self.velocity)
        self.colour_scale.config(command=self.update_balls_colour)
        self.colour_scale.set(self.colours.index(self.colour) + 1)
        self.reset_button.config(command=self.reset_balls)

    def create_balls(self):
        diameter = 2 * self.radius
        for i in range(self.number_change):
            velocity_coefficient = random()
            velocity_x = velocity_coefficient * self.velocity * choice([1, -1])
            velocity_y = math.sqrt(self.velocity ** 2 - velocity_x ** 2) * choice([1, -1])
            self.balls.append(
                Ball(surface=self.screen,
                     colour=pygame.color.Color(self.colour),
                     diameter=diameter,
                     position_x=uniform(diameter, self.surface_width - diameter),
                     position_y=uniform(diameter, self.surface_height - diameter),
                     velocity_x=velocity_x,
                     velocity_y=velocity_y))

    def initialize_balls(self, ):
        for _ in range(150):
            for ball_1 in self.balls:
                ball_1.check_wall_collision(self.surface_width, self.surface_height)
                for ball_2 in self.balls:
                    if ball_1.collides(ball_2):
                        ball_1.collision_simple(ball_2)
                        ball_1.move()
                        ball_2.move()

    def update_balls_number(self, value):
        if int(value) > self.balls.__len__():
            self.number_change = int(value) - self.number
            self.create_balls()
            self.number += int(value)
        else:
            for _ in range(self.number - int(value)):
                self.balls.pop(self.balls.__len__() - 1)
        self.number = int(value)
        self.update_balls_velocity(self.velocity_scale.get())
        self.update_balls_radius(self.radius_scale.get())
        self.update_balls_colour(self.colour_scale.get())

    def update_balls_velocity(self, value):
        velocity_coefficient = float(value) / self.velocity
        for ball in self.balls:
            ball.velocity *= velocity_coefficient
        self.velocity = float(value)

    def update_balls_radius(self, value):
        for ball in self.balls:
            ball.radius = int(value)
            ball.diameter = 2 * ball.radius

    def update_balls_colour(self, value):
        for ball in self.balls:
            ball.colour = pygame.color.Color(self.colours[int(value) - 1])

    def reset_balls(self):
        self.balls.clear()
        self.number = int(self.number_scale.get())
        self.number_change = int(self.number_scale.get())
        self.radius = int(self.radius_scale.get())
        self.velocity = float(self.velocity_scale.get())
        self.colour = self.colours[int(self.colour_scale.get()) - 1]
        self.create_balls()

    def exit(self):
        import sys
        self.window.quit()
        pygame.quit()
        sys.exit()
