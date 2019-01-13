from tkinter import *
from threading import Thread
import Main, Settings, MainTesseract


class Launcher:
    def __init__(self):
        self.pencere = Tk()

        self.pencere.title("Başlatıcı")
        self.pencere.geometry("400x215+700+300")
        self.pencere.resizable(0,0)
    
        self.baslatButon = Button(self.pencere, text = "Başlat", height = 4,relief = SOLID,borderwidth = 1, font = ("Arial Sans-Serif", 12), command = self.Baslat)
        self.seceneklerButon = Button(self.pencere, text = "Seçenekler", height = 5, relief = SOLID, borderwidth = 1, font = ("Arial Sans-Serif", 12), command = Settings.Settings)
        self.baslatButon.pack(fill = "both")
        self.seceneklerButon.pack(fill = "both")

    def Baslat(self):
        try:
            dosya = open("settings.txt","r")
            veri = dosya.readline().rstrip("\n")
            dosya.close()
        except:
            veri = 1
            
        veri = str(veri)
        if veri == "1":
            self.pencere.destroy()
            Main.MainScreen()
        else:
            self.pencere.destroy()
            MainTesseract.MainScreen()
Launcher()

