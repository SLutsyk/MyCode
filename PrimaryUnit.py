import os

import pygame


def wall_generator(level):
    global walls
    walls[0], walls[1], walls[2] = (
        level[0],
        level[1],
        level[2],
    )
    walls[3] = [
        level[2][0],
        level[2][1] - (level[1][1] * 3),
    ]
    walls[4] = [
        level[1][0],
        level[1][1] - (level[1][1] * 3),
    ]
    walls[5] = [
        level[0][0],
        level[0][1] - (level[1][1] * 3),
    ]


def obstacle_generator(obstacle, level):
    obstacle[1][0] = [
        obstacle[0][0][0] + level[0][0],
        obstacle[0][0][1] + level[1][1],
    ]
    obstacle[1][1] = [
        obstacle[0][0][0] + level[0][0],
        obstacle[0][0][1] - (level[1][1] * 0.5),
    ]
    obstacle[1][2] = [
        obstacle[0][1][0] + level[0][0],
        obstacle[0][1][1] - (level[1][1] * 0.5),
    ]
    obstacle[1][3] = [
        obstacle[0][2][0] + level[0][0],
        obstacle[0][2][1] - (level[1][1] * 0.5),
    ]
    obstacle[1][4] = [
        obstacle[0][2][0] + level[0][0],
        obstacle[0][2][1] + level[1][1],
    ]
    obstacle[1][5] = [
        obstacle[0][3][0] + level[0][0],
        obstacle[0][3][1] + level[1][1],
    ]


def obstacle_hitbox(bl, br, tl, tr, x, y):
    point1 = [(bl[0] + br[0]) / 2, (bl[1] + br[1]) / 2]
    point2 = [(tl[0] + tr[0]) / 2, (tl[1] + tr[1] + 64) / 2]
    half_thicness = (br[0] - bl[0]) / 2
    obstacle_n_border = []
    obstacle_p_border = []
    point1n = 0
    point1p = 0
    while point1[0] < point2[0]:
        point1n = point1[0] - half_thicness
        obstacle_n_border.append([point1n, point1[1]])
        point1p = point1[0] + half_thicness
        obstacle_p_border.append([point1p, point1[1]])
        point1[0] += x
        point1[1] -= y
    return obstacle_n_border, obstacle_p_border


class ShapeMovement:
    def __init__(self, coordinates, x, y, high_ratio, low_ratio):  # todo: rename x, y to h_displacement etc
        self.coordinates = coordinates
        self.x = x
        self.y = y
        self.z1 = x * high_ratio
        self.z2 = y * low_ratio

    def horizontal(self, direction):
        for value in self.coordinates:
            value[0] += direction * self.x

    def vertical(self, direction):
        for value in self.coordinates:
            value[1] += direction * self.y

    def diagonal_hk(self, *direction):
        for value in self.coordinates:
            value[1] += direction[1] * self.z2
            value[0] += direction[0] * self.z1

    def diagonal_vk(self, *direction):
        for value in self.coordinates:
            value[1] += direction[1] * self.z1
            value[0] += direction[0] * self.z2


class LevelCollision:
    def __init__(self, v_correction, h_correction, half_level_height, x):
        self.v_correction = v_correction
        self.h_correction = h_correction
        self.half_level_height = half_level_height
        self.x = x

    def t_left(self, vc_corner, hc_corner):
        return vc_corner - (self.h_correction / self.x) < self.half_level_height - (
                    hc_corner / self.x)

    def b_left(self, vc_corner, hc_corner):
        return vc_corner + (self.h_correction / self.x) > self.half_level_height + (
                    hc_corner / self.x)

    def t_right(self, vc_corner, hc_corner):
        return vc_corner + (self.h_correction / self.x) < -(
                (self.half_level_height - self.v_correction) - (
                (hc_corner / self.x) + self.v_correction))

    def b_right(self, vc_corner, hc_corner):
        return vc_corner - (self.h_correction / self.x) > (
            self.half_level_height
            + self.half_level_height
            - self.v_correction
        ) + (
            self.half_level_height
            - ((hc_corner / self.x) + self.v_correction)
        )


