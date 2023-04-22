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
year_label = tk.Label(window, text="Year")
year_label.grid(row=2, column=0)
year_entry = tk.StringVar()
year_options = ["First", "Second", "Third", "Fourth"]
year_dropdown = tk.OptionMenu(window, year_entry, *year_options)
year_dropdown.grid(row=2, column=1)


# Connect to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="reread"
)

# Create a table in the MySQL database
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS mytable1 (name VARCHAR(255), year VARCHAR(255))")

# Define a function to save the data to the MySQL database
def save_data():
    # Get the values from the input fields
    name = name_entry.get()
    year = year_entry.get()
    

    # Insert the values into the table
    sql = "INSERT INTO mytable1 (name,year) VALUES (%s, %s)"
    val = (name,year)
    mycursor.execute(sql, val)

    # Commit the changes
    mydb.commit()

    # Clear the input fields
    name_entry.delete(0, tk.END)

    import remindmedirectcode as rd
   
# Create the "Save" button and connect it to the save_data() function
save_button = tk.Button(window, text="Save", command=save_data)
save_button.grid(row=3, column=1)

# Run the GUI window
window.mainloop()
