from tkinter import *
from PIL import Image,ImageTk
import pygame
import game
import pygame.mixer

class GUI(Tk):
    def __init__(self):
        super().__init__()
        pygame.mixer.init()
        self.height=700
        self.width=450
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False,False)
        
        self.title("Egg Catcher")
        self.iconbitmap("Images/icon.ico")
        self.count=0
        self.music=False
        self.play_music()
        self._load_image()
        

    def __gui__(self):
        Label(self,image=self.img1).place(x=0,y=0)
        Button(image=self.img2,background="#c7fad6",relief="flat",activebackground="#c7fad6",command=self.play).place(x=190,y=360)
        Button(image=self.img3,background="#c3fada",relief="flat",activebackground="#c3fada",command=self.destroy).place(x=100,y=360)
        Button(image=self.img4,background="#c0f9dc",relief="flat",activebackground="#c0f9dc",command=self.instruction).place(x=320,y=360)
        self.soundB=Button(image=self.img6,background="#fdfcc2",relief="flat",activebackground="#fdfcc2",command=self.set_sound)
        self.soundB.place(x=210,y=470)


    def _load_image(self):
        self.img1=Image.open("Images/gui_img.jpg").resize((self.width,self.height))
        self.img1=ImageTk.PhotoImage(image=self.img1)

        # loads the play button
        self.img2=Image.open("Images/play.png").resize((90,90))
        self.img2=ImageTk.PhotoImage(image=self.img2)

        # loads the exit button
        self.img3=Image.open("Images/exit.png").resize((50,50))
        self.img3=ImageTk.PhotoImage(image=self.img3)

        # loads the instruction button
        self.img4=Image.open("Images/inst.png").resize((50,50))
        self.img4=ImageTk.PhotoImage(image=self.img4)

        # loads the sound off button
        self.img5=Image.open("Images/sound_off.png").resize((50,50))
        self.img5=ImageTk.PhotoImage(image=self.img5)

        # loads the sound on button
        self.img6=Image.open("Images/sound_on.png").resize((50,50))
        self.img6=ImageTk.PhotoImage(image=self.img6)

        # loads the letter image
        self.img7=Image.open("Images/letter.png").resize((self.width,self.height+50))
        self.img7=ImageTk.PhotoImage(image=self.img7)

        # loads the back image
        self.img8=Image.open("Images/back.png").resize((40,40))
        self.img8=ImageTk.PhotoImage(image=self.img8)

    def set_sound(self):
        if self.count==0:
            self.soundB.config(image=self.img5)
            self.music=True
            self.play_music()
            self.count=1
        elif self.count==1:
            self.soundB.config(image=self.img6)
            self.music=False
            self.play_music()
           
            self.count=0
        
    def play(self):
        try:
            self.destroy()
            c=game.Game(self.music)
            c.__gameloop__()
        except pygame.error:
            pass

    def play_music(self):
        if self.music:
            pygame.mixer.music.stop()
        else:
            pygame.mixer.music.load("Sounds/bgsound.mp3")
            pygame.mixer.music.play(-1)

    def instruction(self):
        self.inst_frame=Frame(self,width=self.width,height=self.height+30)
        self.inst_frame.place(x=0,y=0)
        Label(self.inst_frame,image=self.img7).place(x=0,y=0)
        Button(self.inst_frame,image=self.img8,background="#b99052",activebackground="#b99052",relief="flat",command=lambda : self.inst_frame.place_forget()).place(x=10,y=10)
        text='''My name is prathames\nInstruction'''
        Label(self.inst_frame,text="INSTRUCTION",background="#d7b97e",font=("Times new roman",20)).place(x=130,y=70)
        with open("instruction.txt","r") as f:
            data=f.read()
        Label(self.inst_frame,text=data,background="#d7b97e",font=("Times new roman",13),justify="left").place(x=74,y=127)
        

       
 

        
            




if __name__=="__main__":
    c=GUI()
    c.__gui__()
    c.mainloop()