import pygame


def check_for_exit_and_window_resize(world):
    for et in pygame.event.get():
        if et.type == pygame.QUIT:
            world.bounce = False
        elif et.type == pygame.VIDEORESIZE:
            world.surface_size = et.size
            world.surface_width = et.w
            world.surface_height = et.h
            world.screen = pygame.display.set_mode(world.surface_size, pygame.RESIZABLE)


def check_for_collision(world):
    for ball_1 in world.balls:
        ball_1.check_wall_collision(world.surface_width, world.surface_height)
        for ball_2 in world.balls:
            if ball_1.collides(ball_2):
                ball_1.collision_simple(ball_2)


def move_and_draw_balls(world):
    world.screen.fill((0, 0, 0))
    for ball in world.balls:
        ball.move()
        ball.display()
    world.fps = world.clock.get_fps()
    display_fps(world)
    world.clock.tick(60)
    pygame.display.flip()


def display_fps(world):
    text_surface = world.fps_font.render('FPS: ' + str(round(world.fps)), True, (120, 120, 120))
    world.screen.blit(text_surface, (2, 0))
