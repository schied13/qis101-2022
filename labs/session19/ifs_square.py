#!/usr/bin/env python3
# ifs_square.py

from simple_screen import SimpleScreen
from ifs import IteratedFunctionSystem

ifs = IteratedFunctionSystem()


def plot_ifs(ss):
    iterations = 200_000
    x, y = 0, 0

    # Iterate (but don't draw) to let IFS reach its stable orbit
    for _ in range(100):
        x, y, color = ifs.transform_point(x, y)

    for _ in range(iterations):
        x, y, color = ifs.transform_point(x, y)
        ss.set_world_pixel(x, y, color)


def main():
    #declaring base frame to be (0,0) to (4,4)
    ifs.set_base_frame(0, 0, 4, 4)

    #Equal probability that it will be either mapping
    p = 1 / 4

    ifs.add_mapping(0, 0, 2, 0, 0, 2, "blue", p)
    ifs.add_mapping(2, 0, 4, 0, 2, 2, "yellow", p)
    ifs.add_mapping(0, 2, 2, 2, 0, 4, "red", p)
    ifs.add_mapping(2, 2, 4, 2, 2, 4, "green", p)

    ifs.generate_transforms()

    ss = SimpleScreen(
        world_rect=((-2, -2), (6, 6)),
        screen_size=(900, 900),
        draw_function=plot_ifs,
        title="IFS Square",
    )
    ss.show()


if __name__ == "__main__":
    main()
