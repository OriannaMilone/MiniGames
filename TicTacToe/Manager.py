#Screen manager
import tkinter as tk
from constants import style
from screens import Home, Game

class Manager(tk.Tk):
    
    def _init__(self, * args,  **kwargs):
        super()._init_(*args, **kwargs)
        self.title('TIC TAC TOE')
        
        container = tk.Frame(self)  #Parent (lienzo padre)
        container.pack(
           side = tk.TOP, 
           fill = tk.BOTH,
           expand = True
        )
        
        container.configure(background = style.BACKGROUND)
        container.grid_columnconfigure(0, weight = 1) #This makes a squre 1x1
        container.grid_rowconfigure(0, weight = 1)
        
        
        self.frames = {}
        for F in (Home, Game):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = tk.NSEW)
        self.show_frame(Home)
            
    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkrise() #Brings up the selected frame
        