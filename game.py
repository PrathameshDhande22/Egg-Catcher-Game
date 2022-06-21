import sys
import pygame

class Game:
    def __init__(self):
        pygame.init()

        # game variables
        self.screen_height=700
        self.screen_width=900
        self.exit_game=False
        self.life=3
        self.score=0

        self.window=pygame.display.set_mode((self.screen_width,self.screen_height))
        self.icon_img=pygame.image.load("Images/g_icon.png")
        pygame.display.set_icon(self.icon_img)
        pygame.display.set_caption("Egg Catcher Game BY Prathamesh Dhande")
        self.__load_image()
        self.__gameloop__()

    def screen_placer(self,img,x,y):
        self.window.blit(img,(x,y))

    def __gameloop__(self):
        while not self.exit_game:
            for self.event in pygame.event.get():
                if self.event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def __load_image(self):
        # loads the background image
        self.back_img=pygame.image.load("Images/back_img.jpeg")
        self.back_img=pygame.transform.scale(self.back_img,(self.screen_width,self.screen_height-100))

        # loads the bar image
        self.bar_img=pygame.image.load("Images/bar.png")
        self.bar_img=pygame.transform.scale(self.bar_img,(self.screen_width,100))

        # loads the basket image
        self.basket_img=pygame.image.load("Images/basket.png")
        self.basket_img=pygame.transform.scale(self.basket_img,(40,40))

        # loads the egg_cracked image
        self.eggcracked_img=pygame.image.load("Images/egg_cracked.png")
        self.eggcracked_img=pygame.transform.scale(self.eggcracked_img,(60,60))

        # loads the egg image
        self.egg_img=pygame.image.load("Images/egg.png")
        self.egg_img=pygame.transform.scale(self.egg_img,(40,40))

        # loads the hen image
        self.hen_img=pygame.image.load("Images/hen.png")
        self.hen_img=pygame.transform.scale(self.hen_img,(50,50))


if __name__=="__main__":
    c=Game()