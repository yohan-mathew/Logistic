from tkinter import *
import time
import sys
import customtkinter as custom

#created the Stage 
root = custom.CTk()
root.title("Plate Data smpl 1.0")
root.geometry("400x150")


#created all the frame(contains respective components)
     #first page frames
frame1 = custom.CTkFrame(root)
frame2 = custom.CTkFrame(root)
frame3 = custom.CTkFrame(root)


#second page frames
frame4 = custom.CTkFrame(root)

#username
usernametxt= custom.CTkEntry(frame2,width=50)

# ---------------------------------------------------------------------------------------------
#                                 **functions made to use everywhere**

#removes any given frames from the stage so I can reuse the space
def eraseContent(*frames):
     for x in frames:
          x.destroy()
# ---------------------------------------------------------------------------------------------
#                                 **functions made to use on frames**

# Step2: after validation, get the details     
def captureDetails():
     frame4.pack()
     plateNotxt = custom.CTkEntry(frame4)
     plateWeighttxt = custom.CTkEntry(frame4)
     plateNolbl = custom.CTkLabel(frame4,text="Plate Number: ")
     plateWeightlbl = custom.CTkLabel(frame4,text="Plate Weight: ")
     
     plateNolbl.pack()
     plateNotxt.pack()
     
     plateWeightlbl.pack()
     plateWeighttxt.pack()
# ---------------------------------------------------------------------------------------------

# Step1: get username & validate user(IF user is in system, go to step 2, ELSE error & exit!)     
def validateUser():
     if usernametxt.get() == "yohan":
          custom.CTkLabel(root, text="Welcome " + usernametxt.get()).pack()
          eraseContent(frame1,frame2,frame3)
          root.update()
          captureDetails()
     else:
          eraseContent(frame1,frame2,frame3)
          rsltLbl = custom.CTkLabel(root, text="Sorry Access denied")
          rsltLbl.pack()
          root.update()
          time.sleep(2)
          sys.exit()
# ---------------------------------------------------------------------------------------------
         
# labels & frames for screen one 
frame1.pack(padx=10,pady=10)
custom.CTkLabel(frame1, text="Login",).pack()
frame2.pack(padx=10,pady=5)
custom.CTkLabel(frame2, text="Name:").pack(side=LEFT)
usernametxt.pack()
frame3.pack(padx=10,pady=1)
custom.CTkButton(frame3, text="Login", command=validateUser).pack()


root.mainloop()
