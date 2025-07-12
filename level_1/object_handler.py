from sprite_object import *
from npc import *
from random import choices, randrange

class ObjectHandler():
    def __init__(self,game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'sprites/npc/'
        self.static_sprite_path  = 'sprites/static_sprites/'
        self.anim_sprite_path  = 'sprites/animated_sprites/'
        add_sprite = self.add_sprite
        add_npc = self.add_npc
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
        add_npc(NPC(game))
        #add_npc1(SoldierNPC(game, pos = (11.5,4.5)))
        #add_npc(CacoDemonNPC(game, pos=(10.5, 4.5)))
        
    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if self.game.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]
            

        
        
    def update_draw(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if self.game.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update_draw() for npc in self.npc_list]
            
        
    def add_npc(self,npc):
        self.npc_list.append(npc)
        
    def add_sprite(self,sprite):
        self.sprite_list.append(sprite)