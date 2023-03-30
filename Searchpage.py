import tkinter as tk
from tkinter import ttk

# create the search window
search_window = tk.Tk()
search_window.title("ReRead - Search Engine")
search_window.geometry("1050x650")
search_window.configure(bg="yellow")

# create a label widget for the "rea" title and pack it to the left
title_label = tk.Label(search_window, text="ReRead", font=("papyrus", 30, "bold"))
title_label.pack(side="top", padx=10)

# create the frame to hold the dropdown menus and search bar and search button
top_frame = tk.Frame(search_window)
top_frame.pack()

# create a label for the first dropdown menu
menu1_label = tk.Label(top_frame, text="Select Year of Study:")
menu1_label.pack(side="top", padx=10)

# create the first dropdown menu
menu1_var = tk.StringVar()
menu1 = ttk.Combobox(top_frame, textvariable=menu1_var, values=["First", "Second", "Third", "Fourth"])
menu1.pack(side="top", padx=10)

# create a label for the second dropdown menu
menu2_label = tk.Label(top_frame, text="Select Reference Book Type:")
menu2_label.pack(side="top", padx=10)

# create the second dropdown menu
menu2_var = tk.StringVar()
menu2 = ttk.Combobox(top_frame, textvariable=menu2_var, values=["Reference Book", "Handwritten Notes", "Other"])
menu2.pack(side="top", padx=10)

# create a label for the third dropdown menu
menu3_label = tk.Label(top_frame, text="Select Subject:")
menu3_label.pack(side="top", padx=10)

# create the third dropdown menu
menu3_var = tk.StringVar()
menu3 = ttk.Combobox(top_frame, textvariable=menu3_var, values=["AT", "CN", "OS", "Maths", "Python"])
menu3.pack(side="top", padx=10)

# create the frame to hold search bar and search button
search_frame = tk.Frame(search_window)
search_frame.pack()

# create the search bar and pack it to the left with double font size
search_bar = tk.Entry(search_frame, width=50, font=("papyrus", 16))
search_bar.pack(side="left")

# create the search button and pack it to the left with double font size
search_button = tk.Button(search_frame, text="Search", font=("papyrus", 16))
search_button.pack(side="left", padx=5)

# create a clear button and pack it to the left with double font size
clear_button = tk.Button(search_frame, text="Clear", font=("papyrus", 16))
clear_button.pack(side="left", padx=5)

# create a list to hold the result labels and text widgets
result_labels = []
results_text_widgets = []
blank_labels = []

# retrieve the data
data = ["Kumbhojkar", "kumbhojkar", "OS Notes","os notes", "COA Slides", "Computer Network PPt"]

# create a function to open a new window
# def open_new_window():
#     new_window = tk.Toplevel(search_window)
#     new_window.title("New Window")
#     new_window.geometry("900x600")
#     new_window.configure(bg="Yellow")

#     # create a label widget in the new window
#     message_label = tk.Label(new_window, text="You clicked the image!", font=("papyrus", 16))
#     message_label.pack()

def clear_results():
    # clear the previous search results
    for label in result_labels:
        label.destroy()
    # for widget in results_text_widgets:
    #     widget.destroy()
    # for label in blank_labels:
    #     label.destroy()
    # blank_labels.clear()
        

# implement search functionality
def search():
    # clear the previous search results
    clear_results()

    # create new result labels and text widgets for the search results
    search_term = search_bar.get().lower()
    found = False
    results = []
    for item in data:
        if search_term in item.lower():
            results.append(item)
            found = True
    if found:
        for result in results:
    
            # create an image label widget with height 5 and width 5
            image_label = tk.Label(search_window, height=5, width=20, bg="white")
            image_label.pack()

            # create a label widget for displaying the search result message with double font size
            result_label = tk.Label(search_window, text=result, font=("papyrus", 16))
            result_label.pack()
            result_labels.append(result_label)


            # create new label widgets for displaying the selected dropdown values
            selected_year_label = tk.Label(search_window, text="Selected Year of Study: " + menu1_var.get(), font=("papyrus", 12))
            selected_book_label = tk.Label(search_window, text="Selected Book Type: " + menu2_var.get(), font=("papyrus", 12))
            selected_subject_label = tk.Label(search_window, text="Selected Subject: " + menu3_var.get(), font=("papyrus", 12))

            # add the selected dropdown value labels to the search results section
            selected_year_label.pack()
            selected_book_label.pack()
            selected_subject_label.pack()

            # create a text widget for displaying the search results with the same font size as the result label
            # results_text = tk.Text(search_window, height=1, font=result_label.cget('font'))
            # results_text.configure(width=30)
            # results_text.pack()
            # results_text.insert(tk.END, result)
            # results_text_widgets.append(results_text)

            # add event binding to the image label to open a new window and display the search result data
            image_label.bind("<Button-1>", lambda event, data=result: show_result_data(data))

          
    else:
        result_label = tk.Label(search_window, text="Not found", font=("Helvetica", 16))
        result_label.pack()
        result_labels.append(result_label)

# function to show the search result data in a new window
def show_result_data(data):
    # create a new window
    result_window = tk.Toplevel(search_window)
    result_window.title("Result Data")
    result_window.geometry("900x600")
    result_window.configure(bg="Yellow")

    # create a label to display the data in the new window
    result_label = tk.Label(result_window, text=data, font=("papyrus", 16))
    result_label.pack()



# add the search functionality to the button
search_button.config(command=search)

# add the search functionality to the button
clear_button.config(command=clear_results)

# run the application
search_window.mainloop()        
