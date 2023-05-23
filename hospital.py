from tkinter import *
from tkinter import ttk #libary
import random #Generate Random Number
import time
import datetime
from tkinter import messagebox
import mysql.connector


class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1270x630+0+0") #Width*Height+x-axis_start+y-axis_start

        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.SideEffect=StringVar()
        self.Bloodpressure=StringVar()
        self.Medication=StringVar()
        self.PatienID=StringVar()
        self.NHSnumber=StringVar()
        self.Patientname=StringVar()
        self.dob=StringVar()
        self.Patientaddress=StringVar()

        lbltitle=Label(self.root,bd=15,relief=RIDGE,text="Hospital Management System",fg="red",bg="white",font=("times new roman",30,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        #======================================Data Frame==============================================

        Dataframe=Frame(self.root,bd=15,relief=RIDGE)
        Dataframe.place(x=0,y=82,width=1270,height=300)

        Dataframeleft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Patient Information")
        Dataframeleft.place(x=10,y=5,width=800,height=255)

        Dataframeright=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Prescription")
        Dataframeright.place(x=820,y=5,width=410,height=255)

        #======================================Button Frame============================================

        Buttonframe=Frame(self.root,bd=15,relief=RIDGE)
        Buttonframe.place(x=0,y=383,width=1270,height=70)

        #======================================Details Frame============================================

        Detailsframe=Frame(self.root,bd=15,relief=RIDGE)
        Detailsframe.place(x=0,y=454,width=1270,height=170)

        #======================================Data Frame Left============================================

        lblNameTablet=Label(Dataframeleft,text="Name Of Tablet",font=("times new roman",12),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0,sticky=W)

        comNametablet=ttk.Combobox(Dataframeleft,textvariable=self.Nameoftablets,font=("times new roman",12,"bold"),width=28)
        comNametablet["values"]=("Nice","Corona Vaccine","Accetaminophen","Adderall","Amlodipine","Ativan")
        comNametablet.grid(row=0,column=1)

        lblref=Label(Dataframeleft,text="Name Of Reference: ",font=("times new roman",12,"bold"),padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(Dataframeleft,textvariable=self.ref,font=("times new roman",12,"bold"),width=30)
        txtref.grid(row=1,column=1)

        lbldose=Label(Dataframeleft,text="Name Of Dose: ",font=("times new roman",12,"bold"),padx=2,pady=4)
        lbldose.grid(row=2,column=0,sticky=W)
        txtdose=Entry(Dataframeleft,textvariable=self.Dose,font=("times new roman",12,"bold"),width=30)
        txtdose.grid(row=2,column=1)

        lbltab=Label(Dataframeleft,text="Number Of Tablet: ",font=("times new roman",12,"bold"),padx=2,pady=4)
        lbltab.grid(row=3,column=0,sticky=W)
        txttab=Entry(Dataframeleft,textvariable=self.NumberofTablets,font=("times new roman",12,"bold"),width=30)
        txttab.grid(row=3,column=1)

        lbliss=Label(Dataframeleft,text="Issue Date: ",font=("times new roman",12,"bold"),padx=2,pady=4)
        lbliss.grid(row=4,column=0,sticky=W)
        txtiss=Entry(Dataframeleft,textvariable=self.Issuedate,font=("times new roman",12,"bold"),width=30)
        txtiss.grid(row=4,column=1)

        lbldexp=Label(Dataframeleft,text="Expiry Date: ",font=("times new roman",12,"bold"),padx=2,pady=4)
        lbldexp.grid(row=5,column=0,sticky=W)
        txtdexp=Entry(Dataframeleft,textvariable=self.ExpDate,font=("times new roman",12,"bold"),width=30)
        txtdexp.grid(row=5,column=1)

        lblside=Label(Dataframeleft,text="Side Effect: ",font=("times new roman",12,"bold"),padx=2,pady=4)
        lblside.grid(row=6,column=0,sticky=W)
        txtside=Entry(Dataframeleft,textvariable=self.SideEffect,font=("times new roman",12,"bold"),width=30)
        txtside.grid(row=6,column=1)

        lblblood=Label(Dataframeleft,text="Blood Pressure: ",font=("times new roman",12,"bold"),padx=2,pady=4)
        lblblood.grid(row=0,column=2,sticky=W)
        txtblood=Entry(Dataframeleft,textvariable=self.Bloodpressure,font=("times new roman",12,"bold"),width=30)
        txtblood.grid(row=0,column=3)

        lblmed=Label(Dataframeleft,text="Medication: ",font=("times new roman",12,"bold"),padx=2,pady=4)
        lblmed.grid(row=1,column=2,sticky=W)
        txtmed=Entry(Dataframeleft,textvariable=self.Medication,font=("times new roman",12,"bold"),width=30)
        txtmed.grid(row=1,column=3)

        lblid=Label(Dataframeleft,text="Patient ID: ",font=("times new roman",12,"bold"),padx=2,pady=4)
        lblid.grid(row=2,column=2,sticky=W)
        txtid=Entry(Dataframeleft,textvariable=self.PatienID,font=("times new roman",12,"bold"),width=30)
        txtid.grid(row=2,column=3)

        lblnhs=Label(Dataframeleft,text="NHS Number: ",font=("times new roman",12,"bold"),padx=2,pady=4)
        lblnhs.grid(row=3,column=2,sticky=W)
        txtnhs=Entry(Dataframeleft,textvariable=self.NHSnumber,font=("times new roman",12,"bold"),width=30)
        txtnhs.grid(row=3,column=3)

        lblname=Label(Dataframeleft,text="Patient Name: ",font=("times new roman",12,"bold"),padx=2,pady=4)
        lblname.grid(row=4,column=2,sticky=W)
        txtname=Entry(Dataframeleft,textvariable=self.Patientname,font=("times new roman",12,"bold"),width=30)
        txtname.grid(row=4,column=3)

        lbldob=Label(Dataframeleft,text="Date Of Birth: ",font=("times new roman",12,"bold"),padx=2,pady=4)
        lbldob.grid(row=5,column=2,sticky=W)
        txtdob=Entry(Dataframeleft,textvariable=self.dob,font=("times new roman",12,"bold"),width=30)
        txtdob.grid(row=5,column=3)

        lbladd=Label(Dataframeleft,text="Patient address: ",font=("times new roman",12,"bold"),padx=2,pady=4)
        lbladd.grid(row=6,column=2,sticky=W)
        txtadd=Entry(Dataframeleft,textvariable=self.Patientaddress,font=("times new roman",12,"bold"),width=30)
        txtadd.grid(row=6,column=3)

        #======================================Data Frame Right============================================

        self.txtpres=Text(Dataframeright,font=("times new roman",12,"bold"),width=46,height=11,padx=2,pady=4)
        self.txtpres.grid(row=0,column=0)

        #======================================Button=====================================================

        btnpres=Button(Buttonframe, command=self.iPrescription, text="Presciption",bg="darkblue",fg="white",font=("times new roman",12,"bold"),width=21,height=1,padx=2,pady=4)
        btnpres.grid(row=0,column=0)

        btnpresdata=Button(Buttonframe, command=self.ipresciptiondata, text="Presciption Data",bg="darkblue",fg="white",font=("times new roman",12,"bold"),width=25,height=1,padx=2,pady=4)
        btnpresdata.grid(row=0,column=1)
        
        btnupdate=Button(Buttonframe, command=self.update, text="Update",bg="darkblue",fg="white",font=("times new roman",12,"bold"),width=21,height=1,padx=2,pady=4)
        btnupdate.grid(row=0,column=2)

        btndelete=Button(Buttonframe, command=self.idelete, text="Delete",bg="darkblue",fg="white",font=("times new roman",12,"bold"),width=21,height=1,padx=2,pady=4)
        btndelete.grid(row=0,column=3)

        btnclear=Button(Buttonframe, command=self.clear, text="Clear",bg="darkblue",fg="white",font=("times new roman",12,"bold"),width=21,height=1,padx=2,pady=4)
        btnclear.grid(row=0,column=4)

        btnexit=Button(Buttonframe, command=self.iexit, text="Exit",bg="darkblue",fg="white",font=("times new roman",12,"bold"),width=21,height=1,padx=2,pady=4)
        btnexit.grid(row=0,column=5)

        #======================================Table - Scroll Bar=====================================================

        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)

        self.hospital_table=ttk.Treeview(Detailsframe,columns=("nameoftable","ref","dose","nooftablet","issuedate","expdate","sideeffect","bloodpressure","medication","patientid",
                                                               "nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftable",text="Name Of Tablet")
        self.hospital_table.heading("ref",text="Reference")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablet",text="Number Of Tablet")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Expiry Date")
        self.hospital_table.heading("sideeffect",text="Side Effect")
        self.hospital_table.heading("bloodpressure",text="Blood Pressure")
        self.hospital_table.heading("medication",text="Medication")
        self.hospital_table.heading("patientid",text="Patient ID")
        self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="Date Of Birth")
        self.hospital_table.heading("address",text="Patient Address")

        self.hospital_table["show"]="headings"

        self.hospital_table.column("nameoftable",width=100)
        self.hospital_table.column("ref",width=70)
        self.hospital_table.column("dose",width=40)
        self.hospital_table.column("nooftablet",width=110)
        self.hospital_table.column("issuedate",width=80)
        self.hospital_table.column("expdate",width=80)
        self.hospital_table.column("sideeffect",width=80)
        self.hospital_table.column("bloodpressure",width=90)
        self.hospital_table.column("medication",width=120)
        self.hospital_table.column("patientid",width=75)
        self.hospital_table.column("nhsnumber",width=85)
        self.hospital_table.column("pname",width=105)
        self.hospital_table.column("dob",width=90)
        self.hospital_table.column("address",width=90)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    #======================================Functionality Declaration=====================================================

    def ipresciptiondata(self):
        if self.Nameoftablets.get()=="" or self.ref.get()=="": #Field empty
            messagebox.showerror("Error","All fields are required!")
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password="",database="project")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.Nameoftablets.get(),
                self.ref.get(),
                self.Dose.get(),
                self.NumberofTablets.get(),
                self.Issuedate.get(),
                self.ExpDate.get(),
                self.SideEffect.get(),
                self.Bloodpressure.get(),
                self.Medication.get(),
                self.PatienID.get(),
                self.NHSnumber.get(),
                self.Patientname.get(),
                self.dob.get(),
                self.Patientaddress.get()

            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Record has been inserted.")

    
    def update(self):
        conn=mysql.connector.connect(host='localhost',username='root',password="",database="project")
        my_cursor=conn.cursor()
        my_cursor.execute("update hospital set Nameoftablet=%s, Nameofdose=%s, Numberoftablets=%s, Issuedate=%s, Expirydate=%s, Sideeffect=%s, Bloodpressure=%s, Medication=%s, PatientID=%s, NHSnumber=%s, Patientname=%s, DOB=%s, Patientadd=%s where ReferenceNo=%s",(
                self.Nameoftablets.get(),
                self.Dose.get(),
                self.NumberofTablets.get(),
                self.Issuedate.get(),
                self.ExpDate.get(),
                self.SideEffect.get(),
                self.Bloodpressure.get(),
                self.Medication.get(),
                self.PatienID.get(),
                self.NHSnumber.get(),
                self.Patientname.get(),
                self.dob.get(),
                self.Patientaddress.get(),
                self.ref.get()

            ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success","Record has been updated.")


    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password="",database="project")
        my_cursor=conn.cursor()
        my_cursor.execute("select *from hospital")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
            conn.close()


    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberofTablets.set(row[3])
        self.Issuedate.set(row[4])
        self.ExpDate.set(row[5])
        self.SideEffect.set(row[6])
        self.Bloodpressure.set(row[7])
        self.Medication.set(row[8])
        self.PatienID.set(row[9])
        self.NHSnumber.set(row[10])
        self.Patientname.set(row[11])
        self.dob.set(row[12])
        self.Patientaddress.set(row[13])

    
    def iPrescription(self):
        self.txtpres.insert(END,"Name of Tablets:\t\t\t"+self.Nameoftablets.get()+"\n")
        self.txtpres.insert(END,"Reference No:\t\t\t"+self.ref.get()+"\n")
        self.txtpres.insert(END,"Dose:\t\t\t"+self.Dose.get()+"\n")
        self.txtpres.insert(END,"Number of Tablets:\t\t\t"+self.NumberofTablets.get()+"\n")
        self.txtpres.insert(END,"Issue Date:\t\t\t"+self.Issuedate.get()+"\n")
        self.txtpres.insert(END,"Expiry Date:\t\t\t"+self.ExpDate.get()+"\n")
        self.txtpres.insert(END,"Side Effect:\t\t\t"+self.SideEffect.get()+"\n")
        self.txtpres.insert(END,"Blood Pressure:\t\t\t"+self.Bloodpressure.get()+"\n")
        self.txtpres.insert(END,"Medication:\t\t\t"+self.Medication.get()+"\n")
        self.txtpres.insert(END,"Patient ID:\t\t\t"+self.PatienID.get()+"\n")
        self.txtpres.insert(END,"NHS Number:\t\t\t"+self.NHSnumber.get()+"\n")
        self.txtpres.insert(END,"Patient Name:\t\t\t"+self.Patientname.get()+"\n")
        self.txtpres.insert(END,"Date Of Birth:\t\t\t"+self.dob.get()+"\n")
        self.txtpres.insert(END,"Patient Address:\t\t\t"+self.Patientaddress.get()+"\n")


    def idelete(self):
        conn=mysql.connector.connect(host='localhost',username='root',password="",database="project")
        my_cursor=conn.cursor()
        query="delete from hospital where ReferenceNo=%s"
        value=(self.ref.get(),)
        my_cursor.execute(query,value)

        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete","Information has been deleted succesfully.")


    def clear(self):
        self.Nameoftablets.set("")
        self.ref.set(""),
        self.Dose.set(""),
        self.NumberofTablets.set(""),
        self.Issuedate.set(""),
        self.ExpDate.set(""),
        self.SideEffect.set(""),
        self.Bloodpressure.set(""),
        self.Medication.set(""),
        self.PatienID.set(""),
        self.NHSnumber.set(""),
        self.Patientname.set(""),
        self.dob.set(""),
        self.Patientaddress.set("")
        self.txtpres.delete("1.0",END)


    def iexit(self):
        iexit=messagebox.askyesno("Hospital Management System","Confirm to continue.")
        if iexit>0:
            root.destroy()
            return




root=Tk()
ob=Hospital(root)
root.mainloop()