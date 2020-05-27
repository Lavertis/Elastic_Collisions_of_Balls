from world import *

world = World()

while world.bounce:
    world.check_for_exit_and_window_resize()
    world.check_for_collision()
    world.move_and_draw_balls()
    try:
        world.window.update()
        world.window.update_idletasks()
    except TclError:
        pass
world.exit()
