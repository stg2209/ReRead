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

# create a list to hold the result labels and text widgets
result_labels = []
results_text_widgets = []
blank_labels = []

# retrieve the data
data = ["Kumbhojkar", "kumbhojkar", "OS Notes", "COA Slides", "Computer Network PPt"]

# implement search functionality
def search():
    # clear the previous search results
    for label in result_labels:
        label.destroy()
    for widget in results_text_widgets:
        widget.destroy()
    for label in blank_labels:
        label.destroy()

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
            

            # create a blank label for spacing
            blank_label = tk.Label(search_window, height=5)
            blank_label.pack()

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
            # # create a text widget for displaying the search results with the same font size as the result label
            # result_label.update()
            # results_text = tk.Text(search_window, height=1, font=result_label.cget('font'))
            # results_text.configure(width=30)
            # results_text.pack()
            # results_text_widgets.append(results_text)

            # add the blank label to the list
            blank_labels.append(blank_label)

    else:
        result_label = tk.Label(search_window, text="Not found", font=("Helvetica", 16))
        result_label.pack()
        result_labels.append(result_label)

# add the search functionality to the button
search_button.config(command=search)

# run the application
search_window.mainloop()        
