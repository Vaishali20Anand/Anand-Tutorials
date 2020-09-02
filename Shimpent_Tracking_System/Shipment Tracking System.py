
import tkinter as tk
from tkinter import *
import sqlite3
from tkinter import ttk
from tkinter import messagebox


class Main:
    def __init__(self):
        self.root = Tk()
        # self.root.state('zoom')
        self.root.attributes('-fullscreen', True)
        w, h = self.root.winfo_reqwidth(), self.root.winfo_reqheight()
        self.root.geometry("%dx%d+0+0" % (w, h))
        Label(self.root,text="Select which of the following you want to be :", font='Robort 40 bold').place(x=20, y=150)
        tk.Button(self.root,text='Admin',font='Robort 22 bold',fg='Black',bg='White',width=19,padx=10,borderwidth=0,
                  command=self.admin).place(x=150, y=300)
        tk.Button(self.root,text='User',font='Robort 22 bold',fg='Black',bg='White',width=19,padx=10,borderwidth=0,
                  command=self.user).place(x=550, y=300)
        tk.Button(self.root,text='Help',font='Robort 22 bold',fg='Black',bg='White',width=19,padx=10,borderwidth=0,
                  command=self.help).place(x=950, y=300)
        tk.Button(self.root,text='Quit',font='Robort 22 bold',fg='Black',bg='White',width=19,padx=10,borderwidth=0,
                  command=self.quit).place(x=550, y=600)
        self.root.title('Courier Tracking System')
        self.root.mainloop()

    def quit(self):
        self.root.destroy()

    def admin(self):
        self.root.destroy()
        self.root = Tk()
        # self.root.state('zoom')
        self.root.attributes('-fullscreen', True)
        w, h = self.root.winfo_reqwidth(), self.root.winfo_reqheight()
        self.root.geometry("%dx%d+0+0" % (w, h))
        self.USERNAME = StringVar()
        self.PASSWORD = StringVar()
        self.lbl_title = Label(text = "ADMIN   LOGIN", font=('Robort', 30,'bold'))
        self.lbl_title.place(x=500,y=100)
        self.lbl_username = Label(text = "Username:", font=('Robort', 15,'bold'),bd=4)
        self.lbl_username.place(x=500,y=230)
        self.lbl_password = Label(text = "Password :", font=('Robort', 15,'bold'),bd=3)
        self.lbl_password.place(x=500, y=330)
        self.lbl_text = Label()
        self.lbl_text.place(x=450,y=500)
        self.lbl_text.grid_propagate(0)
        self.username = Entry(textvariable=self.USERNAME, font=(14), bg='white',bd=6)
        self.username.place(x=650, y=230,)
        self.password = Entry(textvariable=self.PASSWORD, show="*", font=(14),bg='white',bd=6)
        self.password.place(x=650, y=330)
        self.password.place(x=650, y=330)
        self.btn_login = Button(text="Login", font=('Robort 15 bold'),width=25, bg='white', command=self.Login)
        self.btn_login.place(x=400,y=400)
        self.btn_back = Button(text="Back", font=('Robort 15 bold'),width=25, bg='white', 
                        command= self.back)
        self.btn_back.place(x=800,y=400)
        self.root.title('Admin Login')
    
    def loginDatabase(self):
        self.conn_admin = sqlite3.connect("admin.db")
        self.cursor_admin = self.conn_admin.cursor()
        self.cursor_admin.execute("CREATE TABLE IF NOT EXISTS `login` (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")
        self.cursor_admin.execute("SELECT * FROM `login` WHERE `username` = 'admin' AND `password` = 'admin'")
        if self.cursor_admin.fetchone() is None:
            self.cursor_admin.execute("INSERT INTO `login` (username, password) VALUES('admin', 'admin')")
            self.conn_admin.commit()

    def shipmentDatabase(self):
        # global conn_user, cursor_user
        self.conn_user = sqlite3.connect("user.db")
        self.cursor_user = self.conn_user.cursor()
        self.cursor_user.execute("CREATE TABLE IF NOT EXISTS `shipment` (shipid TEXT, date TEXT, loc TEXT)")
        self.cursor_user.execute("SELECT * FROM `shipment` WHERE `shipid` = 'abc'")
        if self.cursor_user.fetchone() is None:
            self.cursor_user.execute("INSERT INTO `shipment` (shipid, date, loc) VALUES('abc', '23-08-2020', 'Kanpur')")
            self.conn_user.commit()

    def Login(self,event=None):
        self.loginDatabase()
        if self.USERNAME.get() == "" or self.PASSWORD.get() == "":
            messagebox.showerror("Incomplete Data!","Please complete the required field!")
        else:
            self.cursor_admin.execute("SELECT * FROM `login` WHERE `username` = ? AND `password` = ?", (self.USERNAME.get(), self.PASSWORD.get()))
            if self.cursor_admin.fetchone() is not None:
                self.root.destroy()
                Admin()
            else:
                messagebox.showwarning("Error!","Invalid username or password.")
                self.USERNAME.set("")
                self.PASSWORD.set("")
        self.cursor_admin.close()
        self.conn_admin.close()
    
    def shipCheck(self):
        self.shipmentDatabase()
        if self.SHIPMENTID.get() == "":
            messagebox.showerror("Error", "Please complete the required field!")
        else:
            self.cursor_user.execute("SELECT * FROM `shipment` WHERE `shipid` = ?", [(self.SHIPMENTID.get())])
            if self.cursor_user.fetchone() is not None:
                self.showdata()
            else:
                messagebox.showwarning("Error 404","Shipment not Found")
                self.SHIPMENTID.set("")
        self.cursor_user.close()
        self.conn_user.close()



    def back(self):
        self.root.destroy()
        Main()

    def help(self):
        self.root.destroy()
        self.root = Tk()
        # self.root.state('zoom')
        self.root.attributes('-fullscreen', True)
        w, h = self.root.winfo_reqwidth(), self.root.winfo_reqheight()
        self.root.geometry("%dx%d+0+0" % (w, h))
        self.lbl_title = Label(text = "ABOUT", font=('Robort', 40,'bold'))
        self.lbl_title.place(x=500,y=100)   
        self.lbl_title = Label(text = "This is a Courier Tracking System. You can track your shipment and know information about it though ", font=('Robort', 20))
        self.lbl_title.place(x=20,y=250)
        self.lbl_title = Label(text = "this interface.You just need you shipment ID to get required information about your shipment. ", font=('Robort', 20))
        self.lbl_title.place(x=20,y=290)
        self.lbl_title = Label(text = "The admin is responsible to update the data regarding your shipment so that user gets the exact.", font=('Robort', 20))
        self.lbl_title.place(x=20,y=330)
        self.lbl_title = Label(text = "information", font=('Robort', 20))
        self.lbl_title.place(x=20,y=370)
        tk.Button(text='Back',font='Robort 22 bold',fg='Black',bg='White',width=19,padx=10,borderwidth=0,
                  command=self.back).place(x=600, y=500)
        tk.Button(text='Quit',font='Robort 22 bold',fg='Black',bg='White',width=19,padx=10,borderwidth=0,
                  command=self.quit).place(x=600, y=600)
        self.root.title('Help')

    def user(self):
        self.root.destroy()
        self.root = Tk()
        # self.root.state('zoom')
        self.root.attributes('-fullscreen', True)
        w, h = self.root.winfo_reqwidth(), self.root.winfo_reqheight()
        self.root.geometry("%dx%d+0+0" % (w, h))
        tk.Label(text='Enter Shipment ID : ',font=('Robort', 30,'bold')).place(x=200,y=100)
        self.SHIPMENTID = StringVar()
        self.ShipmentID = Entry(textvariable=self.SHIPMENTID, font=(14), bg='white',bd=6)
        self.ShipmentID.place(x=650, y=110,)
        tk.Button(text='Back',font='Robort 22 bold',fg='Black',bg='White',width=19,padx=10,borderwidth=0,
                  command=self.back).place(x=200,y=500)
        tk.Button(text='Submit',font='Robort 22 bold',fg='Black',bg='White',width=19,padx=10,borderwidth=0,
                command=self.shipCheck).place(x=600, y=500)
        tk.Button(text='Quit',font='Robort 22 bold',fg='Black',bg='White',width=19,padx=10,borderwidth=0,
                command=self.quit).place(x=1000, y=500)
        self.root.title('User Block')
    
    def showdata(self):
        self.head_list = ("SHIPMENT ID", "DATE", "LOCATION")
        self.trees=self.create_tree(self.root,self.head_list)
        self.trees.place(x=600,y=200)
        conn=sqlite3.connect('user.db')
        bid = self.SHIPMENTID.get()
        # sid=self.astudentt.get()
        try:
            c=conn.execute("select * from shipment where shipid=?",(bid,))
            d=c.fetchall()
            if len(d)!=0:
                for row in d:
                    self.trees.insert("",END,values=row)
            else:
                messagebox.showinfo("Error","Data not found.")
            conn.commit()
        except Exception:
            messagebox.showinfo("Error",".............!")
        conn.close()

    def create_tree(self,plc,lists):
        self.tree = ttk.Treeview(plc,height=5,column=(lists),show='headings')
        n=0
        while n is not len(lists):
            self.tree.heading("#"+str(n+1),text=lists[n])
            self.tree.column(""+lists[n],width=100)
            n=n+1
        return self.tree




