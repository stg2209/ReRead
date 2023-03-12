from tkinter import*;
from PIL import Image,ImageTk;

win= Tk();
win.configure(background="yellow");
win.geometry("500x500")
win.minsize(500,500)
win.maxsize(500,500)
win.title("ReRead")
sign_in= Label(win, text="Sign in :", fg="black",font=("papyrus",15),bg="yellow").grid(row=0,column=2);
username_l= Label(win,text="Username :",fg="black",font=("papyrus",15),bg="yellow").grid(row=2,column=4);
password_l= Label(win,text="password :",fg="black",font=("papyrus",15),bg="yellow").grid(row=4,column=4);
username_e= Entry(win, font=('calibre',10,'normal')).grid(row=2,column=6);
password_e= Entry(win, font=('calibre',10,'normal'),show="*").grid(row=4,column=6);

or_l= Label(win, text="---or---",font=("papyrus",10),bg="yellow").grid(row=7, column=6);
creat_acc_b= Button(win, text="Create account",width="10",font=("papyrus",15)).grid(row=9,column=6);

sign_in_b= Button(win, text="Sign in",font=("papyrus",15)).grid(row=5,column=6)

book_icon = PhotoImage(file = "sign_books.png")
win.iconphoto(False, book_icon)
# books=PhotoImage(file='sign_books.jpg')
# Label(win,image=books).grid(row=15,column=12);

# img = ImageTk.PhotoImage(Image.open("C:\Users\Soham\Documents\Code\python\ReRead"))

# #The Label widget is a standard Tkinter widget used to display a text or image on the screen.
# panel = tk.Label(win, image = img)

#sign_books= Imagetk.PhotoImage(file='C:\\Users\\Soham\\Documents\\Code\\python\\ReRead\\sign_books.jpg')
# sign_book_i= ImageTk.PhotoImage(Image.open("sign_books.png"))
# sign_book_l= Label(win,image=sign_book_i,width="250",height="150").grid(row=12,column=6)

# creat_acc_i= ImageTk.PhotoImage(Image.open("creat_acc.png"))
# creat_acc_l= Label(win,image=creat_acc_i,width=50,height=50).grid(row=7,column=5)

#win.create_image(0,0,ANCHOR=NW, image=sign_books);

win.mainloop();
