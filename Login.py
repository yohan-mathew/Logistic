from tkinter import *
import time
import sys
 
root = Tk()
root.title("Plate Data smpl 1.0")
root.geometry("400x150")

frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)

e1= Entry(frame2,width=50)

def validateUser():
    
     if e1.get() == "yohan":
          Label(root, text="Welcome "+e1.get()).pack()
          root.update()
     else:
         rsltLbl = Label(root, text="Sorry Access denied")
         rsltLbl.pack()
         root.update()
         time.sleep(2)
         sys.exit()
         

frame1.pack(padx=10,pady=10)
Label(frame1, text="Login",).pack()
frame2.pack(padx=10,pady=5)
Label(frame2, text="Name:").pack(side=LEFT)
e1.pack()
frame3.pack(padx=10,pady=1)
Button(frame3, text="Login", command=validateUser).pack()


root.mainloop()
