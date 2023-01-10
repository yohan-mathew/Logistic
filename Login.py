from tkinter import Tk
import time
import sys
import customtkinter as custom



class CreateTop(custom.CTkFrame):   
     def __init__(self,container):
          super().__init__(container,height=50)
          
          self.columnconfigure(0,weight= 1)
       
          self.__createSubWidgets()
     
     def __createSubWidgets(self):
          lbl_heading = custom.CTkLabel(self, text= "login", text_color='white')
          lbl_heading.place(relx=0.5, rely=0.5, anchor='center')

class CreateBottom(custom.CTkFrame):
     def __init__(self,container):
          super().__init__(container,fg_color='transparent')
          
          self.columnconfigure(0,weight= 1)
          
          self.entryData = custom.StringVar()
          
          self.__createSubWidgets()
          
     def __createSubWidgets(self):
          lbl_Name = custom.CTkLabel(self,text="Name: ")
          lbl_Name.grid(row=0,column=0,padx=10,pady=10)
          
          txt_Name = custom.CTkEntry(self, width = 150, corner_radius=10, textvariable=self.entryData)
          txt_Name.grid(row=0,column=1,padx=10,pady=10)
          
          btn_Login = custom.CTkButton(self,width= 200,command=self.validateUser)
          btn_Login.grid(row=1,column=0,columnspan=2,pady=10)
          
     def validateUser(self):
               helv36 = custom.CTkFont(family="Helvetica",size=20,weight="bold")
               if self.entryData.get() == "yohan":
                      for widget in self.winfo_children():
                           widget.destroy()
                      print(app.winfo_children()[0].winfo_children()[0].configure(text="Welcome Yohan"))
                      self.captureDetails()
               else:
                      for widget in self.winfo_children():
                           widget.destroy()
                      rsltLbl = custom.CTkLabel(self, text="Access denied",text_color='red',font=helv36)
                      rsltLbl.grid(row=0,column=0)
                      self.update()
                      time.sleep(2)
                      sys.exit()     

     def captureDetails(self):
          
          self.columnconfigure(1,weight= 1)
          
          plateNotxt = custom.CTkEntry(self)
          plateWeighttxt = custom.CTkEntry(self)
          plateNolbl = custom.CTkLabel(self,text="Plate Number: ")
          plateWeightlbl = custom.CTkLabel(self,text="Plate Weight: ")
          
          plateNolbl.grid(row=0,column=0)
          plateNotxt.grid(row=0,column=1)
          
          plateWeightlbl.grid(row=1,column=0)
          plateWeighttxt.grid(row=1,column=1)
              
class App(custom.CTk):
     def __init__(self):
          super().__init__()
          self.title("Plate Data smpl 1.0")
          self.geometry("400x300")
          self.columnconfigure(0,weight=1)
          
          self.__createSubWidgets()
        
     def __createSubWidgets(self):
          frame_Top = CreateTop(self)
          frame_Top.grid(row=0,column=0,sticky='ew')
          
          frame_Bottom = CreateBottom(self)
          frame_Bottom.place(relx=0.5,rely=0.5, anchor='center')
          
if __name__ == "__main__":
     app = App()     
     app.mainloop()
     
# # Step2: after validation, get the details     
# def captureDetails():
#      frame4.pack()
#      plateNotxt = custom.CTkEntry(frame4)
#      plateWeighttxt = custom.CTkEntry(frame4)
#      plateNolbl = custom.CTkLabel(frame4,text="Plate Number: ")
#      plateWeightlbl = custom.CTkLabel(frame4,text="Plate Weight: ")
     
#      plateNolbl.pack()
#      plateNotxt.pack()
     
#      plateWeightlbl.pack()
#      plateWeighttxt.pack()
# # ---------------------------------------------------------------------------------------------
