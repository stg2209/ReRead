from tkinter import*
from tkinter.ttk import Combobox;
from PIL import Image,ImageTk;
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from tkinter import messagebox

import mysqlx;

win= Tk();
win.configure(background="yellow");
#win.attributes('-fullscreen',True)
win.geometry("1400x620")
#win.minsize(1400,620)
# win.maxsize(500,500)
win.title("ReRead")
image=0
# frame_opts= Frame(win,width=1050,height=550,highlightbackground='Red',highlightthickness=3,bg='yellow').grid(row=1,column=1,padx=0,pady=0)
# # frame_opts.grid(row=0,column=0,padx=290,pady=30)

#frame_ad= Frame(win,width=1400,height=700,highlightbackground='Red',highlightthickness=3,bg='yellow').pack()
#frame_ad.grid(row=0,column=0,padx=120,pady=170
# consumer_mod = Button(win, text="Consumer mode",font=("papyrus",10)).grid(row=0,column=0,padx=40,pady=0)
# consumer_mod = Button(win, text="Previous ads",font=("papyrus",10)).grid(row=0,column=1,padx=0,pady=0)

#frame_ad= Frame(win,width=1050,height=550,highlightbackground='Red',highlightthickness=3,bg='yellow').pack(side=BOTTOM)

def search_1():
    win.destroy()
    import search_1
consumer_mod = Button(win, text="Consumer mode",font=("papyrus",10),command=search_1).place(x=450,y=0)
prev_ad = Button(win, text="Previous ads",font=("papyrus",10)).place(x=750,y=0)

title_l= Label(win,text="Title :",fg="black",font=("papyrus",15),bg="yellow").place(x=250,y=100);
title_e= Entry(win, font=('calibre',10,'normal')).place(x=350,y=110,width=600,height=30)
#title=title_e.get()

subject_label = Label(win, text="Select Subject:",font="papyrus",bg="yellow")
subject_label.place(x=350,y=150)
subject_var = StringVar()
subject = Combobox(win, textvariable=subject_var, values=["AT", "CN", "OS", "Maths", "Python"])
subject.place(x=350, y=190)

sem_label = Label(win, text="Select semester of Study:",font="papyrus",bg="yellow")
sem_label.place(x=500, y=150)
sem_var = StringVar()
sem = Combobox(win, textvariable=sem_var, values=["1","2","3", "4","5","6","7","8",])
sem.place(x=530,y=190) 

type_label = Label(win, text="Select Reference Book Type:",font="papyrus",bg="yellow")
type_label.place(x=750, y=150)
type_var = StringVar()
type = Combobox(win, textvariable=type_var, values=["Reference Book", "Handwritten Notes", "Other"])
type.place(x=800,y=190)

desp_l= Label(win,text="Description :",fg="black",font=("papyrus",15),bg="yellow").place(x=250,y=220);
#desp_e= Entry(win, font=('calibre',10,'normal')).place(x=400,y=350,width=600,height=150)
desp_t =Text(win, width=80, height=10).place(x=400,y=220)
#desp=desp_t.get()

# mydb = mysqlx.connector.connect(
#   host="localhost",
#   user="root",
#   password="root",
#   database="reread"
# )

# mycursor = mydb.cursor()

# def save_data():
#     # Get the values from the input fields
#     title = title_e.get()
#     subject = subject_var.get()
#     sem = sem_var.get()
#     type = type_var.get()
#     desp= desp_t.get()
    
    

#     # Insert the values into the table
#     sql = "INSERT INTO users (user_name, user_username, user_contact, user_email, user_library, user_password,user_gender,user_year) VALUES (%s,%s, %s, %s,%s,%s,%s,%s)"
#     val = (name,username, contact, email,lib,password,gender,year)
#     mycursor.execute(sql, val)

#     # Commit the changes
#     mydb.commit()

#     # Clear the input fields
#     name_entry.delete(0, tk.END)
#     contact_entry.delete(0, tk.END)
#     email_entry.delete(0, tk.END)
#     lib_entry.delete(0,tk.END)
#     password_entry.delete(0,tk.END)
#     reenter_entry.delete(0,tk.END)
#     # gender_entry.delete(0,tk.END)
#     messagebox.showinfo("Successful","Advertisement placed successfully")

def win_image():
    def upload_file():
    
   
     f_types = [('Jpg Files', '*.jpg'),
     ('PNG Files','*.png')]   # type of files to select 
     filename = filedialog.askopenfilename(multiple=True,filetypes=f_types)
     col=1 # start from column 1
     row=5 # start from row 3 
     for f in filename:
        img=Image.open(f) # read the image file
        img=img.resize((100,100)) # new width & height
        img=ImageTk.PhotoImage(img)
        e1 =Label(win_image)
        e1.grid(row=row,column=col)
        e1.image = img # keep a reference! by attaching it to a widget attribute
        e1['image']=img # Show Image
        image=1;  
        if(col==3): # start new line after third column
            row=row+1# start wtih next row
            col=1    # start with first column
            
        else:       # within the same row 
            col=col+1 # increase to next column 
 
    #win.destroy()
    # import add_image
    win_image=Tk()
    b1 = Button(win_image, text='Upload Files',width=20,command = lambda:upload_file()).grid(row=2,column=1,columnspan=4)
    #back= Button(win_image, text='Back', width=20)
    win_image.geometry("410x300")  # Size of the window 
    win_image.title('ReRead')
    book_icon = PhotoImage(file = "sign_books.png")
    win_image.iconphoto(False, book_icon)
    win_image.mainloop()
                
def success():
#  # if len(title_e.get())!=0 and len(subject.get())!=0 and len(sem.get())!=0 and len(type.get())!=0 and len(desp_t.get())!=0 :
#   #if len(title)!=0 and  len(desp)!=0 : 
   messagebox.showinfo("Successful","Advertisement placed successfully")                
add_img_b= Button(win, text="Add images",width="10",font=("papyrus",10),command=win_image).place(x=250,y=400)



publish_b= Button(win, text="Publish",width="10",font=("papyrus",10),command=success).place(x=600,y=500)

book_icon = PhotoImage(file = "sign_books.png")


win.iconphoto(False, book_icon)
win.mainloop()