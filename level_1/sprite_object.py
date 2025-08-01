import pygame as pg
from settings import * 
from collections import deque
import os

class Sprite():
    def __init__(self,game, path = 'sprites/static_sprites/candlebra.png', pos = (10.5, 3.5),scale = 0.5 ,shift =0.0 ):
        self.game = game
        self.player = game.player
        self.x ,self.y = pos
        self.image = pg.image.load(path).convert_alpha()
        self.image_width = self.image.get_width()
        self.half_image_width=self.image.get_width() // 2
        self.image_ratio = self.image_width / self.image.get_height()
        self.dx , self.dy , self.screen_x ,self.theta, self.dist,self.norm_dist = 0,0,0,0,1,1
        self.sprite_half_width = 0
        self.sprite_scale = scale
        self.sprite_height_shift = shift
        
    def get_sprite_proj(self):
        proj = screen_dist /self.norm_dist * self.sprite_scale
        proj_width , proj_hight = proj* self.image_ratio , proj
        
        image = pg.transform.scale(self.image ,(proj_width,proj_hight))
        
        self.sprite_half_width = proj_width // 2
        height_shift = proj_hight * self.sprite_height_shift
        pos = self.screen_x - self.sprite_half_width,half_height - proj_hight //2 *height_shift
        
        self.game.raycasting.obj_to_reneder.append((self.norm_dist , image ,pos))
        
    def get_sprite(self):
        dx =self.x - self.player.x
        dy=self.y - self.player.y
        self.dx,self.dy = dx,dy
        self.theta = math.atan2(dy, dx)
        
        delta = self.theta - self.player.angle
        if (dx > 0 and self.player.angle >math.pi) or (dx<0 and dy < 0):
            delta += math.tau 
            
        delta_rays = delta / delta_angle
        self.screen_x = (half_num_ray + delta_rays) * scale
        
        self.dist = math.hypot(dx ,dy)
        self.norm_dist =self.dist * math.cos(delta)
        if -self.half_image_width < self.screen_x < (width + self.half_image_width) and self.norm_dist > 1 :
            self.get_sprite_proj()
    
    def update(self):
        self.get_sprite()
        
class Animated_spr(Sprite):
    def __init__(self,game, path = 'sprites/animated_sprites/0.png', pos = (11.5, 3.5) ,scale = 0.5 , shift = 0.0 , animated_time = 120):
        
        super().__init__(game, path, pos, scale, shift)
        self.animated_time = animated_time
        self.path = path.rsplit('/', 1)[0]
        self.images = self.get_images(self.path)
        self.animation_time_prev = pg.time.get_ticks()
        self.animation_trigger = False
        
    def update(self):
        super().update()
        self.check_animation_time()
        self.animate(self.images)

    def animate(self, images):
        if self.animation_trigger:
            images.rotate(-1)
            self.image = images[0]

    def check_animation_time(self):
        self.animation_trigger = False
        time_now = pg.time.get_ticks()
        if time_now - self.animation_time_prev > self.animated_time:
            self.animation_time_prev = time_now
            self.animation_trigger = True
 
        
    def get_images(self,path):
        images = deque()
        for file_name in os.listdir(path):
            if os.path.isfile(os.path.join(path, file_name)):
                img = pg.image.load(path + '/' + file_name).convert_alpha()
                images.append(img)
        return images
        
        
        