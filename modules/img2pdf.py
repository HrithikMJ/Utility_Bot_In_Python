"""""
code by Dharun C & Hrithik Joseph
Title: Image to PDF converter using PYTHON IMAGING LIBRARY
Github:https://github.com/HrithikMJ/Image2PDF
"""""
from PIL import Image  # for pdf conversion
import sys  # used in exit function
import tkinter as tk  # GUI
from tkinter import filedialog  # GUI
from tkinter import messagebox  # GUI
from time import sleep
import webbrowser as wb

def process_images():  # the pdf conversion function
    images = []
    try:
      num = int(d.get())
      d.delete(0,"end")
      messagebox.showinfo('HINT', "only open img iles such as {'.png','.jpg','.jpeg','.bmp'} etc ", icon='info')
      for i in range(1,num+1):
              got_file=False
              fname = filedialog.askopenfilename()
              try:
                 im = Image.open(fname)
                 if im.mode == "RGBA":  # pdf cant read RGBA files
                     im = im.convert("RGB")
                 images.append(im)
                 got_file=True

              except:
                  messagebox.showinfo('ERROR!', "cannot identify image file ", icon='error')
                  break

      if got_file:
          imag = filedialog.asksaveasfilename(defaultextension='.pdf')

      elif not got_file:
            messagebox.showinfo('ERROR!', "One or more images aren't imported succesfully ", icon='error')

      try:
          if num != 1:
              im.save(imag, save_all=True, quality=100, append_images=images[:-1])
          else:
              im.save(imag, quality=100)
      except :
          messagebox.showinfo('ERROR!', "The process was closed without saving", icon='error')

    except ValueError:
        messagebox.showerror('ERROR!', "invalid literal for int() with base 10", icon='error')
        d.delete(0,"end")


def openwb():#to open links
    wb.open("https://github.com/HrithikMJ/Image2PDF")


def Exit():  # exit function
    msgBox = messagebox.askquestion(
        'Exit Application', 'Are you sure wanted to exit', icon='warning')
    if msgBox == 'yes':
        sys.exit()

def main_f():
# main_function
    print("""\033[1;31m"""+""" _____  ____    ____   ______    _____   _______  ______   ________
    |_   _||_   \  /   _|.' ___  |  / ___ `.|_   __ \|_   _ `.|_   __  |
      | |    |   \/   | / .'   \_| |_/___) |  | |__) | | | `. \ | |_ \_|
      | |    | |\  /| | | |   ____  .'____.'  |  ___/  | |  | | |  _|
     _| |_  _| |_\/_| |_\ `.___]  |/ /_____  _| |_    _| |_.' /_| |_
    |_____||_____||_____|`._____.' |_______||_____|  |______.'|_____|

                                                                             -DHARUN C & HRITHIK JOSEPH """+"""\033[0;0m""")


    print("\n\n\n\nhttps://github.com/HrithikMJ/Image2PDF")
    sleep(1.2)
    top = tk.Tk()
    top.wm_title("IMG2PDF")
    img1 = tk.PhotoImage(file="images/icon.png")
    top.iconphoto(False, img1)
    img = tk.PhotoImage(file="images/Logo.png")#logo
    top.geometry("400x250")  # screen_size
    s = tk.Label(top, image=img,bd=10).place(x=100, y=0)  # Label
    label = tk.Label(top, text="Enter no:of images:",bd=5).place(x=50, y=100)#Label
    d = tk.Entry(top, width=10,bd=5)#Entry box
    d.place(x=190, y=100)
    a = tk.Button(top, text="Start",width=7, fg='Green',command=process_images,bd=3).place(x=300, y=98)  # button1
    w = tk.Button(top, text="Exit!", fg='Red',width=10,command=Exit, bd=5).place(x=100, y=180)  # button2
    kp= tk.Button(top, text="GitHub</>",fg='Black',width=10,bd=5,command=openwb).place(x=250,y=180)
    top.mainloop()
