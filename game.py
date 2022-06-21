import sys
import threading
import pygame
from pygame.locals import *
import random
import configparser

class Game:
    def __init__(self,music):
        self.music=music
        pygame.init()
        pygame.mixer.init()

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
        self.vy=6
        self.text=pygame.font.SysFont("papyrus",50,True)
        self.text1=pygame.font.SysFont("papyrus",90,True)
        self.text2=pygame.font.SysFont("forte",40)
        self.crack=False
        self.coord=[]
        self.game_over=False
        self.high_score=0
        self.conti=False
        self.pause=False
        self.g_count=0

        self.hen_no=random.randint(1,5)
        # self.hen_no=5

        self.window=pygame.display.set_mode((self.screen_width,self.screen_height))
        self.icon_img=pygame.image.load("Images/g_icon.png")
        pygame.display.set_icon(self.icon_img)
        pygame.display.set_caption("Egg Catcher Game BY Prathamesh Dhande")
        self.clock=pygame.time.Clock()
        self.play_bgmusic()
        self.__load_image()
        

    def screen_placer(self,img,x,y):
        self.window.blit(img,(x,y))

    def __gameloop__(self):
        while not self.exit_game:
            self.clock.tick(40)
            self.get_highscore()
           
            if self.game_over:
                if self.g_count==0:
                    self.play_gameover_sound()
                    self.g_count=1
                if int(self.high_score)<=self.score:
                    self.window.fill((21, 254, 12))
                    self.screen_placer(self.highscore_img,150,50)
                    self.highscore_text=self.text1.render(str(self.high_score),True,(0,0,0))
                    self.screen_placer(self.highscore_text,420,400)
                    self.info_text=self.text.render("Press Enter to Continue",True,(0,0,0))
                    self.screen_placer(self.info_text,150,580)
                
                elif int(self.high_score)>self.score:
                    self.game_over_screen()
                
                for self.event in pygame.event.get():
                    if self.event.type==pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    
                    if self.event.type==pygame.KEYDOWN:
                        if self.event.key==pygame.K_RETURN:
                            self.conti=True
                            self.game_over=False

                        if self.event.key==pygame.K_1:
                            self.conti=False
                            self.game_over=False
                            c=Game(self.music)
                            c.__gameloop__()

                                
                        if self.event.key==pygame.K_2:
                            self.game_over=True
                            pygame.quit()
                            import gui
                            g=gui.GUI()
                            g.__gui__()
                                
                        if self.event.key==pygame.K_3:
                            pygame.quit()
                            sys.exit()

                        
            elif self.conti:
                self.game_over_screen()
                for self.event in pygame.event.get():
                    if self.event.type==pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    
                    if self.event.type==pygame.KEYDOWN:
                        if self.event.key==pygame.K_1:
                            self.conti=False
                            self.game_over=False
                            c=Game(self.music)
                            c.__gameloop__()

                                
                        if self.event.key==pygame.K_2:
                            self.game_over=True
                            pygame.quit()
                            import gui
                            g=gui.GUI()
                            g.__gui__()
                                
                        if self.event.key==pygame.K_3:
                            pygame.quit()
                            sys.exit()


            else:
            
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

                    elif self.event.type==pygame.KEYDOWN:
                        if self.event.key==pygame.K_SPACE:
                            self.vy=0
                            self.pause=True
                        if self.event.key==pygame.K_RETURN:
                            self.vy=6
                            self.pause=False

                self.key_pressed=pygame.key.get_pressed()
                if self.key_pressed[K_LEFT]:
                    self.basket_x+=-10
                    
                elif self.key_pressed[K_RIGHT]:
                    self.basket_x+=10

                self.pause_screen()

                # if the basket gets behind the walls so this is set
                if self.basket_x<0:
                    self.basket_x=0
                elif self.basket_x>818:
                    self.basket_x=818
                self.check_collison()

                self.set_cracked_get()
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
        self.basket_img=pygame.transform.scale(self.basket_img,(100,80))

        # loads the egg_cracked image
        self.eggcracked_img=pygame.image.load("Images/egg_cracked.png")
        self.eggcracked_img=pygame.transform.scale(self.eggcracked_img,(120,100))

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

        # loads the gameover image
        self.gameover_img=pygame.image.load("Images/game_over.jpeg")
        self.gameover_img=pygame.transform.scale(self.gameover_img,(600,400))

        # loads the highscore image
        self.highscore_img=pygame.image.load("Images/highscore.jpeg")
        self.highscore_img=pygame.transform.scale(self.highscore_img,(600,400))



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
        
        elif self.life==0:
            self.game_over=True

    def set_hens(self):
        if self.life==0:
            self.game_over=True
        else:
                
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
        self.egg_rect=pygame.Rect(self.egg_x,self.egg_y,45,60)
        self.basket_rect=pygame.Rect(self.basket_x+30,self.basket_y+40,50,70)
        if self.egg_y>self.screen_height-70:
            self.play_cracked_sound()
            self.crack=True
            self.coord.insert(0,self.egg_x)
            self.coord.insert(1,self.egg_y)
            del self.coord[2:]
            self.count=0
            self.hen_no=random.randint(1,5)
            self.life-=1
            
        elif self.egg_rect.colliderect(self.basket_rect):
            self.play_catched_sound()
            self.crack=False
            self.score+=1
            self.hen_no=random.randint(1,5)
            self.count=0
            self.egg_y=700
        
    def set_cracked_get(self):
        if self.crack:
            self.screen_placer(self.eggcracked_img,self.coord[0],self.coord[1]-20)

    def get_highscore(self):
        config=configparser.ConfigParser()
        config.read("config.ini")
        self.high_score=config['score']['highscore']
        if int(self.high_score)<self.score:
            self.high_score=self.score
            with open("config.ini","w") as f:
                f.write(f"[score]\nhighscore={self.high_score}")

    def game_over_screen(self):
        self.window.fill((0,0,0))
        self.screen_placer(self.gameover_img,150,50)
        self.txt1=self.text2.render("Press 1 to Play Again",True,(255,255,255))
        self.txt2=self.text2.render("Press 2 for Main Menu",True,(255,255,255))
        self.txt3=self.text2.render("Press 3 to Exit",True,(255,255,255))
        self.screen_placer(self.txt1,275,400)
        self.screen_placer(self.txt2,275,450)
        self.screen_placer(self.txt3,275,500)

    def pause_screen(self):
        if self.pause:
            self.paused_text=self.text1.render("Paused",True,(0,0,0))
            self.retun=self.text2.render("Press Enter To Play Game",True,(0,0,0))
            self.screen_placer(self.paused_text,250,300)
            self.screen_placer(self.retun,200,420)
            
        else:
            self.vy=6
            self.pause=False

    def play_bgmusic(self):
        
        if self.music:
            pygame.mixer.music.stop()
        else:
            pygame.mixer.music.load("Sounds/bgsound.mp3")
            pygame.mixer.music.play(-1)

    def play_cracked_sound(self):
        self.cracked_sound=pygame.mixer.Sound("Sounds/egg_cracked.mp3")
        if self.music:
            self.cracked_sound.stop()
        else:
            self.cracked_sound.play(0)

    def play_gameover_sound(self):
        if self.music:
            pygame.mixer.music.stop()
        else:
            pygame.mixer.music.load("Sounds/game_over.wav")
            pygame.mixer.music.play(1)

    def play_catched_sound(self):
        self.catched_sound=pygame.mixer.Sound("Sounds/egg_catched.wav")
        if self.music:
            self.catched_sound.stop()
        else:
            self.catched_sound.play(0)
            
        



if __name__=="__main__":
    c=Game(False)
    c.__gameloop__()