from tkinter import *
from PIL import Image,ImageTk

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.height=700
        self.width=450
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False,False)
        
        self.title("Egg Catcher")
        self.iconbitmap("Images/icon.ico")
        self._load_image()
        self.__gui__()

    def __gui__(self):
        Label(self,image=self.img1).place(x=0,y=0)
        Button(image=self.img2,background="#c7fad6",relief="flat",activebackground="#c7fad6").place(x=200,y=360)


    def _load_image(self):
        self.img1=Image.open("Images/gui_img.jpg").resize((self.width,self.height))
        self.img1=ImageTk.PhotoImage(image=self.img1)

        # loads the play button
        self.img2=Image.open("Images/play.png").resize((70,70))
        self.img2=ImageTk.PhotoImage(image=self.img2)


if __name__=="__main__":
    c=GUI()
    c.mainloop()