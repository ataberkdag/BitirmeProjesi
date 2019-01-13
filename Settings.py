from tkinter import *
veri = 0
try:
    settingsFile = open("settings.txt", "r")
    veri = settingsFile.readline().rstrip("\n")
    settingsFile.close()
except:
    settingsFile = open("settings.txt", "w")
    settingsFile.write("1\n0")
    settingsFile.close()
    veri = 1

veri = str(veri)
class Settings:
    def __init__(self):
        self.pencere = Tk()
        self.pencere.title("Seçenekler")
        self.pencere.geometry("400x125+700+300")
        self.pencere.resizable(0,0)
        
        self.yeni = veri
        Frame1 = Frame(self.pencere, pady = 10, padx = 5)
        Frame2 = Frame(self.pencere, pady = 10, padx = 5)

        Label1 = Label(self.pencere, text = "Görseli okumada hangi yöntem tercih edilsin?")
        Label1.pack()

        self.tesButton = Button(Frame1, text = "Tesseract", width = 20, command = self.islem2)
        self.makButton = Button(Frame1, text = "Makine Öğrenmesi", width = 20, command = self.islem1)
        self.makButton.pack(side = "left")
        self.tesButton.pack(side = "left")

        if veri == "1":
            self.makButton["bg"] = "yellow"
            self.tesButton["bg"] = "white"
        else:
            self.tesButton["bg"] = "yellow"
            self.makButton["bg"] = "white"
        Frame1.pack()

        kaydetB = Button(self.pencere, text = "Kaydet", command = self.kaydet, width = 20, height = 2)
        kaydetB.pack()
    def islem1(self):
        self.yeni = "1"
        self.makButton["bg"] = "yellow"
        self.tesButton["bg"] = "white"
    def islem2(self):
        self.yeni = "2"
        self.makButton["bg"] = "white"
        self.tesButton["bg"] = "yellow"
    def kaydet(self):
        dosya = open("settings.txt","w")
        dosya.write(self.yeni)
        dosya.close()
        self.pencere.destroy()
