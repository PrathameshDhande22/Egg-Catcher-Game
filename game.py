import sys
import threading
import time
import pygame
from pygame.locals import *
import random

class Game:
    def __init__(self):
        pygame.init()

        # game variables
        self.screen_height=700
        self.screen_width=900
        self.exit_game=False
        self.life=3
        self.score=0
        self.basket_x=self.screen_width/2
        self.basket_y=600
        self.egg_x=0
        self.egg_y=0
        self.count=0
        self.vy=5
        self.text=pygame.font.SysFont("papyrus",50,True)

        self.hen_no=random.randint(1,5)
        # self.hen_no=5

        self.window=pygame.display.set_mode((self.screen_width,self.screen_height))
        self.icon_img=pygame.image.load("Images/g_icon.png")
        pygame.display.set_icon(self.icon_img)
        pygame.display.set_caption("Egg Catcher Game BY Prathamesh Dhande")
        self.clock=pygame.time.Clock()
        self.__load_image()
        self.__gameloop__()

    def screen_placer(self,img,x,y):
        self.window.blit(img,(x,y))

    def __gameloop__(self):
        while not self.exit_game:
            self.clock.tick(40)
            self.screen_placer(self.back_img,0,0)
            if self.count==0:
                self.set_egg()
                self.count=1
            threading.Thread(target=self.loop_egg).start()
            self.screen_placer(self.basket_img,self.basket_x,self.basket_y)
            
            self.screen_placer(self.score_img,0,0)
            self.set_live()
            self.set_hens()
            for self.event in pygame.event.get():
                if self.event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.key_pressed=pygame.key.get_pressed()
            if self.key_pressed[K_LEFT]:
                self.basket_x+=-8
                
            elif self.key_pressed[K_RIGHT]:
                self.basket_x+=8

            # if the basket gets behind the walls so this is set
            if self.basket_x<0:
                self.basket_x=0
            elif self.basket_x>818:
                self.basket_x=818
            self.check_collison()
            self.score_text=self.text.render(str(self.score),True,(0,0,0))
            self.screen_placer(self.score_text,140,-15)
            self.egg_y+=self.vy
            pygame.display.update()

    def __load_image(self):
        # loads the background image
        self.back_img=pygame.image.load("Images/back_img.jpeg")
        self.back_img=pygame.transform.scale(self.back_img,(self.screen_width,self.screen_height))

        # loads the basket image
        self.basket_img=pygame.image.load("Images/basket.png")
        self.basket_img=pygame.transform.scale(self.basket_img,(90,90))

        # loads the egg_cracked image
        self.eggcracked_img=pygame.image.load("Images/egg_cracked.png")
        self.eggcracked_img=pygame.transform.scale(self.eggcracked_img,(60,60))

        # loads the egg image
        self.egg_img=pygame.image.load("Images/egg.png")
        self.egg_img=pygame.transform.scale(self.egg_img,(45,60))

        # loads the hen image
        self.hen_img=pygame.image.load("Images/hen.png")
        self.hen_img=pygame.transform.scale(self.hen_img,(140,110))

        # loads the score image
        self.score_img=pygame.image.load("Images/score.png")
        self.score_img=pygame.transform.scale(self.score_img,(130,50))

        # loads the life image
        self.life_img=pygame.image.load("Images/life.png")
        self.life_img=pygame.transform.scale(self.life_img,(40,50))



    def set_live(self):
        if self.life==3:
             self.screen_placer(self.life_img,850,6)
             self.screen_placer(self.life_img,800,6)
             self.screen_placer(self.life_img,750,6)

        elif self.life==2:
            self.screen_placer(self.life_img,850,6)
            self.screen_placer(self.life_img,800,6)

        elif self.life==1:
            self.screen_placer(self.life_img,850,6)

    def set_hens(self):
        pygame.draw.line(self.window,(150,75,0),(0,155),(900,155),width=30)
        self.screen_placer(self.hen_img,20,70) # hen 1
        self.screen_placer(self.hen_img,190,70) # hen 2
        self.screen_placer(self.hen_img,360,70) # hen 3
        self.screen_placer(self.hen_img,530,70) # hen 4
        self.screen_placer(self.hen_img,700,70) # hen 5

    def set_egg(self):
        if self.hen_no==1:
            self.egg_x=60
            self.egg_y=170
            
        elif self.hen_no==2:
            self.egg_x=230
            self.egg_y=170
            
        elif self.hen_no==3:
            self.egg_x=400
            self.egg_y=170
            
        elif self.hen_no==4:
            self.egg_x=570
            self.egg_y=170
            
        elif self.hen_no==5:
            self.egg_x=740
            self.egg_y=170
            
        # print(f"Hen no: {self.hen_no} x={self.egg_x} y={self.egg_y}")
        
    def loop_egg(self):
        # time.sleep(0.09)
        self.screen_placer(self.egg_img,self.egg_x,self.egg_y)

    def check_collison(self):
        if self.egg_y>self.screen_height-60:
            self.screen_placer(self.eggcracked_img,self.egg_x,self.egg_y)
            self.count=0
            self.hen_no=random.randint(1,5)
            self.life-=1
            print(f"distance y={abs(self.egg_x-self.basket_x)} and x={abs(self.basket_y-self.egg_y)}")
        if self.egg_y>570:
            pass
      



if __name__=="__main__":
    c=Game()