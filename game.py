import sys
import pygame
from pygame.locals import *

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
            self.screen_placer(self.back_img,0,50)
            self.screen_placer(self.bar_img,0,0)
            self.screen_placer(self.basket_img,self.basket_x,self.basket_y)
            self.screen_placer(self.score_img,0,0)
            self.set_live()
            for self.event in pygame.event.get():
                if self.event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.key_pressed=pygame.key.get_pressed()
            if self.key_pressed[K_LEFT]:
                self.basket_x+=-7
            elif self.key_pressed[K_RIGHT]:
                self.basket_x+=7

            if self.basket_x<0:
                self.basket_x=0
            elif self.basket_x>818:
                self.basket_x=818

            pygame.display.update()

    def __load_image(self):
        # loads the background image
        self.back_img=pygame.image.load("Images/back_img.jpeg")
        self.back_img=pygame.transform.scale(self.back_img,(self.screen_width,self.screen_height-50))

        # loads the bar image
        self.bar_img=pygame.image.load("Images/bar.png")
        self.bar_img=pygame.transform.scale(self.bar_img,(self.screen_width,50))

        # loads the basket image
        self.basket_img=pygame.image.load("Images/basket.png")
        self.basket_img=pygame.transform.scale(self.basket_img,(80,80))

        # loads the egg_cracked image
        self.eggcracked_img=pygame.image.load("Images/egg_cracked.png")
        self.eggcracked_img=pygame.transform.scale(self.eggcracked_img,(60,60))

        # loads the egg image
        self.egg_img=pygame.image.load("Images/egg.png")
        self.egg_img=pygame.transform.scale(self.egg_img,(40,40))

        # loads the hen image
        self.hen_img=pygame.image.load("Images/hen.png")
        self.hen_img=pygame.transform.scale(self.hen_img,(50,50))

        # loads the score image
        self.score_img=pygame.image.load("Images/score.png")
        self.score_img=pygame.transform.scale(self.score_img,(130,50))

        # loads the life image
        self.life_img=pygame.image.load("Images/life.png")
        self.life_img=pygame.transform.scale(self.life_img,(40,40))

    def set_live(self):
        if self.life==3:
             self.screen_placer(self.life_img,820,4)
             self.screen_placer(self.life_img,770,4)
             self.screen_placer(self.life_img,720,4)

        elif self.life==2:
            self.screen_placer(self.life_img,820,4)
            self.screen_placer(self.life_img,770,4)

        elif self.life==1:
            self.screen_placer(self.life_img,820,4)




if __name__=="__main__":
    c=Game()