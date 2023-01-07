from tkinter import *
root = Tk()
root.title("Plate Data smpl 1.0")
e1= Entry(root)

def validateUser():
    
    if e1.get() == "yohan":
         Label(root, text="Welcome "+e1.get()).grid(row=3,column=0)
    else:
        Label(root, text="Sorry Access denied").grid(row=3,column=0)

Label(root, text="Login", padx="20",pady="20").grid(row=0,column=1,columnspan=3, )
Label(root, text="Name").grid(row=1,column=0)
e1.grid(row=1,column=1)
Button(root, text="Login", command=validateUser).grid(row=2,column=1)


root.mainloop()
