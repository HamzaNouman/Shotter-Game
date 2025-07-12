from sprite_object4 import *
from npc4 import *
from npc4_2 import *
from npc4_3 import *
from random import choices, randrange

class ObjectHandler4():
    def __init__(self,game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'sprites/npc/'
        self.static_sprite_path  = 'sprites/static_sprites/'
        self.anim_sprite_path  = 'sprites/animated_sprites/'
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        add_npc2 = self.add_npc2
        add_npc3 = self.add_npc3
        self.npc_positions = {}
        
        #self.enemies = 1  # npc count
        #self.npc_types = [SoldierNPC]
        #self.weights = [10]
        #self.restricted_area = {(i, j) for i in range(1) for j in range(1)}
        #self.spawn_npc()
        
        #sprite_map
        #add_sprite(Sprite(game))
        add_sprite(Animated_spr(game,pos=(1.5,1.5)))
        add_sprite(Animated_spr(game,pos=(1.5,7.5)))
        add_sprite(Animated_spr(game,pos=(5.5,3.25)))
        add_sprite(Animated_spr(game,pos=(5.5,4.75)))
        add_sprite(Animated_spr(game,pos=(7.5,2.5)))
        add_sprite(Animated_spr(game,pos=(14.5,1.5)))
        add_sprite(Animated_spr(game,pos=(14.5,7.5)))
        add_sprite(Animated_spr(game,pos=(12.5,7.5)))
        add_sprite(Animated_spr(game,pos=(9.5,7.5)))
        
        #npc map
        #add_npc(NPC3(game))
        #add_npc1(SoldierNPC(game, pos = (11.5,4.5)))
        add_npc(CacoDemonNPC(game, pos=(10.5, 4.5)))
        add_npc2(CacoDemonNPC4(game, pos=(2, 2)))
        add_npc3(CyberDemonNPC4(game, pos=(2, 2)))
        
    def update(self):
        self.npc_positions = {npc4.map_pos for npc4 in self.npc_list if self.game.alive6}
        [sprite.update() for sprite in self.sprite_list]
        [npc4.update() for npc4 in self.npc_list]
            

        
        
    def update_draw(self):
        self.npc_positions = {npc4.map_pos for npc4 in self.npc_list if self.game.alive6}
        [sprite.update() for sprite in self.sprite_list]
        [npc4.update_draw() for npc4 in self.npc_list]
            
        
    def add_npc(self,npc4):
        self.npc_list.append(npc4)

    def update2(self):
        self.npc_positions = {npc4_2.map_pos for npc4_2 in self.npc_list if self.game.alive7}
        [sprite.update() for sprite in self.sprite_list]
        [npc4_2.update() for npc4_2 in self.npc_list]
            

        
        
    def update_draw2(self):
        self.npc_positions = {npc4_2.map_pos for npc4_2 in self.npc_list if self.game.alive7}
        [sprite.update() for sprite in self.sprite_list]
        [npc4_2.update_draw() for npc4_2 in self.npc_list]
            
        
    def add_npc2(self,npc4_2):
        self.npc_list.append(npc4_2)

    def update3(self):
        self.npc_positions = {npc4_3.map_pos for npc4_3 in self.npc_list if self.game.alive8}
        [sprite.update() for sprite in self.sprite_list]
        [npc4_3.update() for npc4_3 in self.npc_list]
            

        
        
    def update_draw3(self):
        self.npc_positions = {npc4_3.map_pos for npc4_3 in self.npc_list if self.game.alive8}
        [sprite.update() for sprite in self.sprite_list]
        [npc4_3.update_draw() for npc4_3 in self.npc_list]
            
        
    def add_npc3(self,npc4_3):
        self.npc_list.append(npc4_3)
        
    def add_sprite(self,sprite):
        self.sprite_list.append(sprite)