class Admin:
    def __init__(self):
        self.root = Tk()
        self.root.title('Admin Block')
        # self.root.state('zoomed')
        self.root.attributes('-fullscreen', True)
        w, h = self.root.winfo_reqwidth(), self.root.winfo_reqheight()
        self.root.geometry("%dx%d+0+0" % (w, h))
        tk.Button(self.root,text='Insert a shipment',font='Robort 22 bold',fg='Black',bg='White',width=19,padx=10,borderwidth=0,
                  command=self.addShipment).place(x=12, y=100)
        tk.Button(self.root,text='Remove a shipment',font='Robort 22 bold',fg='Black',bg='White',width=19,padx=10,borderwidth=0,
                  command=self.removeShipment).place(x=12, y=200)
        tk.Button(self.root,text='Update a shipment',font='Robort 22 bold',fg='Black',bg='White',width=19,padx=10,borderwidth=0,
                  command=self.updateShipment).place(x=12, y=300)
        tk.Button(self.root,text='Main menu',font='Robort 22 bold',fg='Black',bg='White',width=19,padx=10,borderwidth=0,
                  command=self.back).place(x=12, y=500)
        tk.Button(self.root,text='QUIT',font='Robort 22 bold',fg='Black',bg='White',width=19,padx=10,borderwidth=0,
                  command=self.quit).place(x=12, y=700)
        self.root.mainloop()
    
    def quit(self):
        self.root.destroy()

    def back(self):
        self.root.destroy()
        Main()

    def addShipment(self):
        self.add_shipmentid = StringVar()
        self.add_date = StringVar()
        self.add_location = StringVar()
        self.f1=Frame(self.root,height=500,width=650)
        self.f1.place(x=500,y=100)
        Label(self.f1,text='Shipment ID : ',font='Robort 12 bold',fg='black',pady=1).place(x=50,y=50)
        Entry(self.f1,width=45,bg='white',fg='black',textvariable=self.add_shipmentid).place(x=400,y=50)
        Label(self.f1,text='Date(in dd-mm-yyyy format) : ',font='Robort 12 bold',fg='black',pady=1).place(x=50,y=100)
        Entry(self.f1,width=45,bg='white',fg='black',textvariable=self.add_date).place(x=400,y=100)
        Label(self.f1,text='Location : ',font='Robort 12 bold',fg='black',pady=1).place(x=50,y=150)
        Entry(self.f1,width=45,bg='white',fg='black',textvariable=self.add_location).place(x=400,y=150)
        self.f1.grid_propagate(0)
        Button(self.f1,text='Add',font='Robort 10 bold',fg='black',bg='white',width=15,bd=3, command=self.adddata).place(x=150,y=200)
    
    def removeShipment(self):
        self.remove_shipmentid = StringVar()
        self.f1=Frame(self.root,height=500,width=650)
        self.f1.place(x=500,y=100)
        Label(self.f1,text='Shipment ID : ',font='Robort 12 bold',fg='black',pady=1).place(x=50,y=50)
        Entry(self.f1,width=45,bg='white',fg='black',textvariable=self.remove_shipmentid).place(x=200,y=50)
        self.f1.grid_propagate(0)
        Button(self.f1,text='Remove',font='Robort 10 bold',fg='black',bg='white',width=15,bd=3,command=self.deletedata).place(x=150,y=200)
    
    def updateShipment(self):
        self.update_shipmentid = StringVar()
        self.update_date = StringVar()
        self.update_location = StringVar()
        self.f1=Frame(self.root,height=500,width=650)
        self.f1.place(x=500,y=100)
        Label(self.f1,text='Shipment ID : ',font='Robort 12 bold',fg='black',pady=1).place(x=50,y=50)
        Entry(self.f1,width=45,bg='white',fg='black',textvariable=self.update_shipmentid).place(x=400,y=50)
        Label(self.f1,text='Date(in dd-mm-yyyy format) :',font='Robort 12 bold',fg='black',pady=1).place(x=50,y=100)
        Entry(self.f1,width=45,bg='white',fg='black',textvariable=self.update_date).place(x=400,y=100)
        Label(self.f1,text='Location : ',font='Robort 12 bold',fg='black',pady=1).place(x=50,y=150)
        Entry(self.f1,width=45,bg='white',fg='black',textvariable=self.update_location).place(x=400,y=150)
        self.f1.grid_propagate(0)
        Button(self.f1,text='Update',font='Robort 10 bold',fg='black',bg='white',width=15,bd=3, command=self.updatedata).place(x=150,y=200)
    
    def adddata(self):
        a = self.add_shipmentid.get()
        b = self.add_date.get()
        c = self.add_location.get()

        connection = sqlite3.connect('user.db')
        cu = connection.cursor()
        
        if cu.execute("SELECT * FROM `shipment` WHERE `shipid` = ?", [(a)]):
            if cu.fetchone() is not None:
                messagebox.showinfo("Error", "Shipment already exists")
                self.add_shipmentid.set("")
            else:
                if (a and b and c) == "":
                    messagebox.showinfo("Error", "Field can not be empty.....!")
                else:
                    cu.execute("INSERT INTO shipment (shipid, date, loc) VALUES(?,?,?)",(a,b,c))
                    connection.commit()
                    messagebox.showinfo("Success","Shipment added successfully")
                    self.add_shipmentid.set("")
                    self.add_location.set("")
                    self.add_date.set("")
        connection.close()

    def deletedata(self):
        a = self.remove_shipmentid.get()
        connection = sqlite3.connect('user.db')
        cu = connection.cursor()
        if a == "":
            messagebox.showinfo("Error", "Field can not be empty.....!")
        elif cu.execute("SELECT * FROM `shipment` WHERE `shipid` = ?", [(a)]):
            if cu.fetchone() is not None:
                sql = 'DELETE FROM shipment WHERE shipid=?'
                cu.execute(sql, (a,))
                connection.commit()
                messagebox.showinfo("Success", "Shipment deleted successfully")
                self.remove_shipmentid.set("")
            else:
                messagebox.showinfo("Error", "Shipment not exists")
        connection.close()

    def updatedata(self):
        a = self.update_shipmentid.get()
        b = self.update_date.get()
        c = self.update_location.get()
        connection = sqlite3.connect('user.db')
        cu = connection.cursor()
        if (a and b and c) == "":
            messagebox.showinfo("Error","Field can not be empty.....!")
        elif cu.execute("SELECT * FROM `shipment` WHERE `shipid` = ?", [(a)]):
            if cu.fetchone() is not None:
                if (a and b and c) != "":
                    cu.execute("UPDATE shipment SET date=?, loc=? WHERE shipid=?", (b,c,a))
                    connection.commit()
                    messagebox.showinfo("Success", "Shipment Updated successfully")
                    self.update_shipmentid.set("")
                    self.update_date.set("")
                    self.update_location.set("")
            else:
                messagebox.showinfo("Error", "Shipment not exists")
        connection.close()


a = Main()