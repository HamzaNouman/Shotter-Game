import pygame as pg
from settings4 import *

class objrend4():
    def __init__(self,game):
        self.game = game
        self.screen = game.screen
        self.wall_texture = self.load_wall_texture()
        self.sky_image =self.get_texture('texture/sky.png', (width,half_height))
        self.sky_offset = 0
        self.blood_screen = self.get_texture('texture/blood_screen.png',res)
        self.digit_size = 90
        self.digit_images = [self.get_texture(f'texture/digits/{i}.png',[self.digit_size] * 2)
                             for i in range(11)]
        self.digits = dict(zip(map(str,range(11)), self.digit_images))
        self.game_over_image = self.get_texture('texture/game_over.png',res)
        self.vict_image = self.get_texture('texture/vic.png',res)
        
    def draw(self):
        self.draw_background()
        self.renderer_game_obj()
        self.draw_player_health()
        
    def game_over(self):
        self.screen.blit(self.game_over_image , (0,0))
        
    def vict(self):
        self.screen.blit(self.vict_image , (0,0))
        
        
    def draw_player_health(self):
        health = str(self.game.player4.health)
        for i,char in enumerate(health):
            self.screen.blit(self.digits[char],((i + 9) * self.digit_size,0))
        self.screen.blit(self.digits['10'],((i + 10) * self.digit_size,0))
        
    
        
    def player_damage(self):
        self.screen.blit(self.blood_screen,(0,0))
        
    def draw_background (self):
        self.sky_offset = (self.sky_offset + 4.5* self.game.player4.rel) % width
        self.screen.blit(self.sky_image , (-self.sky_offset,0))
        self.screen.blit(self.sky_image , (-self.sky_offset + width,0))
        pg.draw.rect(self.screen, floor_color , (0,half_height,width,height))
        
    def renderer_game_obj(self):
        list_obj = sorted(self.game.raycasting4.obj_to_reneder, key=lambda t: t[0], reverse=True)
        for depth , image,pos in list_obj:
            self.screen.blit(image,pos)
        
    @staticmethod
    def get_texture(path, Res = (texture_s,texture_s)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture , Res)
    
    def load_wall_texture(self):
        return {
            1: self.get_texture('texture/1.png'),
            2: self.get_texture('texture/2.png'),
            3: self.get_texture('texture/3.png'),
            4: self.get_texture('texture/4.png'),
            5: self.get_texture('texture/5.png')
            }
        