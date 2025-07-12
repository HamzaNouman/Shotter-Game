import pygame as pg
import sys
sys.path.append('level_1')
sys.path.append('level_2')
sys.path.append('level_3')
sys.path.append('level_4')
sys.path.append('level_5')
import level_1
import level_2
import level_3
import level_4
from level_1.settings import *
from level_2.settings2 import *
from level_3.settings3 import *
from level_4.settings4 import *

class Game():
    def __init__(self):
        #global running,helper
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(res,pg.RESIZABLE|pg.FULLSCREEN)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.global_trigger = False
        self.enemies = 1
        self.global_event = pg.USEREVENT + 0 
        pg.time.set_timer(self.global_event , 40)
        self.alive = True
        self.alive1 = True
        self.alive2 = True
        self.alive3 = True
        self.alive4 = True
        self.alive5 = True
        self.alive6 = True
        self.alive7 = True
        self.alive8 = True
        self.running = False
        self.helper = False
        self.helper2 = 1
        self.help = 1    
        self.fullsc = False   
        self.new_game()
        #self.new_game1()

        
        
        
    def new_game(self):
        self._map = level_1.Map(self)
        self.player = level_1.Player(self)
        self.object_renderer = level_1.objrend(self)
        self.raycasting = level_1.Raycast(self)
        self.object_handler = level_1.ObjectHandler(self)
        self.weapon = level_1.Weapon(self)
        self.sound = level_1.Sound(self)
        self.pathfinding = level_1.PathFinding(self)
        self.npc = level_1.NPC(self)
        


    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.weapon.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FBS)
        pg.display.set_caption(f'{self.clock.get_fps():.1f}')
        
        
    def new_game2(self):
        self.map2 = level_2.Map2(self)
        self.player2 = level_2.Player2(self)
        self.object_renderer2 = level_2.objrend2(self)
        self.raycasting2 = level_2.Raycast2(self)
        self.object_handler2 = level_2.ObjectHandler2(self)
        self.weapon2 = level_2.Weapon2(self)
        self.sound2 = level_2.Sound2(self)
        self.pathfinding2 = level_2.PathFinding2(self)
        self.npc2 = level_2.NPC2(self)

        


    def update2(self):
        self.player2.update()
        self.raycasting2.update()
        self.object_handler2.update()
        self.object_handler2.update2()
        self.weapon2.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FBS)
        pg.display.set_caption(f'{self.clock.get_fps():.1f}')

    def new_game3(self):
        self.map3 = level_3.Map3(self)
        self.player3 = level_3.Player3(self)
        self.object_renderer3= level_3.objrend3(self)
        self.raycasting3 = level_3.Raycast3(self)
        self.object_handler3 = level_3.ObjectHandler3(self)
        self.weapon3 = level_3.Weapon3(self)
        self.sound3 = level_3.Sound3(self)
        self.pathfinding3 = level_3.PathFinding3(self)
        self.npc3 = level_3.NPC3(self)

        


    def update3(self):
        self.player3.update()
        self.raycasting3.update()
        self.object_handler3.update()
        self.object_handler3.update2()
        #self.object_handler2.update2()
        self.weapon3.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FBS)
        pg.display.set_caption(f'{self.clock.get_fps():.1f}')

    def new_game4(self):
        self.map4 = level_4.Map4(self)
        self.player4 = level_4.Player4(self)
        self.object_renderer4= level_4.objrend4(self)
        self.raycasting4 = level_4.Raycast3(self)
        self.object_handler4 = level_4.ObjectHandler4(self)
        self.weapon4 = level_4.Weapon4(self)
        self.sound4 = level_4.Sound4(self)
        self.pathfinding4 = level_4.PathFinding4(self)
        self.npc4 = level_4.NPC4(self)

        


    def update4(self):
        self.player4.update()
        self.raycasting4.update()
        self.object_handler4.update()
        self.object_handler4.update2()
        #self.object_handler2.update2()
        self.weapon4.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FBS)
        pg.display.set_caption(f'{self.clock.get_fps():.1f}')
        
        
    def draw(self):
        self.screen.fill('black')
        self.object_renderer.draw()
        self.weapon.draw()

    def draw2(self):
        self.screen.fill('black')
        self.object_renderer2.draw()
        self.weapon2.draw()

    def draw3(self):
        self.screen.fill('black')
        self.object_renderer3.draw()
        self.weapon3.draw()

    def draw4(self):
        self.screen.fill('black')
        self.object_renderer4.draw()
        self.weapon4.draw()
        
    def check_event(self):
        self.global_trigger = False
        self.enemies = 1
        for event in pg.event.get():

            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
                
            if self.help == 1:
                self.player.single_fire_event(event)
                
            if self.help == 2:
                self.player2.single_fire_event(event)

            if self.help == 3:
                self.player3.single_fire_event(event)

            if self.help == 4:
                self.player3.single_fire_event(event)

            if event.type == pg.VIDEORESIZE:
                if not self.fullsc:
                    self.screen = pg.display.set_mode((event.w,event.h),pg.RESIZABLE)
                
                
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_f :
                    self.fullsc = not self.fullsc
                    if self.fullsc :
                        self.screen = pg.display.set_mode((self.screen.get_width(),self.screen.get_height()),pg.FULLSCREEN)
                    
                    else:
                        self.screen = pg.display.set_mode((1200,600),pg.RESIZABLE)

                if event.key == pg.K_q and self.helper == False:
                    self.running = True
                    self.helper = True
                    
                elif event.key == pg.K_q and self.helper == True:
                    self.running = False
                    self.helper = False
                                    

            else:
                self.global_trigger = True
                


            
        if self.running == True and self.help == 1:
            self._map.draw()
            self.player.draw()
            self.object_handler.update_draw()

        if self.running == True and self.help == 2:
            self.map2.draw()
            self.player2.draw()
            self.object_handler2.update_draw()
            self.object_handler2.update_draw2()

        if self.running == True and self.help == 3:
            self.map3.draw()
            self.player3.draw()
            self.object_handler3.update_draw()
            self.object_handler3.update_draw2()

        if self.running == True and self.help == 4:
            self.map4.draw()
            self.player4.draw()
            self.object_handler4.update_draw()
            self.object_handler4.update_draw2()



        
        
        if self.help == 1:
            self.update()  
            self.draw()
            
        if self.help == 2:
            self.update2() 
            self.draw2()

        if self.help == 3:
            self.update3() 
            self.draw3()

        if self.help == 4:
            self.update4() 
            self.draw4()
            

        
    def run (self):
        while True:
            self.check_event()
            
            


            
if __name__ == '__main__' :
     game = Game()
     game.run()
    