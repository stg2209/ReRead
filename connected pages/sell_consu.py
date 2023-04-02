from tkinter import*;
from PIL import Image,ImageTk;

win= Tk();
win.configure(background="yellow");
# win.attributes('-fullscreen',True)
win.geometry("1400x620")
# win.minsize(500,500)
# win.maxsize(500,500)
win.title("ReRead")

def search_1():
    win.destroy()
    import search_1

def sell_ad():
    win.destroy()
    import sell_ad    

seller_b= Button(win, text="Seller",font=("papyrus",15),height= 1, width=8,command=sell_ad).pack(padx=2,pady=45)
or_l= Label(win, text="---or---",font=("papyrus",15),bg="yellow").pack(padx=10, pady=90);
consumer_b= Button(win, text="Consumer",font=("papyrus",15),height= 1, width=8, command=search_1).pack(padx=2,pady=60)

book_icon = PhotoImage(file = "sign_books.png")
win.iconphoto(False, book_icon)
win.mainloop()