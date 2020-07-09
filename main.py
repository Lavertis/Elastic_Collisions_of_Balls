from world import *
from action import *

world = World()

while world.bounce:
    check_for_exit_and_window_resize(world)
    check_for_collision(world)
    move_and_draw_balls(world)
    try:
        world.window.update()
        world.window.update_idletasks()
    except TclError:
        pass
world.exit()
