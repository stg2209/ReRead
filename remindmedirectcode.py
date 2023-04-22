from tkinter import *
import smtplib 
# import testsigninpage as ts

import mysql.connector

# Establish a database connection
cnx = mysql.connector.connect(host = 'localhost' , user='root', password='', database='reread')

# Create a cursor object to execute SQL queries
cursor = cnx.cursor()

# # Execute a SELECT query
query = "SELECT * FROM mytable1"
cursor.execute(query)

# Retrieve the data
data = cursor.fetchall()

# Close the database connection
cursor.close()
cnx.close()

# Use the data in an if condition
for row in data:
    if row[0] == "anish111" and row[1] == "Second":
        
        try:
            username = '2021.anish.mayekar@ves.ac.in'
            password = 'uijtjlxbtzptrkfo'
            to = '2021.anish.mayekar@ves.ac.in'
            subject = f'Hello {username} you have reveive one mail from reread'
            body = 'This is the body of the mail'
            
            finalMessage = 'Subject: {}\n\n{}'.format(subject,body)
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(username,password)
            server.sendmail(username,to,finalMessage)
            print("Message send successfully")
        except:
            print("Errror occur while sending mail")

    else:
        print("Not found ")



