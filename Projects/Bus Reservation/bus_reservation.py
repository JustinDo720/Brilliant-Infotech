import tkinter as tk
from tkinter import messagebox 
from tkinter import ttk
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

# Bus Reservation Window 
class BusReservation:
    def __init__(self, root, username):
        self.root = root 
        self.root.title('Bus Reservation List')
        self.root.geometry('550x550')

        # User information 
        self.username = username 

        # Must be a treeview for tables
        self.tree = ttk.Treeview(root, columns=('bus_num', 'time', 'fare'), show='headings')
        self.tree.heading('bus_num', text='Bus Number')
        self.tree.heading('time', text='Timing')
        self.tree.heading('fare', text='Fare')

        # Adding Bus Reservation to the table
        query = """
            SELECT *
            FROM bus_res_schedule     
        """
        cur.execute(query)
        results = cur.fetchall()

        for result in results:
            self.tree.insert('', 'end', values=result)
        self.tree.pack(expand=True)
        self.submit_selection = tk.Button(root, text='Select Reservation', command=self.row_sel)
        self.submit_selection.pack()
    
    def row_sel(self):
        item = self.tree.selection()
        if item:
            item_values = self.tree.item(item, 'values')
            user_win = tk.Tk()
            UserBusReservation(user_win, self.username, item_values)

# Showing Specific User Bus Reservation 

class UserBusReservation:
    def __init__(self, root, username, res_details):
        self.root = root 
        self.root.title(f"{username}'s Bus Reservation")
        self.root.geometry('550x550')

        self.res_details = res_details
        print(res_details)

        self.user_label = tk.Label(root, text=f"{username.title()}")
        self.user_label.grid(row=0, columnspan=2)

        self.bus_num_label = tk.Label(root, text=f"Bus Number: {res_details[0]}")
        self.bus_num_label.grid(row=1,column=0)

        self.bus_time_label = tk.Label(root, text=f"Bus Time: {res_details[1]}")
        self.bus_time_label.grid(row=1,column=1)

        self.bus_fare_label = tk.Label(root, text=f"Bus Fare: {res_details[2]}")
        self.bus_fare_label.grid(row=1,column=2)


# Registration Form 
class RegistrationForm:
    def __init__(self, root):
        self.root = root 
        self.root.title('Registration Form')
        self.root.geometry('250x250')

        # Create Labels and input fields for Username and Password
        self.u_name_label = tk.Label(root, text="Username")
        self.u_name_label.grid(row=0, column=0)

        self.entry_username = tk.Entry(root)
        self.entry_username.grid(row=0, column=1)

        self.pass_label = tk.Label(root, text="Password")
        self.pass_label.grid(row=1, column=0)

        # show='*' will hide the entry for privacy 
        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.grid(row=1, column=1)

        # Create label and submit button
        self.submit_button = tk.Button(root, text="Register", command=self.submit_form)
        self.submit_button.grid(row=3, column=0, columnspan=2)
    
    def submit_form(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        cur.execute(
            """
                INSERT INTO bus_res_login(username, password)
                VALUES (%s, %s);
            """,
            (username, password)
        )
        conn.commit()
        messagebox.showinfo("Success", "User account has been created")
        self.root.destroy()
        

# Class for main application window
class MainApplication: 
    def __init__(self, root):
        self.root = root 
        self.root.title('Bus Reservation')
        self.root.geometry('300x300')

        # Login form 
        self.login_username_label = tk.Label(root, text='Username')
        self.login_username_label.grid(row=0,column=0)

        self.login_username_entry = tk.Entry(root)
        self.login_username_entry.grid(row=0, column=1)

        self.login_username_pass = tk.Label(root, text='Password')
        self.login_username_pass.grid(row=1,column=0)

        self.login_pass_entry = tk.Entry(root, show='*')
        self.login_pass_entry.grid(row=1, column=1)

        self.login_button = tk.Button(root, text='Login', command=self.login)
        self.login_button.grid(row=2, columnspan=2)

        self.open_reg_form = tk.Button(self.root, text='Register Here', command=self.open_reg)
        self.open_reg_form.grid(row=3, columnspan=2)

    def open_reg(self):
        reg_window = tk.Tk()
        # Feed in our newly created window as the root of our Registration Form 
        RegistrationForm(reg_window) 

    def login(self):
        
        query = """
            SELECT username,password
            FROM bus_res_login
            WHERE username = %s 
            AND password = %s
        """

        cur.execute(query, (self.login_username_entry.get(), self.login_pass_entry.get()))
        # Grab one result from the query 
        result = cur.fetchone()
        
        if result:
            res_win = tk.Tk()
            BusReservation(res_win, self.login_username_entry.get())

root = tk.Tk()
main_app = MainApplication(root)
root.mainloop()