import tkinter as tk
from tkinter import filedialog, Text
from PIL import ImageTk,Image
import os


class GerarahereWindow:
    def __init__(self, root):

        self.canvas =  tk.Canvas(root, height=700, width=700, bg="#4e528a")
        self.canvas.create_text(350,150,fill="#b9cf3c",font="Times 20 italic bold",
                                text="Hey mate, are you up for no good?")
        self.canvas.pack()

        yesButton = tk.Button(root, text="I'm up to no good!", font="Times 14 italic bold", fg="#b9cf3c", bg="#524d4a",
        activeforeground="#b9cf3c", activebackground="#3d3937",anchor = "w", command = self.badChoice)
        yesButton.pack()

        noButton = tk.Button(root, text="I'll pass on that!", font="Times 14 italic bold",  fg="#b9cf3c", bg="#524d4a", 
        activeforeground="#b9cf3c", activebackground="#3d3937",anchor = "w", command = self.goodChoice)
        noButton.pack()

        button1_window = self.canvas.create_window(340, 400, anchor="n", window=yesButton)
        button2_window = self.canvas.create_window(340, 470, anchor="n", window=noButton)

    def goodChoice(self):
        self.canvas.delete("all")
        img = Image.open("bellair1.png")
        self.canvas.create_text(350,60,fill="#b9cf3c",font="Times 20 italic bold",
                        text="Alrighty, move to bell air!")
        self.canvas.pack()
        self.canvas.image = ImageTk.PhotoImage(img)
        self.canvas.create_image(3,120, image = self.canvas.image, anchor='nw')
        okButton = tk.Button(root, text="I will! :)", font="Times 14 italic bold",  fg="#b9cf3c", bg="#524d4a", 
        activeforeground="#b9cf3c", activebackground="#3d3937",anchor = "w", command = self.canvas.quit)
        self.canvas.create_window(350, 600, anchor="n", window=okButton)
    #"gerarahere_for_real.mp3"
    def badChoice(self):
        self.canvas.delete("all")
        img = Image.open("gerarahere_nogood1.png")
        self.canvas.image = ImageTk.PhotoImage(img)
        self.canvas.create_image(3,50, image = self.canvas.image, anchor='nw')
        okButton = tk.Button(root, text="Ok :(", font="Times 14 italic bold",  fg="#b9cf3c", bg="#524d4a", 
        activeforeground="#b9cf3c", activebackground="#3d3937",anchor = "w", command = self.canvas.quit)
        self.canvas.create_window(350, 600, anchor="n", window=okButton)


root = tk.Tk()
g = GerarahereWindow(root)
root.mainloop()