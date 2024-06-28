from tkinter import *
from PIL import Image, ImageTk
import random
from tkinter import ttk, messagebox
import sqlite3


class Pharmacy:
    def __init__(self, root):
        self.root = root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1535x790+-8+0")
        self.root.resizable(True,True)
        self.root.iconbitmap(r".\image\doc.ico")

        ##### ADDMED VARIABLE ######
        self.ref_variable = StringVar()
        self.addmed_variable = StringVar()

        ########## MEDICINE DEPARTMENT VARIABLE #######
        self.refno_var = StringVar()
        self.companyname_var = StringVar()
        self.typemed_var = StringVar()
        self.medicine_var = StringVar()
        self.lotno_var = StringVar()
        self.issuedt_var = StringVar()
        self.expdt_var = StringVar()
        self.uses_var = StringVar()
        self.sideeffect_var = StringVar()
        self.warning_var = StringVar()
        self.dosage_var = StringVar()
        self.price_var = StringVar()
        self.quantity_var = StringVar()
        self.banned_var = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()

        ######## title animation #########
        self.txt = "PHARMACY MANAGEMENT SYSTEM"
        self.count = 0
        self.text = ""
        self.color = ["thistle1"] #green
        self.heading = Label(self.root, text=self.txt, font=(
            "times new roman", 30, "bold"), bg='medium slate blue', fg="blue", bd=9, relief=RIDGE)
        self.heading.pack(side=TOP, fill= X)
        self.slider()
        self.heading_color()

        # lbltitle=Label(self.root,text=" PHARMACY MANAGEMENT SYSTEM",bd=11,relief=RIDGE
                            # ,bg='#7FFFD4',fg='#0020C2',font=('times new roman',35,'bold'),padx=2,pady=4)
        # lbltitle.pack(side=TOP,fill=X)

        ######### pharmacy logo label #######
        img1 = Image.open(r".\image\new.png")
        img1 = img1.resize((70, 45), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        b1 = Button(self.root, image=self.photoimg1,
                    borderwidth=0, bg='medium slate blue')
        b1.place(x=15, y=8)

        ###### Top Frame #####
        topframe = Frame(self.root, bg='medium slate blue', bd=10, relief=RIDGE, padx=20)
        topframe.place(x=0, y=62, width=1536, height=400)

        ########  down button frame #######
        down_buttonframe = Frame(
            self.root, bg='medium slate blue', bd=10, relief=RIDGE, padx=20)
        down_buttonframe.place(x=0, y=462, width=1536, height=60)

        ###### all buttons ######
        add_button = Button(down_buttonframe,command=self.addmedicine, text="Add Medicine"
        , font=(
            "arial", 12, "bold"), width=12, fg="white", bg="purple4", bd=3, relief=RIDGE, activebackground="Purple4", activeforeground="white")
        add_button.grid(row=0, column=0)

        update_button = Button(down_buttonframe, command=self.update_new,
         text="Update", font=(
            "arial", 13, "bold"), width=10, fg="white", bg="purple4", bd=3, relief=RIDGE, activebackground="Purple4", activeforeground="white")
        update_button.grid(row=0, column=1)

        delete_button = Button(down_buttonframe,command=self.clear_new, text="Delete", font=("arial", 13, "bold"), width=10,
                               fg="white", bg="purple4", bd=3, relief=RIDGE, activebackground="Purple4", activeforeground="white")
        delete_button.grid(row=0, column=2)

        reset_button = Button(down_buttonframe,command=self.reset, text="Reset",
         font=("arial", 13, "bold"), width=10,
                              fg="white", bg="purple4", bd=3, relief=RIDGE, activebackground="Purple4", activeforeground="white")
        reset_button.grid(row=0, column=3)

        exit_button = Button(down_buttonframe, command=self.root.quit,
         text="Exit", font=(
            "arial", 13, "bold"), width=10, fg="white", bg="purple4", bd=3, relief=RIDGE, activebackground="Purple4", activeforeground="white")
        exit_button.grid(row=0, column=4)

        search_by = Label(down_buttonframe, text="MODE :", font=(
            "times new roman", 15, "bold"), fg="thistle1", bg="medium slate blue", bd=3, padx=3)
        search_by.grid(row=0, column=5, sticky=W)

        
        self.search_combo = ttk.Combobox(down_buttonframe, textvariable=self.search_by, width=13, font=(
            "times new roman", 13, "bold"), state="readonly"
            )
        self.search_combo["values"] = ("Select a Mode", "Search By:Ref no","Search By:MedName","Search By:Lot","Sort By:Ascending","Sort By:Descending")
        self.search_combo.grid(row=0, column=6)
        self.search_combo.current(0)

        entry_button = Entry(down_buttonframe,textvariable =self.search_txt,bd = 3,relief=RIDGE,width=12, font=("times new roman", 13, "bold"))
        entry_button.grid(row=0, column=7)
        search_button = Button(down_buttonframe,command=self.search_data, text="Search",
         font=("arial", 13, "bold"), width=10,
                              fg="white", bg="purple4", bd=3, relief=RIDGE, activebackground="Purple4", activeforeground="white")
        search_button.grid(row=0, column=8)

        show_button = Button(down_buttonframe,command=self.fetch_new,
         text="show all", font=(
            "arial", 13, "bold"), width=10, fg="white", bg="purple4", bd=3, relief=RIDGE, activebackground="Purple4", activeforeground="white")
        show_button.grid(row=0, column=9)



        sort_button=Button(down_buttonframe,command=self.order_data,
         text="Sort", font=(
            "arial", 13, "bold"), width=7, fg="white", bg="purple4", bd=3, relief=RIDGE, activebackground="Purple4", activeforeground="white")
        sort_button.grid(row=0,column=10)


        remove1_button=Button(down_buttonframe,command=self.add,
         text="+", font=(
            "arial", 13, "bold"), width=5, fg="white", bg="purple4", bd=3, relief=RIDGE, activebackground="Purple4", activeforeground="white")
        remove1_button.grid(row=0,column=11)
        
        remove2_button=Button(down_buttonframe,command=self.remove,
         text="-", font=(
            "arial", 13, "bold"), width=5, fg="white", bg="purple4", bd=3, relief=RIDGE, activebackground="Purple4", activeforeground="white")
        remove2_button.grid(row=0,column=12)

        bellow_button = Button(down_buttonframe,command=self.bellow,text="Below level", font=(
        "arial", 13, "bold"), width=11, fg="white", bg="purple4", bd=3, relief=RIDGE, activebackground="Purple4", activeforeground="white")
        bellow_button.grid(row=0,column=13)


        ######## left small frame #######
        left_smallframe = LabelFrame(topframe, bg='medium slate blue', bd=10, relief=RIDGE,
                                     padx=20, text="Medicine Information", font=("arial", 13, "bold"), fg="white")
        left_smallframe.place(x=0, y=5, width=1000, height=350) #820

           #### labeling & entry box #########

        # 1

        ref_label = Label(left_smallframe, text="Reference No. :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="medium slate blue")
        ref_label.grid(row=0, column=0, sticky=W)
        conn = sqlite3.connect(database=r'.\pharmacy.db')
        my_cursor = conn.cursor()
        my_cursor.execute("select Ref_no from pharma")
        row=my_cursor.fetchall()
        
        self.ref_combo = ttk.Combobox(left_smallframe,textvariable=self.refno_var, width=22, font=(
            "arial", 13, "bold"), state="readonly")
        self.ref_combo["values"] =row
        self.ref_combo.grid(row=0, column=1)
        self.ref_combo.current(0)

        
        # 2

        company_label = Label(left_smallframe, text=" Company Name :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="medium slate blue")
        company_label.grid(row=1, column=0,sticky=W)
        conn = sqlite3.connect(database=r'.\pharmacy.db')
        my_cursor = conn.cursor()
        my_cursor.execute("select Ref_no from pharma")
        row=my_cursor.fetchall()
        
        self.company_entry = Entry(left_smallframe,textvariable=self.companyname_var,width=24, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.company_entry.grid(row=1, column=1)

          # 3
        type_label = Label(left_smallframe, text="Type Of Medicine :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="medium slate blue")
        type_label.grid(row=2, column=0, sticky=W)
        self.type_combo = ttk.Combobox(left_smallframe, textvariable=self.typemed_var,
        width=22, font=(
            "arial", 13, "bold"), state="readonly")
        self.type_combo["values"] = ( " Select  ", "Tablet", "Capsule", "Injection", "Ayurvedic", "Drops", "Inhales")
        self.type_combo.grid(row=2, column=1)
        self.type_combo.current(0)

        #4
        medname_label = Label(left_smallframe, text="Medicine Name  :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="medium slate blue")
        medname_label.grid(row=3, column=0,sticky=W)

        conn = sqlite3.connect(database=r'.\pharmacy.db')
        my_cursor = conn.cursor()
        my_cursor.execute("select Med_name from pharma")
        med=my_cursor.fetchall()

        self.medname_combo=ttk.Combobox(left_smallframe,textvariable=self.medicine_var,
        width=22,font=("arial",13,"bold"),state="readonly")
        self.medname_combo["values"]=med
        self.medname_combo.grid(row=3,column=1)
        self.medname_combo.current(0)

        #5
        lot_label = Label(left_smallframe, text=" Lot No.  :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="medium slate blue")
        lot_label.grid(row=4, column=0,sticky=W)
        self.lot_entry = Entry(left_smallframe,textvariable=self.lotno_var,
         width=24, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.lot_entry.grid(row=4, column=1)

        #6
        issue_label = Label(left_smallframe, text=" Issue Date  :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="medium slate blue")
        issue_label.grid(row=5, column=0,sticky=W)
        self.issue_entry = Entry(left_smallframe, textvariable=self.issuedt_var,
         width=24, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.issue_entry.grid(row=5, column=1)

        #7
        exp_label = Label(left_smallframe, text=" Expiry Date :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="medium slate blue")
        exp_label.grid(row=6, column=0,sticky=W)
        self.exp_entry = Entry(left_smallframe,textvariable=self.expdt_var,
         width=24, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.exp_entry.grid(row=6, column=1)

        #8
        use_label = Label(left_smallframe, text=" Uses :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="medium slate blue")
        use_label.grid(row=7, column=0,sticky=W)
        self.use_entry = Entry(left_smallframe,textvariable=self.uses_var,
         width=24, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.use_entry.grid(row=7, column=1)

        #9
        sideeffect_label = Label(left_smallframe, text=" Side Effect :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="medium slate blue")
        sideeffect_label.grid(row=8, column=0,sticky=W)
        self.sideeffect_entry = Entry(left_smallframe,textvariable=self.sideeffect_var,
         width=24, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.sideeffect_entry.grid(row=8, column=1)

        #10
        warn_label = Label(left_smallframe, text=" Prec & warning :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="medium slate blue")
        warn_label.grid(row=9, column=0,sticky=W)
        self.warn_entry = Entry(left_smallframe,textvariable=self.warning_var,
         width=24, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.warn_entry.grid(row=9, column=1)


        #11
        dosage_label = Label(left_smallframe, text=" Dosage :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="medium slate blue")
        dosage_label.grid(row=0, column=2,sticky=W)
        self.dosage_entry = Entry(left_smallframe,textvariable=self.dosage_var,
         width=24, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.dosage_entry.grid(row=0, column=3)

        #12
        price_label = Label(left_smallframe, text=" Tablet Price :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="medium slate blue")
        price_label.grid(row=1, column=2,sticky=W)
        self.price_entry = Entry(left_smallframe,textvariable=self.price_var,
         width=24, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.price_entry.grid(row=1, column=3)

        #13
        qt_label = Label(left_smallframe, text=" Tablet Quantity :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="medium slate blue")
        qt_label.grid(row=2, column=2,sticky=W)
        self.qt_entry = Entry(left_smallframe, textvariable=self.quantity_var,
         width=24, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.qt_entry.grid(row=2, column=3)

        #14
        banned_label = Label(left_smallframe, text=" Banned For  :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="medium slate blue")
        banned_label.grid(row=3, column=2,sticky=W)
        self.banned_entry = Entry(left_smallframe, textvariable=self.banned_var,
         width=24, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.banned_entry.grid(row=3, column=3)


            ######## image in left small frame #####
        # image 1
        self.bg = ImageTk.PhotoImage(file=r".\image\med.jpg")
        lbl_bg = Label(left_smallframe, image=self.bg)
        lbl_bg.place(x=395, y=155, width=200, height=150) #165y370
        # image 2
        self.bgg = ImageTk.PhotoImage(file=r".\image\medi.jpg")
        lbl_bgg = Label(left_smallframe, image=self.bgg)
        lbl_bgg.place(x=595, y=155, width=200, height=150) #165y570

        # save life label
        save_bgg = Label(left_smallframe, text="----------- Stay Home Stay Safe -----------",
                         font=("arial", 13, "bold"), bg='medium slate blue', fg="white")
        save_bgg.place(x=370, y=120, width=400)

        ############ right frame #########
        right_frame = LabelFrame(topframe, bg='medium slate blue', bd=10, relief=RIDGE, padx=5,
                                 text="New Medicine Add department", font=("arial", 13, "bold"), fg="white")
        right_frame.place(x=846, y=5, width=625, height=350) #452

          # image & label

        # image 1
        self.bg1 = ImageTk.PhotoImage(file=r".\image\co.jpg")
        lbl_bg1 = Label(right_frame, image=self.bg1)
        lbl_bg1.place(x=20, y=0, width=240, height=100) #0x

        #image

        # self.bg1 = ImageTk.PhotoImage(file=r".\image\inject.jpg")
        # lbl_bg1 = Label(right_frame, image=self.bg1)
        # lbl_bg1.place(x=20, y=0, width=240, height=100) #0x
        # #### label & entry in right frame ####
        # 1
        no_label = Label(right_frame, text="Reference No:", font=(
            "times new roman", 15, "bold"), bg="medium slate blue") #11
        no_label.place(x=270, y=10) #0x105y

        self.no_entry = Entry(right_frame, textvariable=self.ref_variable, width=17, font=(
            "times new roman", 15, "bold"), bg="white") #11 #w16
        self.no_entry.place(x=400, y=10) #100xny105

        # 2
        med_label = Label(right_frame, text="Med  Name:", font=(
            "times new roman", 15, "bold"), bg="medium slate blue") #11
        med_label.place(x=270, y=55) #0x130y

        self.med_entry = Entry(right_frame, textvariable=self.addmed_variable, width=17, font=(
            "times new roman", 15, "bold"), bg="white") #11w16
        self.med_entry.place(x=400, y=55)#100x130y


        #### in right frame small frame #####

        newframe = Frame(right_frame, bg='dark slate blue', bd=5, relief=RIDGE)
        # newframe.place(x=350, y=120, width=200, height=200) #x=256, y=160, width=150, height=150 
        newframe.place(x=350, y=120, width=200, height=180) #x=256, y=160, width=150, height=150 

          ###### button in this frame ###
        add_button = Button(newframe, command=self.AddMed, text="Add", font=("arial",13 , "bold"), width=18, fg="white", bg="Purple4",
                            bd=3, relief=RIDGE, activebackground="Purple4", activeforeground="white") #13w14
        add_button.grid(row=0, column=0)

        updatenew_button = Button(newframe,command=self.Update_med, text="Update", font=("arial", 13, "bold"), width=18, fg="white", bg="Purple4",
                                  bd=3, relief=RIDGE, activebackground="Purple4", activeforeground="white")
        updatenew_button.grid(row=1, column=0)

        delnew_button = Button(newframe, command=self.Delete_med,text="Delete", font=("arial", 13, "bold"), width=18, fg="white", bg="Purple4",
                               bd=3, relief=RIDGE, activebackground="Purple4", activeforeground="white")
        delnew_button.grid(row=2, column=0)

        clr_button = Button(newframe, text="Clear", command=self.clear_med, font=("arial", 13, "bold"), width=18,
                            fg="white", bg="Purple4", bd=3, relief=RIDGE, activebackground="Purple4", activeforeground="white")
        clr_button.grid(row=3, column=0)

        sort_button = Button(newframe, text="Sort", command=self.sortright, font=("arial", 13, "bold"), width=18,
                            fg="white", bg="Purple4", bd=3, relief=RIDGE, activebackground="Purple4", activeforeground="white")
        sort_button.grid(row=4, column=0)
        ##### scrollbar frame in right frame ####
        side_frame = Frame(right_frame, bd=4, relief=RIDGE, bg="dark slate blue")
        side_frame.place(x=20, y=110, width=300, height=200) #x=30, y=160, width=250, height=150

        ### scrollbar code ###

        sc_x = ttk.Scrollbar(side_frame, orient=HORIZONTAL)
        sc_y = ttk.Scrollbar(side_frame, orient=VERTICAL)
        self.medicine_table = ttk.Treeview(side_frame, column=(
            "ref", "medname"), xscrollcommand=sc_x.set, yscrollcommand=sc_y.set)

        sc_x.pack(side=BOTTOM, fill=X)
        sc_y.pack(side=RIGHT, fill=Y)

        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("ref", text="Ref")
        self.medicine_table.heading("medname", text="Medicine Name")

        self.medicine_table["show"] = "headings"
        self.medicine_table.pack(fill=BOTH, expand=1)

        self.medicine_table.column("ref", width=100)
        self.medicine_table.column("medname", width=100)

        self.medicine_table.bind("<ButtonRelease-1>", self.medget_cursor)
        self.fetch_datamed()

        ######### down frame #######
        down_frame = Frame(self.root, bg='dark slate blue', bd=10, relief=RIDGE)
        down_frame.place(x=0, y=522, width=1536, height=270) #212 #w1350

        ########## scrollbar in down frame ########
        scroll_frame = Frame(down_frame, bd=2, relief=RIDGE, bg="white")
        scroll_frame.place(x=0, y=0, width=1516, height=245)#192 #w1330

        ##### scrollbar code #####
        scroll_x = ttk.Scrollbar(scroll_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(scroll_frame, orient=VERTICAL)
        self.info_table = ttk.Treeview(scroll_frame, column=("ref no", "comp name", "type", "medi name", "lot no", "issue", "exp",
                                       "uses", "side effect", "warning", "dosage", "price", "product","ban"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.info_table.xview)
        scroll_y.config(command=self.info_table.yview)

        self.info_table.heading("ref no", text="Ref No.")
        self.info_table.heading("comp name", text="Company Name")
        self.info_table.heading("type", text="Type Of Medicine")
        self.info_table.heading("medi name", text="Medicine Name")
        self.info_table.heading("lot no", text="Lot No.")
        self.info_table.heading("issue", text="Issue Date")
        self.info_table.heading("exp", text="Expiry Date")
        self.info_table.heading("uses", text="Uses")
        self.info_table.heading("side effect", text="Side Effects")
        self.info_table.heading("warning", text="Prec & Warning")
        self.info_table.heading("dosage", text="Dosage")
        self.info_table.heading("price", text="Medicine Price")
        self.info_table.heading("product", text="Product Qt.")
        self.info_table.heading("ban", text="Banned For")

        self.info_table["show"] = "headings"
        self.info_table.pack(fill=BOTH, expand=1)

        self.info_table.column("ref no", width=100)
        self.info_table.column("comp name", width=100)
        self.info_table.column("type", width=100)
        self.info_table.column("medi name", width=100)
        self.info_table.column("lot no", width=100)
        self.info_table.column("issue", width=100)
        self.info_table.column("exp", width=100)
        self.info_table.column("uses", width=100)
        self.info_table.column("side effect", width=100)
        self.info_table.column("warning", width=100)
        self.info_table.column("dosage", width=100)
        self.info_table.column("price", width=100)
        self.info_table.column("product", width=100)
        self.info_table.column("ban", width=100)

        

        self.fetch_datamed()
        self.fetch_new()
        self.info_table.bind("<ButtonRelease-1>", self.get_cursor)

    ####### MEDICINE ADD FUNCTIONALITY  DECLARATION #######

    def AddMed(self):

        if self.ref_variable.get() == "" or self.addmed_variable.get() == "":
            messagebox.showerror("Error", "All fields are required")

        else:
            conn = sqlite3.connect(database=r'.\pharmacy.db')
            my_cursor = conn.cursor()
            sql = "Insert into pharma(Ref_no,Med_name) values(?,?)"
            val = (self.ref_variable.get(),
                self.addmed_variable.get())
            my_cursor.execute(sql,val)
            
            conn.commit()
            self.fetch_datamed()

            my_cursor.execute("select Ref_no from pharma")
            row_01= my_cursor.fetchall()
            self.ref_combo["values"]=('select',*row_01)

            my_cursor.execute("Select Med_name from pharma")
            row_02 = my_cursor.fetchall()
            self.medname_combo["values"] = ('Select',*row_02)
            conn.close()

            messagebox.showinfo("Success", "MEDICINE ADDED")

    def fetch_datamed(self):
        conn = sqlite3.connect(database=r'.\pharmacy.db')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from pharma")
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.medicine_table.delete(*self.medicine_table.get_children())

            for i in rows:
                self.medicine_table.insert("", END, values=i)

            conn.commit()
        conn.close()

    ###### for show data on click #####

    def medget_cursor(self, event=""):
        cursor_row = self.medicine_table.focus()
        content = self.medicine_table.item(cursor_row)
        row = content["values"]
        self.ref_variable.set(row[0])
        self.addmed_variable.set(row[1])

    def Update_med(self):
        if self.ref_variable.get() == "" or self.addmed_variable.get()=="":

            messagebox.showerror("Error", "Ref No. and med name is required")
        else:
        
            conn = sqlite3.connect(database=r'.\pharmacy.db')
            new_cursor = conn.cursor()
            sql = "Update pharma set MED_NAME=? where REF_NO=?"
            val = (self.addmed_variable.get(),self.ref_variable.get())
            new_cursor.execute(sql,val)
            sql2="Update pharma set REF_NO=? where MED_NAME=?"
            val2=(self.ref_variable.get(),self.addmed_variable.get())
            new_cursor.execute(sql2,val2)
            conn.commit()
            self.fetch_datamed()
            
            new_cursor.execute("Select Ref_no from pharma")
            combo1 = new_cursor.fetchall()
            self.ref_combo["values"] = ('Select',*combo1)

            new_cursor.execute("Select Med_name from pharma")
            combo2 = new_cursor.fetchall()
            self.medname_combo["values"] = ('Select',*combo2)
            messagebox.showinfo("Update", "Successfully Updated",
            )
            
            conn.close()
        





    def Delete_med(self):
        if self.ref_variable.get()=="":
            messagebox.showerror("Error","Ref no is required")
        else:

            try:
                conn=sqlite3.connect(database=r'.\pharmacy.db')
                my_cursor=conn.cursor()
                sql = "Delete from pharma where Ref_no=? "
                val = (self.ref_variable.get(),)
                my_cursor.execute(sql,val)
                conn.commit()
                messagebox.showinfo("Delete","Successfully Deleted")
                self.fetch_datamed()
            except Exception as e:
                messagebox.showerror("Error",f"Error due to:{str(e)}")
        conn.close()

        

    def clear_med(self):
        self.ref_variable.set("")
        self.addmed_variable.set("")

    def sortright (self):
        conn=sqlite3.connect(database=r'.\pharmacy.db')
        new_cursor=conn.cursor()
        sql = "Select * from pharma order by Med_name"
        new_cursor.execute(sql)
        row=new_cursor.fetchall()
        for i in row:
            self.medicine_table.delete(*self.medicine_table.get_children())

            for i in row:
                self.medicine_table.insert("",END,values=i)
            conn.commit()

        


    


            
    
    ######## MEDICINE DEPARTMENT FUNCTIONALITY #######
    def addmedicine(self):
        if self.refno_var.get() == "" or self.lotno_var.get() == "" or self.typemed_var.get() == "":
            messagebox.showerror("Error","All fields are required")
        else:
            conn=sqlite3.connect(database=r'.\pharmacy.db')
            new_cursor=conn.cursor()
            sql = "Insert into Information(REF_NO,COMPANY_NAME,TYPE_OF_MED,MED_NAME,LOT_NO,ISSUE_DT,EXP_DT,USES,SIDE_EFFECT,PRECAUTION,DOSAGE,PRICE,QUANTITY,BAN) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
            val =  (self.refno_var.get(),
            self.companyname_var.get(),
            self.typemed_var.get(),
            self.medicine_var.get(),
            self.lotno_var.get(),
            self.issuedt_var.get(),
            self.expdt_var.get(),
            self.uses_var.get(),
            self.sideeffect_var.get(),
            self.warning_var.get(),
            self.dosage_var.get(),
            self.price_var.get(),
            self.quantity_var.get(),
            self.banned_var.get()
            )
            new_cursor.execute(sql,val)
            conn.commit()
            self.fetch_new()
            conn.close()

            
            messagebox.showinfo("Success","Successfully added")

    def fetch_new(self):
        conn=sqlite3.connect(database=r'.\pharmacy.db')
        new_cursor=conn.cursor()
        new_cursor.execute("select * from Information")
        row=new_cursor.fetchall()

        if len(row)!=0:
            self.info_table.delete(*self.info_table.get_children())

            for i in row:
                self.info_table.insert("",END,values=i)

            conn.commit()
        conn.close()

        
    
    def get_cursor(self,event=""):
        cursor_row=self.info_table.focus()
        content=self.info_table.item(cursor_row)
        row=content["values"]
        self.refno_var.set(row[0])
        self.companyname_var.set(row[1])
        self.typemed_var.set(row[2])
        self.medicine_var.set(row[3])
        self.lotno_var.set(row[4])
        self.issuedt_var.set(row[5])
        self.expdt_var.set(row[6])
        self.uses_var.set(row[7])
        self.sideeffect_var.set(row[8])
        self.warning_var.set(row[9])
        self.dosage_var.set(row[10])
        self.price_var.set(row[11])
        self.quantity_var.set(row[12])
        self.banned_var.set(row[13])

    def update_new(self):
        
        if self.refno_var.get() == "" or self.lotno_var.get() == "" or self.typemed_var.get() == "":
            messagebox.showerror("Error","All fields are required")
        else:
            conn=sqlite3.connect(database=r'.\pharmacy.db')
            new_cursor=conn.cursor()
            sql = "Update Information set COMPANY_NAME=?,TYPE_OF_MED=?,MED_NAME=?,LOT_NO=?,ISSUE_DT=?,EXP_DT=?,USES=?,SIDE_EFFECT=?,PRECAUTION=?,DOSAGE=?,PRICE=?,QUANTITY=?,BAN=? where REF_NO=?"
            val = (self.companyname_var.get(),
            self.typemed_var.get(),
            self.medicine_var.get(),
            self.lotno_var.get(),
            self.issuedt_var.get(),
            self.expdt_var.get(),
            self.uses_var.get(),
            self.sideeffect_var.get(),
            self.warning_var.get(),
            self.dosage_var.get(),
            self.price_var.get(),
            self.quantity_var.get(),
            self.banned_var.get(),
            self.refno_var.get(),)
            new_cursor.execute(sql,val)
                                                                                        
            conn.commit()
            self.fetch_new()
            conn.close()
            messagebox.showinfo("Success","Successfully updated")

    def clear_new(self):
        conn=sqlite3.connect(database=r'.\pharmacy.db')
        new_cursor=conn.cursor()
        sql="delete from Information where REF_NO=?"
        val = (self.refno_var.get(),)
        new_cursor.execute(sql,val)
        conn.commit()
        self.fetch_new()
        conn.close()
        messagebox.showinfo('Delete',"Information deleted succesfully")


    def reset(self):
        self.companyname_var.set("")
        self.lotno_var.set("")
        self.issuedt_var.set("")
        self.expdt_var.set("")
        self.uses_var.set("")
        self.sideeffect_var.set("")
        self.warning_var.set("")
        self.dosage_var.set("")
        self.price_var.set("")
        self.quantity_var.set("")
        self.banned_var.set("")
        messagebox.showinfo('Reset',"Information Reseted succesfully")



    def search_data(self):

        conn=sqlite3.connect(database=r'.\pharmacy.db')
        new_cursor=conn.cursor()
        selected = self.search_by.get()
        if selected == "Select a Mode":
            messagebox.showerror("Error","You have to choose an Mode Option")
        
        elif selected == "Search By:Ref no" and self.search_txt.get() == "" :
            messagebox.showerror("Error","You have to write in the search box")

        elif selected == "Search By:Ref no":
            sql = "Select * from Information where REF_NO=?"
            val = (self.search_txt.get(),)
            new_cursor.execute(sql,val)
            row=new_cursor.fetchall()

            if len(row)!=0:
                self.info_table.delete(*self.info_table.get_children())

                for i in row:
                    self.info_table.insert("",END,values=i)

                conn.commit()

        elif selected == "Search By:Lot" and self.search_txt.get() == "" :
            messagebox.showerror("Error","You have to write in the search box")
        

        elif selected == "Search By:Lot":
            sql = "Select * from Information where LOT_NO=?"
            val =(self.search_txt.get(),)
            new_cursor.execute(sql,val)
            row=new_cursor.fetchall()

            if len(row)!=0:
                self.info_table.delete(*self.info_table.get_children())

                for i in row:
                    self.info_table.insert("",END,values=i)

                conn.commit()

        elif selected == "Search By:MedName" and self.search_txt.get() == "" :
            messagebox.showerror("Error","You have to write in the search box")
        

        elif selected == "Search By:MedName":
            sql = "Select * from Information where MED_NAME=?"
            val = (self.search_txt.get(),)
            new_cursor.execute(sql,val)
            row=new_cursor.fetchall()

            if len(row)!=0:
                self.info_table.delete(*self.info_table.get_children())

                for i in row:
                    self.info_table.insert("",END,values=i)
            conn.commit()
        
        elif selected == "Sort By:Ascending" : 
            messagebox.showerror("Error","You have to choose a Search Option")

        elif selected == "Sort By:Descending" : 
            messagebox.showerror("Error","You have to choose a Search Option")

    


        
        conn.close()

    def order_data(self):
        conn=sqlite3.connect(database=r'.\pharmacy.db')
        new_cursor=conn.cursor()
        selected = self.search_by.get()

        if selected == "Select a Mode":
            messagebox.showerror("Error","You have to choose a Mode Option")

        elif selected == "Sort By:Ascending":
            sql ="Select * from Information order by MED_NAME"
            new_cursor.execute(sql)
            row=new_cursor.fetchall()
            for i in row:
                self.info_table.delete(*self.info_table.get_children())

                for i in row:
                    self.info_table.insert("",END,values=i)
            conn.commit()
        
        elif selected == "Sort By:Descending":
            sql="Select * from Information order by MED_NAME desc"
            new_cursor.execute(sql)
            row=new_cursor.fetchall()
            for i in row:
                self.info_table.delete(*self.info_table.get_children())

                for i in row:
                    self.info_table.insert("",END,values=i)
            conn.commit()
        
        elif selected == "Search By:MedName" : 
            messagebox.showerror("Error","You have to choose a Sorting Option")


        elif selected == "Search By:Ref no" : 
            messagebox.showerror("Error","You have to choose a Sorting Option")
        
        elif selected == "Search By:Lot" : 
            messagebox.showerror("Error","You have to choose a Sorting Option")
        
        

        
        conn.close()

    def remove(self):
        conn=sqlite3.connect(database=r'.\pharmacy.db')
        new_cursor=conn.cursor()
        if self.search_txt.get() == "" :
            messagebox.showerror("Error","You have to write a number in the entry box")
        elif self.search_txt.get() != "" :
            sql = "Update Information set QUANTITY = QUANTITY - ? where QUANTITY = ?"
            val = (self.search_txt.get(),self.quantity_var.get())
            new_cursor.execute(sql,val)
            conn.commit()
            self.fetch_new()
            messagebox.showinfo("Success","Successfully Removed")

        
        conn.close()

    def add(self):
        conn=sqlite3.connect(database=r'.\pharmacy.db')
        new_cursor=conn.cursor()
        if self.search_txt.get() == "" :
            messagebox.showerror("Error","You have to write a number in the entry box")
        elif self.search_txt.get() != "" :
            sql = "Update Information set QUANTITY = QUANTITY + ? where QUANTITY = ?"
            val = (self.search_txt.get(),self.quantity_var.get())
            new_cursor.execute(sql,val)
            conn.commit()
            self.fetch_new()
            messagebox.showinfo("Success","Successfully added")
            

        
        conn.close()

    def bellow(self):
        conn=sqlite3.connect(database=r'.\pharmacy.db')
        new_cursor=conn.cursor()
        sql = "select * from Information where QUANTITY <300 "
        new_cursor.execute(sql)
        row=new_cursor.fetchall()
        if len(row) != 0 :
            self.info_table.delete(*self.info_table.get_children())

            for i in row:
                self.info_table.insert("",END,values=i)
            conn.commit()
        conn.close()



        
    def slider(self):
        if self.count>=len(self.txt):
            self.count=-1
            self.text=""
            self.heading.config(text=self.text)
        else:
            self.text=self.text+self.txt[self.count]
            self.heading.config(text=self.text)
        self.count+=1
        self.heading.after(200,self.slider)
    def heading_color(self):
        fg=random.choice(self.color)
        self.heading.config(fg=fg)
        self.heading.after(100,self.heading_color)



if __name__ == '__main__':
    root=Tk()
    obj=Pharmacy(root)
    root.mainloop()




