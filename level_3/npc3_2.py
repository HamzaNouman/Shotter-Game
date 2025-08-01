from sprite_object3 import *
from random import choice,randint,random
from settings3 import *

class NPC3(Animated_spr):
    def __init__(self,game,path = 'sprites/npc/soldier/0.png',pos = (10.5 , 5.5),scale =0.5,shift=0.0,animated_time=220):
        super().__init__(game,path ,pos,scale ,shift,animated_time)
        self.attack_images = self.get_images(self.path + '/attack')
        self.death_images = self.get_images(self.path + '/death')
        self.idle_images = self.get_images(self.path + '/idle')
        self.pain_images = self.get_images(self.path + '/pain')
        self.walk_images = self.get_images(self.path + '/walk')
        self.game = game
        
        self.attack_dist = randint(3,6)
        self.speed = 0.03
        self.size =10
        self.health = 100
        self.attack_damage = 10
        self.accuracy = 0.15
        #self.alive =True
        self.pain = False
        self.ray_cast_value=False
        self.frame_counter = 0
        self.search_player_trigger = False
        
    def update(self):
        self.check_animation_time()
        self.get_sprite()
        self.run_logic()
        #self.draw_ray_cast()
        
    def update_draw(self):
        #self.check_animation_time()
        #self.get_sprite()
        #self.run_logic()
        self.draw_ray_cast()
        
    def check_wall(self, x,y):
        return (x,y) not in self.game.map3.world_map
    
    def check_wallc(self,dx,dy):
        if self.check_wall(int(self.x +dx * self.size),int(self.y)):
            self.x +=dx    
            
        if self.check_wall(int(self.x),int(self.y + dy * self.size)):
            self.y +=dy
        
    def movement(self):
        next_pos = self.game.pathfinding3.get_path(self.map_pos, self.game.player3.map_pos)
        next_x , next_y = next_pos
        
        if next_pos not in self.game.object_handler3.npc_positions:
                    #pg.draw.rect(self.game.screen, 'blue',(75 * next_x,66 * next_y,75,66))
                    angle = math.atan2(next_y +0.5 -self.y,next_x +0.5 - self.x)
                    dx = math.cos(angle) * self.speed
                    dy = math.sin(angle) * self.speed
                    self.check_wallc(dx,dy)
                    
    def attack(self):
        if self.animation_trigger:
            self.game.sound3.npc_attack.play()
            if random() <self.accuracy:
                self.game.player3.get_damage(self.attack_damage)

    def animate_death(self):
        if not self.game.alive5:
            if self.game.global_trigger and self.frame_counter < len(self.death_images) - 1:
                self.death_images.rotate(-1)
                self.image = self.death_images[0]
                self.frame_counter += 1
                


            
                
        #print(self.alive)
    def animate_pain(self):
        self.animate(self.pain_images)
        if self.animation_trigger:
            self.pain = False
        
    def check_hit_in_npc(self):
        if self.ray_cast_value and self.game.player3.shot:
            if half_width - self.sprite_half_width < self.screen_x < half_width + self.sprite_half_width:
                self.game.sound3.npc_pain.play()
                self.game.player3.shot = False
                self.pain = True
                self.health -= self.game.weapon.damage
                self.check_health()
                
    def check_health(self):
        if self.health <1:
            self.game.alive5 = False
            self.game.sound3.npc_death.play()
        
    def run_logic(self):
        if self.game.alive5:
            self.ray_cast_value = self.ray_cast_player_npc()
            self.check_hit_in_npc()
            if self.pain:
                self.animate_pain()
                
            elif self.ray_cast_value:
                self.search_player_trigger = True
                
                if self.dist < self.attack_dist:
                    self.animate(self.attack_images)
                    self.attack()
                else:
                    self.animate(self.walk_images)
                    self.movement()
                
            elif self.search_player_trigger:
                self.animate(self.walk_images)
                self.movement()
                
            else:
                self.animate(self.idle_images)
                
        else:
            self.animate_death()
            
    @property
    def map_pos(self):
        return int(self.x),int(self.y)
    
    def ray_cast_player_npc(self):
        if self.game.player3.map_pos == self.map_pos:
            return True
        
        wall_dist_v , wall_dist_h = 0,0
        player_dist_v , player_dist_h = 0,0
        
        ox,oy = self.game.player3.pos
        x_map,y_map= self.game.player3.map_pos
        
        ray_angle = self.theta
        
        sin_a = math.sin(ray_angle)
        cos_a = math.cos(ray_angle)
        
        y_hor,dy = (y_map +1,1) if sin_a>0 else(y_map - 1e-6,-1)
        
        depth_hor =  (y_hor - oy) /sin_a
        x_hor = ox + depth_hor * cos_a
        
        delta_depth = dy / sin_a
        dx =delta_depth * cos_a
            
        for i in range(max_depth):
            tile_hor = int(x_hor),int(y_hor)
            if tile_hor == self.map_pos:
                player_dist_h = depth_hor
                break
            if tile_hor in self.game.map3.world_map:
                wall_dist_h = depth_hor
                break
            x_hor += dx
            y_hor += dy
            depth_hor += delta_depth
        
        
        x_vert,dx = (x_map +1,1) if cos_a>0 else(x_map - 1e-6,-1)
        
        depth_vert =  (x_vert - ox) /cos_a
        y_vert = oy + depth_vert * sin_a
        
        delta_depth = dx / cos_a
        dy =delta_depth * sin_a
            
        for i in range(max_depth):
            tile_vert = int(x_vert),int(y_vert)
            if tile_vert == self.map_pos:
                player_dist_v = depth_vert
                break
            if tile_vert in self.game.map3.world_map:
                wall_dist_v = depth_vert
                break
            x_vert += dx
            y_vert += dy
            depth_vert += delta_depth
            
        player_dist = max(player_dist_v , player_dist_h)
        wall_dist = max(wall_dist_v , wall_dist_h)
        
        if 0 < player_dist < wall_dist or not wall_dist:
            return True
        return False
        
        
    def draw_ray_cast(self):
        if self.game.alive5:
            pg.draw.circle(self.game.screen, 'red',(15 * self.x,10 * self.y),4)
            #if self.ray_cast_player_npc():
               # pg.draw.line(self.game.screen , 'orange',(15 * self.game.player3.x,10 * self.game.player3.y),
                            #(15 * self.x,10 * self.y),2 )
        else:
            pass
        
        

class CacoDemonNPC3(NPC3):
    def __init__(self, game, path='sprites/npc/caco_demon/0.png', pos=(10.5, 6.5),
                 scale=0.7, shift=0.0, animation_time=250):
        super().__init__(game, path, pos, scale, shift, animation_time)
        self.attack_dist = 1.0
        self.health = 150
        self.attack_damage = 25
        self.speed = 0.05
        self.accuracy = 0.35