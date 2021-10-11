import pyqrcode
import os
import tkinter as tk
from tkinter.messagebox import showerror
import cv2
import png


def make_qr():
    try:
        str_data = data.get()
        if str_data != '' and str_data != 'INSERT TEXT HERE':
            img = pyqrcode.create(str_data)
            #cv2.imshow(img, 'QR')
            img.png('img.png',scale=6)
            #img.save('img.png')
            data.delete(0, tk.END)
            os.startfile('img.png')

        else:
            showerror('Error! Please Enter Data')

    except Exception as e:
        print(e)            



root = tk.Tk()
root.title('QR Code Generator by CodeSavitar')
root.geometry('500x500')

#bg = tk.PhotoImage(file='image.png')
#bg_lab = tk.Label(root, image=bg, bg='white')
#bg_lab.place(x=0,y=0,relwidth=1,relheight=1)

data = tk.Entry(root, font=('Comic Sans MS', 18), bg='Black', fg='White')
data.place(x=0,y=240)

data.insert(tk.END, 'INSERT TEXT HERE')

button = tk.Button(root, text='Generate QR', font=('Comic Sans MS', 13), relief=tk.RAISED, command=make_qr)
button.place(x=90,y=300)

root.mainloop()