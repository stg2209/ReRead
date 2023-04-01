import tkinter as tk
from tkinter import Radiobutton, messagebox
import mysql.connector

# Create the GUI window
window = tk.Tk()
window.title("ReRead")

# Create the labels and input fields
name_label = tk.Label(window, text="Name")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1)

contact_label = tk.Label(window, text="Contact")
contact_label.grid(row=1, column=0)
contact_entry = tk.Entry(window)
contact_entry.grid(row=1, column=1)

email_label = tk.Label(window, text="Email")
email_label.grid(row=2, column=0)
email_entry = tk.Entry(window)
email_entry.grid(row=2, column=1)

lib_label = tk.Label(window, text="Libraryid")
lib_label.grid(row=3, column=0)
lib_entry = tk.Entry(window)
lib_entry.grid(row=3, column=1)

password_label = tk.Label(window, text="Password")
password_label.grid(row=4, column=0)
password_entry = tk.Entry(window)
password_entry.grid(row=4, column=1)

reenter_label = tk.Label(window, text="Reenter")
reenter_label.grid(row=5, column=0)
reenter_entry = tk.Entry(window)
reenter_entry.grid(row=5, column=1)

gender_label = tk.Label(window, text="Gender")
gender_label.grid(row=6, column=0)
gender_entry =tk.StringVar()
male_entry = tk.Radiobutton(window,text ="Male",variable =gender_entry ,value="Male")
male_entry.grid(row=6, column=1)
female_entry = tk.Radiobutton(window,text ="Female",variable =gender_entry,value="Female")
female_entry.grid(row=6, column=2)

year_label = tk.Label(window, text="Year")
year_label.grid(row=7, column=0)
year_entry = tk.StringVar()
year_options = ["First", "Second", "Third", "Fourth"]
year_dropdown = tk.OptionMenu(window, year_entry, *year_options)
year_dropdown.grid(row=7, column=1)



# Connect to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="reread"
)

# Create a table in the MySQL database
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS mytable (name VARCHAR(255), contact INT,email VARCHAR(255),lib INT,password VARCHAR(255),reenter VARCHAR(255),gender VARCHAR(255),year VARCHAR(255))")

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
    

    # Insert the values into the table
    sql = "INSERT INTO mytable (name, contact, email, lib,password,reenter,gender,year) VALUES (%s, %s, %s,%s,%s,%s,%s,%s)"
    val = (name, contact, email,lib,password,reenter,gender,year)
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


# Create the "Save" button and connect it to the save_data() function
save_button = tk.Button(window, text="Save", command=save_data)
save_button.grid(row=8, column=1)

# Run the GUI window
window.mainloop()