def main(params):
    shape_movement = ShapeMovement(
        coordinates=params.coordinates,
        x=params.h_displacement,
        y=params.d_displacement,
        high_ratio=params.high_ratio,
        low_ratio=params.low_ratio
    )

    level_collision = LevelCollision(
        v_correction=params.level[1][1],
        h_correction=params.level[0][0],
        half_level_height=params.level[0][1],
        x=params.h_displacement
    )

    class Game:
        def __init__(self):
            self.running = False

        def start(self):
            self.running = True
            while self.running:
                self.handle_quit()
                keys = pygame.key.get_pressed()

        def handle_quit(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

        def _render(self):
            pygame.draw.polygon(screen, (255, 255, 255), level)
            pygame.draw.polygon(screen, (200, 75, 0), walls)
            pygame.draw.polygon(screen, (255, 0, 0), shape, 1)
            pygame.draw.polygon(screen, (20, 75, 0), obstacle1[1])
            pygame.display.update()
            screen.fill((0, 0, 0))
            clock.tick(120)

        def handle_key_left(self):
            pass

        def handle_key_right(self):
            pass

        def handle_key_up(self):
            pass

        def handle_key_down(self):
            pass

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            #  вертикальні   відступ лівого кута половина висоти     горизонтальні координати
            #  координати    рівня від екрану /  рівня               лівого кута / на
            #  лівого кута   на коефіцієнт х                         коефіцієнт х
            if shape[0][0] < level[0][0]:
                continue
            elif level_collision.t_left(shape[0][1], shape[0][0]):
                shape_movement.diagonal_hk(-1, 1)
            elif level_collision.b_left(shape[0][1], shape[0][0]):
                shape_movement.diagonal_hk(-1, -1)
            else:
                shape_movement.horizontal(-1)
        if keys[pygame.K_RIGHT]:
            if shape[2][0] > level[2][0]:
                continue
            elif level_collision.t_right(shape[2][1], shape[2][0]):
                shape_movement.diagonal_hk(1, 1)
            elif level_collision.b_right(shape[2][1], shape[2][0]):
                shape_movement.diagonal_hk(1, -1)
            else:
                shape_movement.horizontal(1)
        if keys[pygame.K_UP]:
            if shape[1][1] - 34 < level[1][1]:
                continue
            elif level_collision.t_left(shape[0][1], shape[0][0]):
                shape_movement.diagonal_hk(1, -1)
            elif level_collision.t_right(shape[2][1], shape[2][0]):
                shape_movement.diagonal_hk(-1, -1)
            else:
                shape_movement.vertical(-1)
        if keys[pygame.K_DOWN]:
            if shape[2][1] + 17 > level[3][1]:
                continue
            else:
                shape_movement.vertical(1)

        pygame.draw.polygon(screen, (255, 255, 255), level)
        pygame.draw.polygon(screen, (200, 75, 0), walls)
        pygame.draw.polygon(screen, (255, 0, 0), shape, 1)
        pygame.draw.polygon(screen, (20, 75, 0), obstacle1[1])
        pygame.display.update()
        screen.fill((0, 0, 0))
        clock.tick(120)


if __name__ == '__main__':
    x = 7
    y = 29
    os.environ["SDL_VIDEO_WINDOW_POS"] = "%d,%d" % (x, y)
    pygame.init()
    screen = pygame.display.set_mode((1586, 822))
    pygame.display.set_caption("Primary Unit")

    shape = [
        [10, 275],
        [42, 292],
        [74, 275],
        [74, 211],
        [42, 194],
        [10, 211],
    ]
    level = [[80, 443], [793, 64], [1506, 443], [793, 822]]
    walls = [[], [], [], [], [], []]
    obstacle1 = [
        [[87, 379], [407, 209], [471, 243], [151, 413]],
        [[], [], [], [], [], []],
    ]
    obstacle2 = [
        [[471, 175], [663, 73], [727, 107], [535, 209]],
        [[], [], [], [], [], []],
    ]

    level_horizontal_dimention = level[2][0] - level[0][0]
    level_vertical_dimention = level[3][1] - level[1][1]
    level_catet = ((level_horizontal_dimention ** 2) + (level_vertical_dimention ** 2)) ** 0.5
    low_ratio = (level_vertical_dimention / level_horizontal_dimention) * 2
    high_ratio = (1 - (level_vertical_dimention / level_horizontal_dimention)) * 2
    v_displacement = 1
    h_displacement = level_horizontal_dimention / level_vertical_dimention
    d_displacement = (level_catet / level_vertical_dimention) / 2

    print(level_catet / level_vertical_dimention)

    wall_generator(level)
    obstacle_generator(obstacle1, level)

    done = False
    clock = pygame.time.Clock()

    from types import SimpleNamespace

    params = SimpleNamespace(
        level=level,
        coordinates=shape,
        h_displacement=h_displacement,
        d_displacement=d_displacement,
        low_ratio=low_ratio,
        high_ratio=high_ratio
    )

    main(params=params)
