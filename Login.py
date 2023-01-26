import sqlite3
from tkinter import Tk
import time
import sys
import customtkinter as custom
from datetime import datetime



#Header Frame
class CreateTop(custom.CTkFrame):   
     def __init__(self,container):
          super().__init__(container,height=50)
          self.columnconfigure(0,weight= 1)
          self.__createSubWidgets()
     
     def __createSubWidgets(self):
          lbl_heading = custom.CTkLabel(self, text= "Login", font=subheadingFont)
          lbl_heading.place(relx=0.5, rely=0.5, anchor='center')

#Content Frame
class CreateBottom(custom.CTkFrame):
     def __init__(self,container):
          super().__init__(container,fg_color='transparent')

          self.columnconfigure(0,weight= 1)
          self.productdetail =""
          self.entryData = custom.StringVar()
          
          self.__createLoginWidgets()
          
          
     def __createLoginWidgets(self):
          lbl_Name = custom.CTkLabel(self,text="Name: ",font=paragraphFont)
          lbl_Name.grid(row=0,column=0,padx=10,pady=10)
          
          txt_Name = custom.CTkEntry(self, width = 150, corner_radius=10, textvariable=self.entryData)
          txt_Name.grid(row=0,column=1,padx=10,pady=10)
          
          btn_Login = custom.CTkButton(self,width= 200,text="Login",command=self.__validateUser,font=paragraphFont)
          btn_Login.grid(row=1,column=0,columnspan=2,pady=10)
     
     #make sure the user is in the System, if not, Access will be denied and app will be terminated      
     def __validateUser(self):
               
               # if user name = yohan, then procced to the optionScreen
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
     
     #Provides user with buttons to enter details about ARRIVAL, DEPARTURE, REMOVAL AND REPORTS
     def optionScreen(self):
          #ARRIVAL ---CALLS--> __captureDetailsArrival
          custom.CTkLabel(self,text="If your Barge just arrived",font=paragraphFont).grid(row=0,column=0)
          custom.CTkButton(self,width=100,text="Arrival",command=self.__captureDetailsArrival).grid(row=1,column=0,pady=(0,15))
          
          #DEPARTURE---CALLS--> __findBarge
          custom.CTkLabel(self,text="If your Barge is Leaving Now",font=paragraphFont).grid(row=2,column=0)
          custom.CTkButton(self,width=100,text="Departure",command=self.__findBarge).grid(row=3,column=0,pady=(0,15))
          
          #REMOVAL---CALLS--> __findBarge
          custom.CTkLabel(self,text="If you want to remove a Previous Barge",font=paragraphFont).grid(row=4,column=0)
          custom.CTkButton(self,width=100,text="Remove Barge",command=self.__findBarge).grid(row=5,column=0,pady=(0,15))
          
          #REPORTS---CALLS--> __captureDetailsDeparture
          custom.CTkLabel(self,text="If you would like to see a Report",font=paragraphFont).grid(row=6,column=0)
          custom.CTkButton(self,width=100,text="Reports").grid(row=7,column=0,pady=(0,15))

     #Screen to enter all the arrival details
     def __captureDetailsArrival(self):
          
          #methods
          # makes sure text is entered for the BargeNo
          def errors():
                txt_BargeNo.configure(placeholder_text="REQUIRED",border_color='red')

          # clears the errors, when everything is valid
          def clearError():
               txt_BargeNo.configure(placeholder_text='try "XAE234"',border_color= txt_BargeArrivalDate._border_color )
               lbl_error.grid_forget() 
          
          # returns current time and date 
          def getTime():
               todayTime_date=datetime.now()
               day = todayTime_date.strftime("%D")
               time = todayTime_date.strftime("%I:%M")
               return day,time
          
          # method for submit button
          def __addToDb():
               
                #create a db
               conn = sqlite3.connect('barge_book.db')
               c = conn.cursor()
               # c.execute("DROP TABLE barges")
               
               #create the table if it hasnt been already created
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
                    pass
               
               #insert into the table
               try:
                    #checking to see if barge No is entererd
                    if txt_BargeNo.get() == '' or txt_BargeNo.get() == ' ':
                         raise sqlite3.IntegrityError
                    
                    #insert into barges
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
                    
                    #clear all the text fields and any errors
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
                    
                    c.execute("SELECT * FROM barges")
                    result= c.fetchall()
                    print(result)
                    
               except sqlite3.IntegrityError:
                    if txt_BargeNo.get() == '' or txt_BargeNo.get() == ' ':
                         errors()
                    else:
                         lbl_error.grid(row=3,column=1)
                         print("the record already exisits")

               #close connection
               conn.commit()
               conn.close()
               self.update()
          
          #goes back the __optionScreen     
          def __goBack():
               for widget in self.winfo_children():
                    widget.destroy()
               self.optionScreen()
 
          #first clears the frame and starts adding all the ARRIVAL PROMPTS
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
          lbl_error = custom.CTkLabel(self,text="duplicate entry on same date not allowed", text_color= 'red')
          lbl_BargeNo = custom.CTkLabel(self,text="Barge Number: ")
          lbl_BargeArrivalDate = custom.CTkLabel(self,text="Arrival Date: ")
          lbl_BargeArrivaltime= custom.CTkLabel(self,text="Arrival Time: ")
          
          btn_save = custom.CTkButton(self,width=150,text="save", command=__addToDb)
          btn_back = custom.CTkButton(self,width=150,text="back", command=__goBack)
          
          #placing them on the grid
          lbl_bargeheading.grid(row=0,column=0,columnspan=2)
          
          lbl_sourceLocation.grid(row=1,column=0)
          txt_sourceLocation.grid(row=1,column=1)
          
          lbl_BargeNo.grid(row=2,column=0)
          txt_BargeNo.grid(row=2,column=1)
          
          lbl_BargeArrivalDate.grid(row=4,column=0)
          txt_BargeArrivalDate.grid(row=4,column=1)
          
          lbl_BargeArrivaltime.grid(row=5,column=0)
          txt_BargeArrivaltime.grid(row=5,column=1)
          
          lbl_bargeheading2.grid(row=6,column=0,columnspan=2,pady=(15,0))
          
          txt_productDetails.grid(row=7,column=0,columnspan=2)
          txt_productlid.grid(row=8,column=0,columnspan=2,pady=(5,0))
          
          lbl_bargeheading3.grid(row=9,column=0,columnspan=2,pady=(15,0))
          txt_comments.grid(row=10,column=0,columnspan=2)
          
          btn_save.grid(row=11,column=1,padx=(20,0),pady=(15,0))
          btn_back.grid(row=11,column=0,padx=(20,0),pady=(15,0))
          
     #find the barge before removing it or entering the departure details         
     def __findBarge(self):
          
          # returns current time and date 
          def getTime():
               todayTime_date=datetime.now()
               day = todayTime_date.strftime("%D")
               time = todayTime_date.strftime("%I:%M")
               return day,time
  
          #back button Method
          def __goBack():
               
               for widget in self.winfo_children():
                    widget.destroy()
               self.optionScreen()

          #Remove Button Method
          def __deleteBarge():
               conn = sqlite3.connect('barge_book.db')
               c = conn.cursor()
               
               # put it into a array ["bargeNo","on","arrival Date"]
               x = selectedBarge.get().split(" ")
               
               barge = x[0]
               arivalDate = x[2]
               try:
                    c.execute("""DELETE FROM barges
                                   WHERE bargeNo = ? AND bargeArrivalDate = ?
                              
                              """, (barge,arivalDate))
               except:
                    pass
               
               #close connection
               conn.commit()
               conn.close()
               self.update()
               __goBack()

         
          def __captureDetailsDeparture(y):
               def __addToDb():
                         c = conn.cursor()
                         
                         #insert into the table
                              
                         #insert into barges
                         args = (txt_BargeDepartureDate.get(),txt_BargeDeparturetime.get(),txt_comments.get('1.0',custom.END),y[0],y[2])
                         c.execute("""UPDATE barges
                                        SET bargeReleasetime = ? , bargeReleaseDate = ?,comments= ?
                                        WHERE bargeNo = ? AND bargeArrivalDate = ?""", args)
                         
                         #clear all the text fields and any errors
                         
                         c.execute("SELECT * FROM barges")
                         result= c.fetchall()
                         print(result)
                              
                         #close connection
                         conn.commit()
                         conn.close()
                         self.update()

               conn = sqlite3.connect('barge_book.db')
               c = conn.cursor()
               
               args = (y[0],y[2])
               c.execute("SELECT comments FROM barges WHERE bargeNo = ? AND bargeArrivalDate = ?",args)
               result= c.fetchall()
               
               
               #first clears the frame and starts adding all the ARRIVAL PROMPTS
               for widget in self.winfo_children():
                    widget.destroy()
               
               lbl_bargeheading= custom.CTkLabel(self,text="Barge Departure Details")
               lbl_bargeheading3= custom.CTkLabel(self,text="Any Comments..")
               
               lbl_BargeDepartureDate = custom.CTkLabel(self,text="Departure Date: ")
               lbl_BargeDeparturetime= custom.CTkLabel(self,text="Departure Time: ")
               
               txt_BargeDepartureDate = custom.CTkEntry(self)
               txt_BargeDepartureDate.insert(0,string=getTime()[0])
               txt_BargeDeparturetime = custom.CTkEntry(self)
               txt_BargeDeparturetime.insert(0,string=getTime()[1])
               
               txt_comments = custom.CTkTextbox(self,width=300,height=50,activate_scrollbars=True)
               
               btn_save = custom.CTkButton(self,width=150,text="save", command=__addToDb)
               btn_back = custom.CTkButton(self,width=150,text="back", command=__goBack)
               
               lbl_bargeheading.grid(row=0,column=0,columnspan=2)
               
               lbl_BargeDepartureDate.grid(row=1,column=0)
               txt_BargeDepartureDate.grid(row=1,column=1)
          
               lbl_BargeDeparturetime.grid(row=2,column=0)
               txt_BargeDeparturetime.grid(row=2,column=1)
               
               lbl_bargeheading3.grid(row=3,column=0,columnspan=2,pady=(15,0))
               txt_comments.grid(row=4,column=0,columnspan=2)
               txt_comments.insert("0.0",text=result[0][0])
               
               btn_save.grid(row=5,column=1,padx=(20,0),pady=(15,0))
               btn_back.grid(row=5,column=0,padx=(20,0),pady=(15,0))
               
          
               
          self.columnconfigure(1,weight= 1)
          
          #connects to the DataBase in the system
          conn = sqlite3.connect('barge_book.db')
          c = conn.cursor()
          
          #Store all the BargeNo and Arrival Dates into an array
          x= []
          c.execute("SELECT bargeNo,bargeArrivalDate FROM barges")
          result= c.fetchall()
          for details in result:
              x.append(details[0] +" on " +details[1]) 

          #variable that holds the Selected Drop down list value
          selectedBarge = custom.StringVar()

          #Clears the screen
          for widget in self.winfo_children():
               widget.destroy()
          
          #creates the find Barge screen
          lbl_bargeheading= custom.CTkLabel(self,text="Barge Finder",font=headingFont)
          
          txt_BargeNo = custom.CTkComboBox(self, variable= selectedBarge ,values=x)
          lbl_BargeNo = custom.CTkLabel(self,text="Barge Number: ")
          
          btn_departure = custom.CTkButton(self,width=150,text="Departure", command= lambda: __captureDetailsDeparture(selectedBarge.get().split(" ")) )
          btn_remove = custom.CTkButton(self,width=150,text="Remove",command = __deleteBarge)
          btn_back = custom.CTkButton(self,width=150,text="back", command=__goBack)
          
          lbl_bargeheading.grid(row=0,column=0,pady=15,columnspan=2)
          
          lbl_BargeNo.grid(row=1,column=0)
          txt_BargeNo.grid(row=1,column=1)
          
          btn_remove.grid(row=2,column=1,padx=(20,0),pady=(15,0))
          btn_departure.grid(row=2,column=0,padx=(20,0),pady=(15,0))
          btn_back.grid(row=3,column=0,padx=(20,0),pady=(15,0),columnspan=2)
          
          #close the db connection and clear the array
          conn.commit()
          conn.close()
          self.update()
          x = []

# Creates the Window
class App(custom.CTk):
     def __init__(self):
          super().__init__()
          self.title("Plate Data smpl 1.0")
          self.geometry("500x550")
          self.columnconfigure(0,weight=1)
          
          #fonts for the app
          global headingFont,subheadingFont,paragraphFont
          paragraphFont = custom.CTkFont(family="David",size=13)
          subheadingFont = custom.CTkFont(family="Merriweather", size= 20, weight="bold")
          headingFont = custom.CTkFont(family="Helvetica",size=25,weight="bold")
          
          self.__createSubWidgets()
     
     #creates 2 frames(top{header} and bottom{content}) 
     def __createSubWidgets(self):
          frame_Top = CreateTop(self)
          frame_Top.grid(row=0,column=0,sticky='ew')
          
          frame_Bottom = CreateBottom(self)
          frame_Bottom.place(relx=0.5,rely=0.5, anchor='center')

#Main
if __name__ == "__main__":
     app = App()     
     app.mainloop()