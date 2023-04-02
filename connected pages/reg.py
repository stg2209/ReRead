import tkinter as tk
from tkinter import Radiobutton, messagebox
import mysql.connector

# Create the GUI window
window = tk.Tk()
window.title("ReRead")
window.geometry('600x700')
window.minsize(600,700)
window.maxsize(600,700)  
window.configure(background="yellow");
window.title("ReRead")  

# Create the labels and input fields
name_label = tk.Label(window, text="Name",font=("papyrus",15),bg="yellow")
name_label.place(x=80,y=90) 
name_entry = tk.Entry(window)
name_entry.place(x=280,y=90) 

username_label = tk.Label(window, text="Username",font=("papyrus",15),bg="yellow")
username_label.place(x=80,y=135) 
username_entry = tk.Entry(window)
username_entry.place(x=280,y=135) 

contact_label = tk.Label(window, text="Contact",font=("papyrus",15),bg="yellow")
contact_label.place(x=80,y=180) 
contact_entry = tk.Entry(window)
contact_entry.place(x=280,y=180) 

email_label = tk.Label(window, text="Email",font=("papyrus",15),bg="yellow")
email_label.place(x=80,y=280) 
email_entry = tk.Entry(window)
email_entry.place(x=280,y=280) 

lib_label = tk.Label(window, text="Libraryid",font=("papyrus",15),bg="yellow")
lib_label.place(x=80,y=330)
lib_entry = tk.Entry(window)
lib_entry.place(x=280,y=330) 

password_label = tk.Label(window, text="Password",font=("papyrus",15),bg="yellow")
password_label.place(x=80,y=430)
password_entry = tk.Entry(window)
password_entry.place(x=300,y=430)  

reenter_label = tk.Label(window, text="Reenter",font=("papyrus",15),bg="yellow")
reenter_label.place(x=80,y=480)
reenter_entry = tk.Entry(window)
reenter_entry.place(x=300,y=480) 

gender_label = tk.Label(window, text="Gender",font=("papyrus",15),bg="yellow")
gender_label.place(x=80,y=230)
gender_entry =tk.StringVar()
male_entry = tk.Radiobutton(window,text ="Male",variable =gender_entry ,value="Male",font=("papyrus",15),bg="yellow")
male_entry.place(x=280,y=230) 
female_entry = tk.Radiobutton(window,text ="Female",variable =gender_entry,value="Female",font=("papyrus",15),bg="yellow")
female_entry.place(x=355,y=230) 

year_label = tk.Label(window, text="Year",font=("papyrus",15),bg="yellow")
year_label.place(x=80,y=380) 
year_entry = tk.StringVar()
year_options = ["First", "Second", "Third", "Fourth"]
year_dropdown = tk.OptionMenu(window, year_entry, *year_options)
year_dropdown.place(x=300,y=380) 



# Connect to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="reread"
)

# Create a table in the MySQL database
mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE IF NOT EXISTS mytable (name VARCHAR(255), contact INT,email VARCHAR(255),lib INT,password VARCHAR(255),reenter VARCHAR(255),gender VARCHAR(255),year VARCHAR(255))")

# Define a function to save the data to the MySQL database
def save_data():
    # Get the values from the input fields
    name = name_entry.get()
    contact = contact_entry.get()
    email = email_entry.get()
    lib = lib_entry.get()
    password = password_entry.get()
    reenter = reenter_entry.get()
    gender = gender_entry.get()
    year = year_entry.get()
    username = username_entry.get()
    

    # Insert the values into the table
    sql = "INSERT INTO users (user_name, user_username, user_contact, user_email, user_library, user_password,user_gender,user_year) VALUES (%s,%s, %s, %s,%s,%s,%s,%s)"
    val = (name,username, contact, email,lib,password,gender,year)
    mycursor.execute(sql, val)

    # Commit the changes
    mydb.commit()

    # Clear the input fields
    name_entry.delete(0, tk.END)
    contact_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    lib_entry.delete(0,tk.END)
    password_entry.delete(0,tk.END)
    reenter_entry.delete(0,tk.END)
    # gender_entry.delete(0,tk.END)
    messagebox.showinfo("Successful","Registered successfully") 
    sell_consu()

def sell_consu():
    window.destroy()
    import sell_consu
# Create the "Save" button and connect it to the save_data() function
save_button = tk.Button(window, text="Save", font=("papyrus",12),command=save_data)
save_button.place(x=320,y=520)

# Run the GUI window
window.mainloop()