from tkinter import *
from PIL import Image, ImageTk
import cv2, os, Control

class MainScreen:
    def __init__(self):
        width, height = 800, 600
        self.video = cv2.VideoCapture(0)
        self.video.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

        self.pencere = Tk()
        self.pencere.geometry("640x550+700+200")
        self.pencere.resizable(0, 0)
        self.pencere.title("Makine Öğrenmesi")
        self.kamera = Label(self.pencere)
        self.KameraGörüntüle()
        self.kamera.pack()
        self.buton = Button(self.pencere, text = "Kontrol Et",
                            command = self.EkranGörüntüsü)
        self.buton.pack(fill = "both")
        self.sonuc = Label(self.pencere, text = "Sonuç: ")
        self.sonuc.pack()

    def KameraGörüntüle(self):
        bos, görüntü = self.video.read()
        cv2görüntü = cv2.cvtColor(görüntü, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2görüntü)
        imgtk = ImageTk.PhotoImage(image = img)
        self.kamera.imgtk = imgtk
        self.kamera.configure(image = imgtk)
        self.kamera.after(10, self.KameraGörüntüle)

    def EkranGörüntüsü(self):
        yol = os.getcwd()
        bos, frame = self.video.read()
        yol = os.path.join(yol, "kontrol.jpg")
        resim = cv2.imwrite(yol, frame)
        sonuc = Control.main()
        self.sonuc['text'] = "Sonuç: " + str(sonuc)


