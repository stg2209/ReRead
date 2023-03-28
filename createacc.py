from tkinter import*  
base = Tk()  
base.geometry('600x700')
base.minsize(600,700)
base.maxsize(600,700)  
base.configure(background="yellow");
base.title("ReRead")  
  

        
labl_0 = Label(base, text="Registration form",width=20,font=("papyrus",18,"bold"),bg="yellow")
labl_0.place(x=120,y=53)  
  
  
name = Label(base, text="Name",width=20,font=("papyrus",12,"bold"),bg="yellow")
name.place(x=60,y=130)    
entry_name = Entry(base,width = 20, font=('Arial', 12))  
entry_name.place(x=280,y=130)  
  
email = Label(base, text="Email",width=20,font=("papyrus",12,"bold"),bg="yellow")  
email.place(x=60,y=180)   
entry_email = Entry(base,width = 20, font=('Arial', 12))  
entry_email.place(x=280,y=180)  
  
gender = Label(base, text="Gender",width=20,font=("papyrus",12,"bold"),bg="yellow")  
gender.place(x=60,y=230)  
varblbl = IntVar() 
Radiobutton(base, text="Male",padx = 5, variable =varblbl, value=1).place(x=280,y=230)  
Radiobutton(base, text="Female",padx = 20, variable =varblbl, value=2).place(x=335,y=230)  
  
libraryCard= Label(base, text="Library Card No.",width=20,font=("papyrus",12,"bold"),bg="yellow")  
libraryCard.place(x=60,y=280)    
entry_library = Entry(base,width = 20, font=('Arial', 12))  
entry_library.place(x=280,y=280)  

mobile = Label(base, text="Mobile No.",width=20,font=("papyrus",12,"bold"),bg="yellow")  
mobile.place(x=60,y=330)    
entry_mobile = Entry(base,width = 20, font=('Arial', 12))  
entry_mobile.place(x=280,y=330) 

years = ("1st", "2nd", "3rd", "4th")  
cy = StringVar()  
ylist= OptionMenu(base, cy, *years)  
ylist.config(width=15)  
cy.set("")  
academicyear= Label(base, text="Current Academic Year ", width=20,font=("papyrus",12,"bold"),bg="yellow")  
academicyear.place(x=60,y=380)  
ylist.place(x=300,y=380)  

password = Label(base, text="Password",width=20,font=("papyrus",12,"bold"),bg="yellow")  
password.place(x=60,y=430)    
password= Entry(base,width = 20,show = "*")  
password.place(x=300,y=430)  
  
  
epassword = Label(base, text="Re-Enter Password",width=20,font=("papyrus",12,"bold"),bg="yellow")  
epassword.place(x=60,y=480)    
epassword= Entry(base,width = 20,show = "*")  
epassword.place(x=300,y=480)  
  
  #sign_in= Label(win, text="Sign in :", fg="black",font=("papyrus",15),bg="yellow").grid(row=0,column=2);
  
Button(base, text='Submit',width=30,bg='brown',fg='white').place(x=190,y=560)  
# it will be used for displaying the registration form onto the window  
base.mainloop()  
print("Registration form is created seccussfully...")  


