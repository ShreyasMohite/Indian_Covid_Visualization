from tkinter import *
from tkinter.ttk import Combobox
import tkinter.messagebox
from covid_india import states
import json
import threading
import matplotlib.pyplot as mp



class Covid_Visualization:
    def __init__(self,root):
        self.root=root
        self.root.title("Covid Visualzation")
        self.root.geometry("400x200")
        self.root.iconbitmap("logo620.ico")
        self.root.resizable(0,0)


        states_data=StringVar()




        def on_enter1(e):
            but_check['background']="black"
            but_check['foreground']="cyan"
            
            

        def on_leave1(e):
            but_check['background']="SystemButtonFace"
            but_check['foreground']="SystemButtonText"


        def on_enter2(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"
            
            

        def on_leave2(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"




        def clear():
            states_data.set("Select Indian States")

        def find_data():
            try:
                if states_data.get()!="Select Indian States":

                    ab=json.dumps(states.getdata(states_data.get()))
                    x=json.loads(ab)
                    active=x['Active']
                    cured=x['Cured']
                    death=x['Death']
                    
                    
                    #print(active)
                    #print(cured)
                    #print(death)
                    names=['Active','Cured','Death']
                    h=[active,cured,death]
                    mp.bar(names,h,width=0.2)
                    mp.xlabel("Name of Cases")
                    mp.ylabel("Number of Cases")
                    mp.title(states_data.get() +" State Covid Visualization")
                    mp.show()

                else:
                    tkinter.messagebox.showerror("Error","Please Select State")
            except Exception as e:
                tkinter.messagebox.showerror("Error","Something went wrong")
                print(e)
            


            


#=======================frame===========================#
        
        mainframe=Frame(self.root,width=400,height=200,relief="ridge",bd=3,bg="#144e78")
        mainframe.place(x=0,y=0)


        select_state=['Andaman and Nicobar Islands','Andhra Pradesh',\
                      'Arunachal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh',\
                      'Dadra and Nagar Haveli and Daman and Diu','Delhi','Goa','Gujarat',\
                      'Haryana','Himachal Pradesh',\
                      'Jammu and Kashmir','Jharkhand','Karnataka','Kerala','Ladakh','Lakshadweep',\
                      'Madhya Pradesh','Maharashtra',\
                      'Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Puducherry','Punjab',\
                      'Rajasthan','Sikkim','Tamil Nadu',\
                      'Telengana','Tripura','Uttarakhand','Uttar Pradesh','West Bengal']
        select_state_combo=Combobox(mainframe,values=select_state,font=('arial',14),width=23,state="readonly",textvariable=states_data)
        select_state_combo.set("Select Indian States")
        select_state_combo.place(x=60,y=30)

        but_check=Button(mainframe,width=17,text="Check",font=('times new roman',12),cursor="hand2",command=find_data)
        but_check.place(x=20,y=90)
        but_check.bind("<Enter>",on_enter1)
        but_check.bind("<Leave>",on_leave1)

        but_clear=Button(mainframe,width=17,text="Clear",font=('times new roman',12),cursor="hand2",command=clear)
        but_clear.place(x=210,y=90)
        but_clear.bind("<Enter>",on_enter2)
        but_clear.bind("<Leave>",on_leave2)







if __name__ == "__main__":
    root=Tk()
    Covid_Visualization(root)
    root.mainloop()