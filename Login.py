import sqlite3
from tkinter import Tk
import time
import sys
import customtkinter as custom
from datetime import datetime




class CreateTop(custom.CTkFrame):   
     def __init__(self,container):
          super().__init__(container,height=50)
          
          self.columnconfigure(0,weight= 1)
          
          self.__createSubWidgets()
     
     def __createSubWidgets(self):
          lbl_heading = custom.CTkLabel(self, text= "Login", font=subheadingFont)
          lbl_heading.place(relx=0.5, rely=0.5, anchor='center')

class CreateBottom(custom.CTkFrame):
     def __init__(self,container):
          super().__init__(container,fg_color='transparent')
          
          self.columnconfigure(0,weight= 1)
          self.productdetail =""
          self.entryData = custom.StringVar()
          
          self.__createSubWidgets()
          
     def __createSubWidgets(self):
          lbl_Name = custom.CTkLabel(self,text="Name: ",font=paragraphFont)
          lbl_Name.grid(row=0,column=0,padx=10,pady=10)
          
          txt_Name = custom.CTkEntry(self, width = 150, corner_radius=10, textvariable=self.entryData)
          txt_Name.grid(row=0,column=1,padx=10,pady=10)
          
          btn_Login = custom.CTkButton(self,width= 200,text="Login",command=self.__validateUser,font=paragraphFont)
          btn_Login.grid(row=1,column=0,columnspan=2,pady=10)
          
     def __validateUser(self):
               
               if self.entryData.get() == "yohan":
                      for widget in self.winfo_children():
                           widget.destroy()
                      app.winfo_children()[0].winfo_children()[0].configure(text="Welcome Yohan",font=subheadingFont)
                      self.optionScreen()
               else:
                      for widget in self.winfo_children():
                           widget.destroy()
                      rsltLbl = custom.CTkLabel(self, text="Access denied",text_color='red',font=headingFont)
                      rsltLbl.grid(row=0,column=0)
                      self.update()
                      time.sleep(2)
                      sys.exit()     
     
     def optionScreen(self):
          
          
          custom.CTkLabel(self,text="If your Barge just arrived",font=paragraphFont).grid(row=0,column=0)
          custom.CTkButton(self,width=100,text="Arrival",command=self.__captureDetailsArrival).grid(row=1,column=0,pady=(0,15))
          
          custom.CTkLabel(self,text="If your Barge is Leaving Now",font=paragraphFont).grid(row=2,column=0)
          custom.CTkButton(self,width=100,text="Departure",command=self.__findBarge).grid(row=3,column=0,pady=(0,15))
          
          custom.CTkLabel(self,text="If you want to remove a Previous Barge",font=paragraphFont).grid(row=4,column=0)
          custom.CTkButton(self,width=100,text="Remove Barge",command=self.__findBarge).grid(row=5,column=0,pady=(0,15))
          
          custom.CTkLabel(self,text="If you would like to see a Report",font=paragraphFont).grid(row=6,column=0)
          custom.CTkButton(self,width=100,text="Reports").grid(row=7,column=0,pady=(0,15))

     def __captureDetailsArrival(self):
          
          def errors():
                txt_BargeNo.configure(placeholder_text="REQUIRED",border_color='red')
          def clearError():
               txt_BargeNo.configure(placeholder_text='try "XAE234"',border_color= txt_BargeArrivalDate._border_color )
                
                
          def getTime():
               todayTime_date=datetime.now()
               day = todayTime_date.strftime("%D")
               time = todayTime_date.strftime("%I:%M")
               return day,time
          
          def __addToDb():
                #create a db
               conn = sqlite3.connect('barge_book.db')

               # create a cursor
               c = conn.cursor()
               
               # c.execute("DROP TABLE barges")
               
               
               try:
                    c.execute("""CREATE TABLE barges( 
                              
                                        source text, 
                                        bargeNo text, 
                                        bargeArrivalDate text, 
                                        bargeArrivalTime text, 
                                        productDetails text, 
                                        productWithLid integer, 
                                        bargeReleaseTime text, 
                                        bargeReleaseDate text, 
                                        comments blob, 
                                        PRIMARY KEY(bargeNo, bargeArrivalDate));""")
               except:
                    print("Already Done!")
               
               
               if(txt_BargeNo.get() != ''):
                    c.execute("""INSERT INTO barges(source, bargeNo, bargeArrivalDate, bargeArrivalTime,productDetails, productWithLid, comments) 
                                   VALUES (:source, :bargeNo,:bargeArrivalDate, :bargeArrivalTime, :productDetails, :productWithLid, :comments)""",
                                        {
                                             'source':txt_sourceLocation.get(),
                                             'bargeNo':txt_BargeNo.get(),
                                             'bargeArrivalDate': txt_BargeArrivalDate.get(),
                                             'bargeArrivalTime': txt_BargeArrivaltime.get(),
                                             'productDetails':txt_productlid.get(),
                                             'productWithLid':txt_productDetails.get('1.0',custom.END),
                                             'comments':txt_comments.get('1.0',custom.END)
                                        })
                    txt_sourceLocation.delete(0,custom.END)
                    txt_BargeNo.delete(0,custom.END)
                    txt_BargeArrivalDate.delete(0,custom.END)
                    txt_BargeArrivaltime.delete(0,custom.END)
                    txt_BargeArrivalDate.insert(0,string=getTime()[0])
                    txt_BargeArrivaltime.insert(0,string=getTime()[1])
                    txt_productlid.deselect()
                    txt_productDetails.delete('1.0',custom.END)
                    txt_comments.delete('1.0',custom.END)
                    clearError()
               else:
                    print("bargeNO is required")
                    errors()
               c.execute("SELECT bargeNo,bargeArrivalDate FROM barges")
               
               result= c.fetchall()
               
               print(result)
               
                    
               #commit changes
               conn.commit()

               #close connection
               conn.close()
               
               self.update()
               
          
          def __goBack():
               for widget in self.winfo_children():
                    widget.destroy()
               self.optionScreen()
          
          
          
          
          for widget in self.winfo_children():
               widget.destroy()
          
          self.columnconfigure(1,weight= 1)
          
          lbl_bargeheading= custom.CTkLabel(self,text="Barge Arrival Details")
          lbl_bargeheading2= custom.CTkLabel(self,text="Product Details")
          lbl_bargeheading3= custom.CTkLabel(self,text="Any Comments..")
          
          txt_sourceLocation= custom.CTkEntry(self,placeholder_text='try "portland"')
          txt_BargeNo = custom.CTkEntry(self,placeholder_text='try "XAE234"')
          txt_BargeArrivalDate = custom.CTkEntry(self)
          txt_BargeArrivalDate.insert(0,string=getTime()[0])
          txt_BargeArrivaltime = custom.CTkEntry(self)
          txt_BargeArrivaltime.insert(0,string=getTime()[1])
          
          txt_productlid = custom.CTkCheckBox(self,text="Product Has a Lid")
          txt_productDetails = custom.CTkTextbox(self,width=300,height=50,activate_scrollbars=True)
          
          txt_comments = custom.CTkTextbox(self,width=300,height=50,activate_scrollbars=True)
          
          lbl_sourceLocation = custom.CTkLabel(self,text="Source Location: ")
          lbl_BargeNo = custom.CTkLabel(self,text="Barge Number: ")
          lbl_BargeArrivalDate = custom.CTkLabel(self,text="Arrival Date: ")
          lbl_BargeArrivaltime= custom.CTkLabel(self,text="Arrival Time: ")
          
          btn_save = custom.CTkButton(self,width=150,text="save", command=__addToDb)
          btn_back = custom.CTkButton(self,width=150,text="back", command=__goBack)
          
          lbl_bargeheading.grid(row=0,column=0,columnspan=2)
          
          lbl_sourceLocation.grid(row=1,column=0)
          txt_sourceLocation.grid(row=1,column=1)
          
          lbl_BargeNo.grid(row=2,column=0)
          txt_BargeNo.grid(row=2,column=1)
          
          lbl_BargeArrivalDate.grid(row=3,column=0)
          txt_BargeArrivalDate.grid(row=3,column=1)
          
          lbl_BargeArrivaltime.grid(row=4,column=0)
          txt_BargeArrivaltime.grid(row=4,column=1)
          
          lbl_bargeheading2.grid(row=5,column=0,columnspan=2,pady=(15,0))
          
          txt_productDetails.grid(row=6,column=0,columnspan=2)
          txt_productlid.grid(row=7,column=0,columnspan=2,pady=(5,0))
          
          lbl_bargeheading3.grid(row=8,column=0,columnspan=2,pady=(15,0))
          txt_comments.grid(row=9,column=0,columnspan=2)
          
          btn_save.grid(row=10,column=1,padx=(20,0),pady=(15,0))
          btn_back.grid(row=10,column=0,padx=(20,0),pady=(15,0))
          

     
     def __findBarge(self):
          
          def __goBack():
               for widget in self.winfo_children():
                    widget.destroy()
               self.optionScreen()
          
          self.columnconfigure(1,weight= 1)
          
          
          
          for widget in self.winfo_children():
               widget.destroy()
          
          lbl_bargeheading= custom.CTkLabel(self,text="Barge Finder",font=headingFont)
          
          txt_BargeNo = custom.CTkEntry(self,placeholder_text='try "XAE234"')
          lbl_BargeNo = custom.CTkLabel(self,text="Barge Number: ")
          
          btn_departure = custom.CTkButton(self,width=150,text="Departure")
          btn_remove = custom.CTkButton(self,width=150,text="Remove")
          btn_back = custom.CTkButton(self,width=150,text="back", command=__goBack)
          
          lbl_bargeheading.grid(row=0,column=0,pady=15,columnspan=2)
          
          lbl_BargeNo.grid(row=1,column=0)
          txt_BargeNo.grid(row=1,column=1)
          
          btn_remove.grid(row=2,column=1,padx=(20,0),pady=(15,0))
          btn_departure.grid(row=2,column=0,padx=(20,0),pady=(15,0))
          btn_back.grid(row=3,column=0,padx=(20,0),pady=(15,0),columnspan=2)
          
          
class App(custom.CTk):
     def __init__(self):
          super().__init__()
          self.title("Plate Data smpl 1.0")
          self.geometry("500x500")
          self.columnconfigure(0,weight=1)
          
          global headingFont,subheadingFont,paragraphFont
          paragraphFont = custom.CTkFont(family="David",size=13)
          subheadingFont = custom.CTkFont(family="Merriweather", size= 20, weight="bold")
          headingFont = custom.CTkFont(family="Helvetica",size=25,weight="bold")
          
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
