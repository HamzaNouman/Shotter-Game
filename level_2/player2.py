from settings2 import * 
import pygame as pg
import math

class Player2():
    def __init__(self,game):
        
        self.game = game
        self.x,self.y = player_pos
        self.angle = player_angle
        self.shot = False
        self.health = player_max_health
        self.helper3 = helper9
        self.rel = 0
        self.health_recovery_delay = 700
        self.time_prev = pg.time.get_ticks()

        
    def recover_health(self):
        if self.check_health_recovery_delay() and self.health < player_max_health:
            self.health +=1
        
    def check_health_recovery_delay(self):
        time_now = pg.time.get_ticks()
        if time_now - self.time_prev > self.health_recovery_delay:
            self.time_prev = time_now
            return True
        
    def check_game_over(self):
        if self.health < 1:
            self.game.object_renderer2.game_over()
            pg.display.flip()
            self.game.helper2 = True
            pg.time.delay(1500)
            self.game.new_game2()
            
    def check_vict(self):
        if self.game.alive2 == False and self.game.alive3 == False:
            self.game.object_renderer2.vict()
            self.game.help = 3
            pg.display.flip()
            pg.time.delay(1500)
            self.game.new_game3()
            

            
        
        
            
        
    def get_damage(self,damage):
        self.health -= damage
        self.game.object_renderer2.player_damage()
        self.game.sound2.player_pain.play()
        self.check_game_over()
        
    def single_fire_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and not self.shot and not self.game.weapon2.reloading:
                self.game.sound2.shotgun.play()
                self.shot=True
                self.game.weapon2.reloading = True

        
    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx,dy =0,0
        speed = player_speed * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a
        
        keys = pg.key.get_pressed()
        
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
            
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
            
        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
            
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos
            
        self.check_wallc(dx, dy)
        
    #    if keys[pg.K_LEFT]:
     #       self.angle -= player_rot_speed * self.game.delta_time
            
      #  if keys[pg.K_RIGHT]:
        #    self.angle += player_rot_speed * self.game.delta_time
            
        self.angle %= math.tau
            
    def check_wall(self, x,y):
        return (x,y) not in self.game.map2.world_map
    
    def check_wallc(self,dx,dy):
        Scale = player_s_scale / self.game.delta_time
        if self.check_wall(int(self.x +dx * Scale),int(self.y)):
            self.x +=dx
            
            
        if self.check_wall(int(self.x),int(self.y + dy * Scale)):
            self.y +=dy
            
    
    def draw(self):
        #pg.draw.line(self.game.screen,'yellow',(self.x * 15 , self.y *10),
                     #(self.x * 15 + width * math.cos(self.angle),
                      #self.y * 10 + width * math.sin(self.angle)),2)
        pg.draw.circle(self.game.screen, 'green', (self.x * 15, self.y *10),4)
        
    def mouse_control(self):
        mx , my = pg.mouse.get_pos()
        if mx< mouse_border_left or mx > mouse_border_right:
            pg.mouse.set_pos([half_width,half_height])
        self.rel = pg.mouse.get_rel()[0]
        self.rel = max(-mouse_maxrel,min (mouse_maxrel,self.rel ))
        self.angle += self.rel  * mouse_sens * self.game.delta_time
    
    def update(self):
        self.movement()
        self.mouse_control()
        self.recover_health()
        self.check_vict()
        
    @property    
    def pos(self):
        return self.x,self.y
    @property    
    def map_pos(self):
        return int (self.x),int (self.y)
        