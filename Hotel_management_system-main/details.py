from os import stat
from tkinter import*
from PIL import Image, ImageTk #pip install pillow
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class Detailsroom:
    def __init__(self,root):
        self.root=root
        self.root.title("Hostel Management System")
        self.root.geometry("1121x452+234+243")

        ################ Title ##################
        lbl_title = Label(self.root,text="ROOMBOOKING DETAILS",font=("times new roman",18,"bold"),bg="blue",fg="white",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1121,height=35)

        ################## Logo ######################
        img2 = Image.open("clg-logo.jpeg")
        img2 = img2.resize((100,35),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg = Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=100,height=35)

        ################ LABEL FRAME ###################
        lblFrameLeft=LabelFrame(self.root,bd=2,relief=RIDGE,text="NEW ROOM ADD",font=("times new roman",12,"bold"),padx=2)
        lblFrameLeft.place(x=5,y=40,width=460,height=350)

        ############## FLOOR #################
        lbl_contact = Label(lblFrameLeft,text="Contact ",font=("arial",10,"bold"),padx=2,pady=6)
        lbl_contact.grid(row=0,column=0,sticky=W)
        
        self.var_contact=StringVar()
        entry_contact = ttk.Entry(lblFrameLeft,textvariable=self.var_contact,width=20,font=("arial",11,"bold"),state=DISABLED)
        entry_contact.grid(row=0,column=1,sticky=W)

        ############## ROOM NUMBER #################
        lbl_check_out= Label(lblFrameLeft,text="Check Out. ",font=("arial",10,"bold"),padx=2,pady=6)
        lbl_check_out.grid(row=2,column=0,sticky=W)
        
        self.var_check_out=StringVar()
        entry_check_out = ttk.Entry(lblFrameLeft,textvariable=self.var_check_out,width=20,font=("arial",11,"bold"))
        entry_check_out.grid(row=2,column=1,sticky=W)

        ############## ROOM TYPE #################
        lbl_room_TYPE= Label(lblFrameLeft,text="Room Type. ",font=("arial",10,"bold"),padx=2,pady=6)
        lbl_room_TYPE.grid(row=3,column=0,sticky=W)
        
        self.var_room_type=StringVar()
        entry_room_TYPE = ttk.Entry(lblFrameLeft,textvariable=self.var_room_type,width=20,font=("arial",11,"bold"))
        entry_room_TYPE.grid(row=3,column=1,sticky=W)

        ###################################################################################################################

        ############## FLOOR #################
        lbl_check_in= Label(lblFrameLeft,text="Check In ",font=("arial",10,"bold"),padx=2,pady=6)
        lbl_check_in.grid(row=1,column=0,sticky=W)
        
        self.var_check_in=StringVar()
        entry_check_in = ttk.Entry(lblFrameLeft,textvariable=self.var_check_in,width=20,font=("arial",11,"bold"))
        entry_check_in.grid(row=1,column=1,sticky=W)

        ############## ROOM NUMBER #################
        lbl_room_no= Label(lblFrameLeft,text="Room No. ",font=("arial",10,"bold"),padx=2,pady=6)
        lbl_room_no.grid(row=4,column=0,sticky=W)
        
        self.var_room_no=StringVar()
        entry_room_no = ttk.Entry(lblFrameLeft,textvariable=self.var_room_no,width=20,font=("arial",11,"bold"))
        entry_room_no.grid(row=4,column=1,sticky=W)

        ############## ROOM TYPE #################
        # lbl_room_TYPE= Label(lblFrameLeft,text="ROOM TYPE. ",font=("arial",10,"bold"),padx=2,pady=6)
        # lbl_room_TYPE.grid(row=2,column=0,sticky=W)
        
        # self.var_room_type=StringVar()
        # entry_room_TYPE = ttk.Entry(lblFrameLeft,textvariable=self.var_room_type,width=20,font=("arial",11,"bold"))
        # entry_room_TYPE.grid(row=2,column=1,sticky=W)

        #####################################################################################################################

        ############## BUTTONS ##############
        btn_frame = Label(lblFrameLeft,bd=2,relief=RIDGE)
        btn_frame.place(x=15,y=200,width=412,height=32)

        btn_add = Button(btn_frame,text="ADD",command=self.add_data,font=("arial",10,"bold"),bg="blue",fg="white",width=10)
        btn_add.grid(row=0,column=0,padx=5)

        btn_update = Button(btn_frame,text="UPDATE",command=self.update,font=("arial",10,"bold"),bg="blue",fg="white",width=10)
        btn_update.grid(row=0,column=1,padx=5)

        btn_delete = Button(btn_frame,text="DELETE",command=self.dat_Delete,font=("arial",10,"bold"),bg="blue",fg="white",width=10)
        btn_delete.grid(row=0,column=2,padx=5)

        btn_reset = Button(btn_frame,text="RESET",command=self.reset,font=("arial",10,"bold"),bg="blue",fg="white",width=10)
        btn_reset.grid(row=0,column=3,padx=5)

        ############## TABLE FRAME SEARCH ###############        
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("times new roman",12,"bold"),padx=2)
        table_frame.place(x=500,y=40,width=680,height=350)

        ############################3

        lblsearchby = Label(table_frame,text="Search By Contact No. :",font=("arial",10,"bold"),bg="red",fg="white")
        lblsearchby.grid(row=0,column=0,sticky=W,padx=4)

        self.search_var = StringVar()

        # combo_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("arial",10,"bold"),width=12,state="readonly")
        # combo_search["value"]=("MOBILE")
        # combo_search.current(0)
        # combo_search.grid(row=0,column=1,padx=4)

        self.txt_search = StringVar()
        entry_search = ttk.Entry(table_frame,textvariable=self.txt_search,width=29,font=("arial",11,"bold"))
        entry_search.grid(row=0,column=1,padx=4)

        btn_search = Button(table_frame,text="SEARCH",command=self.search_data,font=("arial",10,"bold"),bg="blue",fg="white",width=10)
        btn_search.grid(row=0,column=2,padx=5)

        btn_showall = Button(table_frame,text="SHOW ALL!!",command=self.fetch_data,font=("arial",10,"bold"),bg="blue",fg="white",width=10)
        btn_showall.grid(row=0,column=3,padx=5)

        ##########################33333333333

        details_table = Label(table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=34,width=674,height=350)

        Scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(details_table,columns=("CONTACT"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)

        Scroll_x.config(command=self.room_table.xview)
        Scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("CONTACT",text="Student Contacts")
        # self.room_table.heading("CHECK IN",text="CHECK IN")
        # self.room_table.heading("CHECK OUT",text="CHECK OUT")
        # self.room_table.heading("ROOM TYPE",text="ROOM TYPE")
        # self.room_table.heading("ROOM NO",text="ROOM NO.")

        self.room_table["show"]="headings"

        self.room_table.column("CONTACT",width=100)
        # self.room_table.column("CHECK IN",width=100)
        # self.room_table.column("CHECK OUT",width=100)
        # self.room_table.column("ROOM TYPE",width=100)
        # self.room_table.column("ROOM NO",width=100)

        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_contact.get()=="" or self.var_room_type.get()=="":
            messagebox.showerror("Error","ALL FIELDS ARE REQUIRED!!!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="nopassw",database="ankur")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s)",(self.var_contact.get(),self.var_check_in.get(),self.var_check_out.get(),self.var_room_type.get(),self.var_room_no.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","New Room added succeccfully!!!",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="nopassw",database="ankur")
        my_cursor = conn.cursor()
        my_cursor.execute("Select MOBILE from customer")
        rows = my_cursor.fetchall()
        if len(rows)!= 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    def search_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="nopassw",database="ankur")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer where MOBILE LIKE '%"+str(self.txt_search.get())+"%'")
        # my_cursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows_featch = my_cursor.fetchall()
        if len(rows_featch)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows_featch:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()   

    def get_cursor(self,event=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]

        self.var_contact.set(row[0]),
        self.var_check_in.set(row[1]),
        self.var_check_out.set(row[2]),
        self.var_room_type.set(row[3]),
        self.var_room_no.set(row[4])
        

    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter Details",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="nopassw",database="ankur")
            my_cursor = conn.cursor()
            my_cursor.execute("update room set CONTACT=%s, CHECK_IN=%s, CHECK_OUT=%s,  ROOM_TYPE=%s where ROOM=%s",(self.var_contact.get(),self.var_check_in.get(),self.var_check_out.get(),self.var_room_type.get(),self.var_room_no.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","New Room details has been updated sucessfully",parent=self.root)

    def dat_Delete(self):
        dat_Delete = messagebox.askyesno("Hostel Management System,","Do you want to remove this room detail",parent=self.root)
        if dat_Delete>0:
            conn = mysql.connector.connect(host="localhost",username="root",password="nopassw",database="ankur")
            my_cursor = conn.cursor()
            query = "delete from room where ROOM=%s"
            value = (self.var_room_no.get(),)
            my_cursor.execute(query,value)
        else:
            if not dat_Delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_contact.set(""),
        self.var_room_no.set(""),
        self.var_room_type.set("")





if __name__ == "__main__":
    root=Tk()
    Obj=Detailsroom(root)
    root.mainloop()
