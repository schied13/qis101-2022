#!/usr/bin/env python3
# ifs_hexagonal.py
from simple_screen import SimpleScreen
from ifs import IteratedFunctionSystem

ifs = IteratedFunctionSystem()


def plot_ifs(ss):
    iterations = 200_000
    #centered at 15,15
    x, y = 15, 15

    # Iterate (but don't draw) to let IFS reach its stable orbit
    for _ in range(100):
        x, y, color = ifs.transform_point(x, y)

    for _ in range(iterations):
        x, y, color = ifs.transform_point(x, y)
        ss.set_world_pixel(x, y, color)


def main():
    #(0,0) to (30,30) base frame
    ifs.set_base_frame(0, 0, 30, 30)

    p = 1 / 6
    ifs.add_mapping(25, 15, 15, 15, 20, 25, "blue", p)#COD
    ifs.add_mapping(20, 25, 15, 15, 10, 25, "blue", p)#DOE
    ifs.add_mapping(10, 25, 15, 15, 5, 15, "blue", p)#EOF
    ifs.add_mapping(5, 15, 15, 15, 10, 5, "blue", p)#FOA
    ifs.add_mapping(10, 5, 15, 15, 20, 5, "blue", p)#AOB
    ifs.add_mapping(20, 5, 15, 15, 25, 15, "blue", p)#BOC

    ifs.generate_transforms()

    ss = SimpleScreen(
        world_rect=((0, 0), (30, 30)),
        screen_size=(900, 900),
        draw_function=plot_ifs,
        title="Hexagon",
    )
    ss.show()


if __name__ == "__main__":
    main()
