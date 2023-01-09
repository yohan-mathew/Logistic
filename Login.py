from tkinter import *
import time
import sys
import customtkinter as custom

#created the Stage 
root = custom.CTk()
root.title("Plate Data smpl 1.0")
root.geometry("400x300")
root.columnconfigure(0, weight=1)
root.rowconfigure(1,weight=1)
root.rowconfigure(2,weight=1)


#created all the frame(contains respective components)
     #first page frames
frame1 = custom.CTkFrame(root,height=50)
frame2 = custom.CTkFrame(root,fg_color='transparent')
frame3 = custom.CTkFrame(root)


#second page frames
frame4 = custom.CTkFrame(root)

#username
usernametxt= custom.CTkEntry(frame2,width=100)

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
     helv36 = custom.CTkFont(family="Helvetica",size=20,weight="bold")
     if usernametxt.get() == "yohan":
          custom.CTkLabel(root, text="Welcome " + usernametxt.get()).pack()
          eraseContent(frame1,frame2,frame3)
          root.update()
          captureDetails()
     else:
          eraseContent(frame1,frame2,frame3)
          rsltLbl = custom.CTkLabel(root, text="Access denied",text_color='red',font=helv36)
          rsltLbl.grid(row=1,column=0)
          root.update()
          time.sleep(2)
          sys.exit()
# ---------------------------------------------------------------------------------------------
         
frame1.grid(row=0,column=0,sticky='ew')
custom.CTkLabel(frame1, text="Login",).place(relx=0.5, rely=0.5, anchor='center')

frame2.grid(row=1,column=0,pady=10,sticky='ew')
frame2.columnconfigure(0,weight=1)
frame2.columnconfigure(1,weight=1)
custom.CTkLabel(frame2, text="Name:").grid(row=0,column=0,sticky='e',ipadx=10)
usernametxt.grid(row=0,column=1,sticky='w')

frame3.grid(row=2,column=0,sticky='n')
# frame3.pack(padx=10,pady=1)
custom.CTkButton(frame3, text="Login", command=validateUser).grid(row=0,column=0)


root.mainloop()
