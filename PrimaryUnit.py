import os
import pygame

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
high_ratio = (1 - (level_vertical_dimention / level_horizontal_dimention)) *2
v_displacement = 1
h_displacement = level_horizontal_dimention / level_vertical_dimention
d_displacement = (level_catet / level_vertical_dimention) / 2

print(level_catet / level_vertical_dimention)

def wall_generator(level=level):
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


def obstacle_generator(obstacle, level=level):
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


def obstacle_hitbox(
    bl, br, tl, tr, x=h_displacement, y=v_displacement
):
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


def shape_movement(
    axis,
    *direction,
    coordinates=shape,
    x=h_displacement,
    y=v_displacement,
    z1=d_displacement * high_ratio,
    z2=d_displacement * low_ratio
):
    if axis == "horizontal":
        for value in coordinates:
            value[0] += direction[0] * x
    elif axis == "vertical":
        for value in coordinates:
            value[1] += direction[0] * y
    elif axis == "diagonal_hk":
        for value in coordinates:
            value[1] += direction[1] * z2
            value[0] += direction[0] * z1
    elif axis == "diagonal_vk":
        for value in coordinates:
            value[1] += direction[1] * z1
            value[0] += direction[0] * z2


def level_collision(
    vc_corner,
    hc_corner,
    direction,
    v_correction=level[1][1],
    h_correction=level[0][0],
    half_level_height=level[0][1],
    x=h_displacement,
):
    if direction == "t_left":
        return vc_corner - (
            h_correction / x
        ) < half_level_height - (hc_corner / x)
    elif direction == "b_left":
        return vc_corner + (
            h_correction / x
        ) > half_level_height + (hc_corner / x)
    elif direction == "t_right":
        return vc_corner + (h_correction / x) < -(
            (half_level_height - v_correction)
            - ((hc_corner / x) + v_correction)
        )
    elif direction == "b_right":
        return vc_corner - (h_correction / x) > (
            half_level_height
            + half_level_height
            - v_correction
        ) + (
            half_level_height
            - ((hc_corner / x) + v_correction)
        )


# obstacle1_point_list = obstacle_hitbox(obstacle[0], obstacle[1], obstacle[2], obstacle[4])

wall_generator()
obstacle_generator(obstacle1)
# obstacle_generator(obstacle2)

done = False
clock = pygame.time.Clock()

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
        elif level_collision(
            shape[0][1], shape[0][0], "t_left"
        ):
            shape_movement("diagonal_hk", -1, 1)
        elif level_collision(
            shape[0][1], shape[0][0], "b_left"
        ):
            shape_movement("diagonal_hk", -1, -1)
        else:
            shape_movement("horizontal", -1)
    if keys[pygame.K_RIGHT]:
        if shape[2][0] > level[2][0]:
            continue
        elif level_collision(
            shape[2][1], shape[2][0], "t_right"
        ):
            shape_movement("diagonal_hk", 1, 1)
        elif level_collision(
            shape[2][1], shape[2][0], "b_right"
        ):
            shape_movement("diagonal_hk", 1 , -1)
        else:
            shape_movement("horizontal", 1)
    if keys[pygame.K_UP]:
        if shape[1][1] - 34 < level[1][1]:
            continue
        elif level_collision(
            shape[0][1], shape[0][0], "t_left"
        ):
            shape_movement("diagonal_hk", 1, -1)
        elif level_collision(
            shape[2][1], shape[2][0], "t_right"
        ):
            shape_movement("diagonal_hk", -1 * low_ratio, -1 * high_ratio)
        else:
            shape_movement("vertical", -1)
    if keys[pygame.K_DOWN]:
        if shape[2][1] + 17 > level[3][1]:
            continue
        # elif level_collision(
        #     shape[2][1], shape[2][0], "b_right"
        # ):
        #     shape_movement("diagonal_vk", -1 * high_ratio, 1 * low_ratio)
        # elif level_collision(
        #     shape[0][1], shape[0][0], "b_left"
        # ):
        #     shape_movement("diagonal_vk", 1 * high_ratio, 1 * low_ratio)
        else:
            shape_movement("vertical", 1)


    
    pygame.draw.polygon(screen, (255, 255, 255), level)
    pygame.draw.polygon(screen, (200, 75, 0), walls)
    pygame.draw.polygon(screen, (255, 0, 0), shape, 1)
    pygame.draw.polygon(screen, (20, 75, 0), obstacle1[1])
    # pygame.draw.polygon(screen, (20, 75, 0), obstacle2[1])
    pygame.display.update()
    screen.fill((0, 0, 0))
    clock.tick(120)
