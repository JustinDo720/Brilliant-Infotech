import tkinter as tk
import mysql.connector as mysql
import os

# Connecting to our database

conn = mysql.connect(
    host=os.environ.get('MYSQL_LOCAL_HOST'), 
    user=os.environ.get('MYSQL_LOCAL_USER'), 
    password=os.environ.get('MYSQL_LOCAL_PASSWORD'), 
    db='bus_reservation'
)

# Creating that cursor 
cur = conn.cursor()



def submit_form():
    username = entry_username.get()
    password = entry_password.get()

    cur.execute(
        """
            INSERT INTO bus_res_login(username, password)
            VALUES (),
        """
    )
    print(username, password)



# User Registration and Login Form 

root = tk.Tk()
root.title('Registration Form')
root.geometry('250x250')

# Create Labels and input fields for Username and Password
u_name_label = tk.Label(root, text="Username")
u_name_label.grid(row=0, column=0)

entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1)

pass_label = tk.Label(root, text="Password")
pass_label.grid(row=1, column=0)

# show='*' will hide the entry for privacy 
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1)

# Create label and submit button
submit_button = tk.Button(root, text="Register", command=submit_form)
submit_button.grid(row=3, column=0, columnspan=2)

root.mainloop()