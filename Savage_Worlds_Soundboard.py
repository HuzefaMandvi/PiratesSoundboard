import winsound
import tkinter as tk

root = tk.Tk()
ocean_img = tk.PhotoImage(file = 'ocean.gif')
tavern_img = tk.PhotoImage(file = 'tavern.gif')
battle_img = tk.PhotoImage(file = 'battle.gif')
shanty_img = tk.PhotoImage(file = 'shanty.gif')
flag_img = tk.PhotoImage(file = 'flag.gif')

# class for the main window
class Soundboard(tk.Frame):

    Home = tk.Label()

    def __init__ (self, master=None):
        tk.Frame.__init__(self,master)
        self.grid()
        self.createWidgets()
#initialize all widgets
    def createWidgets(self):
        self.Head = tk.Label(self, text="Pirates of the Spanish Main Soundboard").grid(row=0, column=1, sticky = 'W'+'E')
        self.Home = tk.Label(self, image = flag_img)
        self.Home.grid(row=1, column=1, sticky = 'W')
        self.OceanButton = tk.Button(self, text = 'Ocean', command = self.startOcean).grid(row=2, column = 0)
        self.TavernButton = tk.Button(self, text = 'Tavern', command = self.startTavern).grid(row = 2, column = 1)
        self.SeaFightButton = tk.Button(self, text = 'Sea Fight', command = self.startSeaFight).grid(row = 2, column = 3)
        self.ShantyButton = tk.Button(self, text = 'Pirate Shanty', command = self.startShanty).grid(row = 2, column = 4)
        self.StopButton = tk.Button(self, text = 'Stop Sound', command = self.stopSound).grid(row = 2, column = 5)

#starts ocean sound, changes image to ocean
    def startOcean(self):
        self.Home.configure(image = ocean_img)
        winsound.PlaySound('Ocean',winsound.SND_ASYNC)
#starts ambient tavern sound, changes image to tavern
    def startTavern(self):
        self.Home.configure(image = tavern_img)
        winsound.PlaySound('Tavern',winsound.SND_ASYNC)
#starts sea fight sound, changes image to sea fight
    def startSeaFight(self):
        self.Home.configure(image = battle_img)
        winsound.PlaySound('Battle',winsound.SND_ASYNC)

    def startShanty(self):
        self.Home.configure(image = shanty_img)
        winsound.PlaySound('Shanty',winsound.SND_ASYNC)
#stops sound, changes back to flag
    def stopSound(self):
        self.Home.configure(image = flag_img)
        winsound.PlaySound(None,winsound.SND_ASYNC)

#make the actual soundboard 
soundboard = Soundboard(root)

#cute little pirate flag icon
root.iconbitmap('icon.ico')

#open soundboard
root.mainloop()
