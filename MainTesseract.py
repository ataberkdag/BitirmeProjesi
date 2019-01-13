from tkinter import *
from PIL import Image, ImageTk
import cv2, os, pytesseract

class MainScreen:
    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
        width, height = 800, 600
        self.video = cv2.VideoCapture(0)
        self.video.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

        self.pencere = Tk()
        self.pencere.geometry("640x520+700+200")
        self.pencere.title("Tesseract")
        self.kamera = Label(self.pencere)
        self.show_frame()
        self.kamera.pack()
        self.buton = Button(self.pencere, text = "Kontrol Et", command = self.takeSnap)
        self.buton.pack(fill = "both")

    def show_frame(self):
        bos, frame = self.video.read()

        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image = img)
        self.kamera.imgth = imgtk
        self.kamera.configure(image = imgtk)
        self.kamera.after(10, self.show_frame)

    def takeSnap(self):
        yol = os.getcwd()
        p = os.path.join(yol, "kontrol.jpg")
        ret, frame = self.video.read()
        picture = cv2.imwrite(p, frame)
        print(pytesseract.image_to_string(cv2.imread(p)))
