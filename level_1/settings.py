import math
import pygame as pg
import os
pg.init()

os.environ['SDL_VEDIO_CENTERED'] = '1'
info  = pg.display.Info()

res = width,height = info.current_w,info.current_h
half_width = width //2
half_height = height //2
FBS = 120

player_pos= 1.5,5
player_angle= 0
player_speed= 0.004
player_rot_speed= 0.002
player_s_scale = 60
player_max_health = 100
helper9 = 1

mouse_sens = 0.0003
mouse_maxrel = 40
mouse_border_left =  100
mouse_border_right  = width - mouse_border_left

floor_color = (30,30,30)

fov = math.pi / 3
half_fov = fov / 2
num_ray = width // 2
half_num_ray = num_ray // 2
delta_angle = fov / num_ray
max_depth = 20

screen_dist = half_width / math.tan(half_fov)
scale = width // num_ray

texture_s = 256
half_tex_s = texture_s // 2 