from tkinter import*
from tkinter.ttk import Combobox;
from PIL import Image,ImageTk;
from tkinter import filedialog
from tkinter.filedialog import askopenfile

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
        if(col==3): # start new line after third column
            row=row+1# start wtih next row
            col=1    # start with first column
        else:       # within the same row 
            col=col+1 # increase to next column 

win_image=Tk()
b1 = Button(win_image, text='Upload Files',width=20,command = lambda:upload_file()).grid(row=2,column=1,columnspan=4)
back= Button(win_image, text='Back', width=20)
win_image.geometry("410x300")  # Size of the window 
win_image.title('ReRead')
book_icon = PhotoImage(file = "sign_books.png")
win_image.iconphoto(False, book_icon)
win_image.mainloop()

