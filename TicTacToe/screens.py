import tkinter as tk 
from constants import style

class Home(tk.Frame):
    
    def _init_(self, parent, controller):
        super()._init_(parent)
        self.configure(background = style.BACKGROUND)
        self.controller = controller  #Instancia del manager
        
        

class Game(tk.Frame):
    
    def _init_(self, parent, controller):
        super()._init_(parent)
        self.configure(background = style.BACKGROUND)
        self.controller = controller  #Instancia del manager
        