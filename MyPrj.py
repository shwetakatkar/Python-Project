#------------------------------------------------------------- Modules -----------------------------------------------------------


from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import time
import datetime
from time import strftime
import pymysql
from tkinter import messagebox
from tkinter import _tkinter
import PIL.Image, PIL.ImageTk
from ttkthemes import themed_tk as tk
import re
root=Tk()
root.geometry('700x400')
root.title("Excellence tutorial")
root.resizable(0,0)
style1 = Style()

#-------------------------------------------------------------Declaration-----------------------------------------------------------

pwd=StringVar()
uname=StringVar()
USERNAME=StringVar()
PASSWORD1=StringVar()
PASSWORD2=StringVar()
FIRSTNAME=StringVar()
LASTNAME=StringVar()

sid=StringVar(value='')
lname=StringVar(value='')
fname=StringVar(value='')
clss=StringVar(value='')
gender=StringVar(value='')
pname=StringVar(value='')
mname=StringVar(value='')
emailid=StringVar(value='')
caste=StringVar(value='')
religion=StringVar(value='')
bgrp=StringVar(value='')

day=IntVar(value=int(strftime("%d")))
month=IntVar(value=int(strftime("%m")))
year=IntVar(value=int(strftime("%Y")))
mobno=StringVar(value='')
stream=StringVar()
subject=StringVar()
phy=IntVar()
chem=IntVar()
eng=IntVar()
maths=IntVar()
bio=IntVar()
mks=IntVar()
tmks =IntVar()
mk=IntVar()
per=DoubleVar()
ecode=StringVar()
rsid=StringVar()
funpd=StringVar()
fpd=StringVar()
fsid=StringVar()
fttl=StringVar()
ftamt=StringVar()
pd=IntVar()
unpd=IntVar()
tid=StringVar()
tlname=StringVar()
tfname=StringVar()
tedu=StringVar()
tgender=StringVar()
temailid=StringVar()
tday=IntVar(value=int(strftime("%d")))
tmonth=IntVar(value=int(strftime("%m")))
tyear=IntVar(value=int(strftime("%Y")))
tmobno=StringVar()
stid=StringVar()
trs=StringVar()
thrs=StringVar()
tamt=StringVar()
value0=StringVar()
DateOfToday=StringVar()
newdate=StringVar()

#--------------------------------------------------Dbms----------------------------------------------------------------------------------


db=pymysql.connect("localhost","root","root")
cursor=db.cursor()
cursor.execute("create database if not exists db")
cursor.execute("use db")


#----------------------------------------------------------------Student Class Display-----------------------------------------------------------
def cls():
    top=Toplevel()
    top.title('class')
    top.geometry('1300x750')
    top.config(background='White')
    top.resizable(0,0)
    style = Style()
    style.configure('W.TButton', font =('Times New Roman', 20, 'bold'),relief="groove",anchor='center')
    tree=ttk.Treeview(top)
    style.configure("mystyle.Treeview", highlightthickness=1, bd=1, font=('helvetica', 16)) # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('arial', 14,'bold')) # Modify the font of the headings
    tree=Treeview(top,style="mystyle.Treeview",show="headings",height=25)
    tree.pack(side=TOP,fill=X)
   
    tree['columns'] = ('ID', 'F_Name', 'L_Name', 'Class','gender','dob','mob_no','paid','unpaid')
    #tree.configure(yscrollcommand=vsb.set)
    tree.column("ID", width=5, anchor='c')
    tree.heading("#1", text="ID")
    tree.column("F_Name", width=10, anchor='c')
    tree.heading("#2", text="Last Name")
    tree.column("L_Name", width=10, anchor='c')
    tree.heading("#3", text="First Name")
    tree.column("Class", width=10, anchor='c')
    tree.heading("#4", text="Class")
    tree.column("gender", width=10, anchor='c')
    tree.heading("#5", text="Gender")
    tree.column("dob", width=10, anchor='c')
    tree.heading("#6", text="Date of birth")
    tree.column("mob_no", width=10, anchor='c')
    tree.heading("#7", text="Mobile No")
    tree.column("paid", width=10, anchor='c')
    tree.heading("#8", text="Fees paid")
    tree.column("unpaid", width=10, anchor='c')
    tree.heading("#9", text="Fees unpaid")
    sql_a="select * from student"
    cursor.execute(sql_a)
    result=cursor.fetchall()
    cpt = 0
    for row in result:
   # I suppose the first column of your table is ID
           tree.insert('', 'end', text=str(cpt), values=(row[0], row[1], row[2], row[3] , row[4] , row[5] , row[9] , row[13] , row[14] ))
           cpt+=1
           
#----------------------------------------------------------------Student Attendence-----------------------------------------------------------------------

def attendence():
    rtt=Toplevel()
    rtt.title("Attendence register")
    rtt.geometry('730x750+0+0')
    rtt.resizable(0,0)
    rtt.config(background='white smoke')
    '''background_image=PhotoImage(file='F:\\sycs pracs\\python\\backgrd1.png')
    background_label = Label(rtt, image=background_image)
    background_label.image = background_image
    background_label.grid()'''
    
    style = Style()
    
    style.configure('MY.TFrame', font =('helvetica', 14),anchor='center',background='white smoke')
    style.configure('W.TLabel', font =('helvetica', 14),anchor='center',background='white smoke')
    style.configure('W.TCombobox', font =('helvetica', 14, 'bold'),anchor='center')
    style.configure('W.TButton', font =('helvetica', 20, 'bold'),anchor='center',background='black')
    
    DateOfToday.set(strftime('%d %b %Y'))
    
    f1 = Frame(rtt,style='MY.TFrame', width = 900)  
    f1.grid(row=0)
    
    f2 = Frame(rtt,width = 900, height=100,style='MY.TFrame')  
    f2.grid(row=4,pady=5,sticky=W)
    
    f3 = Frame(rtt,width =100 ,height=70,style='MY.TFrame')
    f3.grid(row=10,pady=5)
    f4 = Frame(rtt,width =100 ,height=70,style='MY.TFrame')
    f4.grid(row=112,pady=5,sticky=W)
    
    f2.grid_rowconfigure(0, weight=1)
    f2.grid_columnconfigure(0, weight=1)

    def on_configure(event):
        # update scrollregion after starting 'mainloop'
        # when all widgets are in canvas
        canvas.configure(scrollregion=canvas.bbox('all'))

    

    yscrollbar = Scrollbar(f3)
    
    yscrollbar.grid(row=0, column=5, sticky='NS')

    canvas = Canvas(f3,yscrollcommand=yscrollbar.set ,width = 600,height=500, background='white smoke')
    frm = Frame(canvas,width=1000,style='MY.TFrame')
    
    canvas.create_window((9000,9000), window=frm, anchor='nw',height=700)
    canvas.grid(row=0, column=0)
    
    canvas.bind('<Configure>', on_configure)
   
    yscrollbar.config(command=canvas.yview)
    
    l5=Label(f1,font=('helvetica',15),textvariable=DateOfToday,width=15,anchor='w')
    l5.grid(column=1, row=1,sticky='',padx=25,pady=10,ipadx=3,ipady=3)
    l5.configure(background='white smoke')
    
    l1=Label(f2,text="")
    l1.grid(row=2,column=0,sticky=W,padx=5,pady=10,ipadx=3,ipady=3)
    l1.config(background='white smoke')
    l1=Label(f2,font=('helvetica',16,'bold'),text="  Student Id  ",relief='raise',width=13)
    l1.grid(row=2,column=1,sticky=W+S,padx=30,pady=10,ipadx=5,ipady=5)
    

    l2=Label(f2,font=('helvetica',16,'bold'),text="  Student Name  ",relief='raise',width=13)
    l2.grid(row=2,column=2,sticky=W+S,padx=30,pady=10,ipadx=5,ipady=5)

    l3=Label(f2,font=('helvetica',16,'bold'),text="  Attendence  ",relief='raise',width=11)
    l3.grid(row=2,column=3,sticky=E+S ,padx=30,pady=10,ipadx=5,ipady=5)

    namesID = []
    sql_a="select * from student"
    cursor.execute(sql_a)
    result=cursor.fetchall()
    
    for row in result:
        namesID.append(row[0])
    i=0
    for i in range(len(namesID)):
        cur_label = 'label' + str(i) # label0, label1
        cur_label = Label(frm, text = namesID[i],style='W.TLabel')
        cur_label.grid(row=i+3,column=0,sticky=W,padx=80,pady=10,ipadx=3,ipady=3)

    names = []
    sql_a1="select * from student"
    cursor.execute(sql_a1)
    result=cursor.fetchall()
    
    for row in result:
        names.append(str(row[1])+" "+str(row[2]))
    i=0
    for i in range(len(namesID)):
        
        cur_label = ('label' + str(i)) # label0, label1
        cur_label = Label(frm, text = names[i],style='W.TLabel')
        cur_label.grid(row=i+3, column=1,sticky=W,padx=50,pady=10,ipadx=3,ipady=3)
    vars = []
    
    for i in range(len(namesID)):
        box = 'box' + str(i) # l
        var = StringVar()
    
        box=Combobox(frm, textvariable=var,style='W.TCombobox',state='readonly',width=10)
        box['values']=('','Present','Absent')
        box.current=(0)
        vars.append(var)
        box.grid(row=i+3,column=2,sticky=W ,padx=50,pady=10,ipadx=1,ipady=1)
        

    def qExit():
        ans=messagebox.askyesno("Exit System","Do you want to quit?",parent=rtt)
        if (ans):
            rtt.destroy()
    
    def save():
        now = datetime.datetime.now()
        
        sql3="""create table if not exists attendence(t_date date , ID int(10) ,Name varchar(20) ,Status varchar(10))"""
        cursor.execute(sql3)
        for i in range(1,5):
            
            print(newdate)
            cursor.execute("Insert into attendence(t_date,ID,Name, Status) values ('{}','{}','{}','{}')".format((now.strftime("%Y-%m-%d")) ,(namesID[i]),(names[i]),(vars[i]).get()))
            db.commit()

    b1=Button(f4,text="Save",style="W.TButton",width=10,command=save)
    b1.grid(row=20,column=0,padx=35,pady=40,sticky=SW)

    b3=Button(f4,text="Exit",style="W.TButton",width=10,command=qExit)
    b3.grid(row=20,column=2,padx=15,pady=40,sticky=SW)
    
    rtt.mainloop()

#----------------------------------------------------------------Student Fees-----------------------------------------------------------------------

def Fees():
    s1=Toplevel()
    s1.title('Student')
    s1.geometry('600x500')
    style = Style()
    style.configure('W.TButton', font =('Times New Roman', 17, 'bold'),relief="groove",anchor='center',background='black')
    style.configure('BW1.TLabel', font =('Helvetica', 15, 'bold'),anchor='center')
    s1.resizable(0,0)
    def f_ok():

        
        try:
            xs_fsid=int(fsid.get())
        except:
            messagebox.showerror('','Only digits are allowed in Student ID',parent=s1)
        cursor.execute( "SELECT Id, COUNT(*) FROM student WHERE Id = %s GROUP BY Id", (int(fsid.get()) ))
        row_count = cursor.rowcount
    
        if row_count == 0:
            es5.delete(0,END)
            es6.delete(0,END)
            messagebox.showerror('',' Given Student ID doesn\'t exists. Enter valid ID.',parent=s1)
        else:
            cursor.execute("select * from student where ID=%s", (int(fsid.get() )))
            resl=cursor.fetchall()
            for row in resl:
                es5.delete(0,END)
                es5.insert(0,row[13])
                es6.delete(0,END)
                es6.insert(0,row[14])
        
            
    def fees_pay():
        try:
            x_tamt=int(ftamt.get())
                  
        except:
            messagebox.showerror('','Only digits are allowed in Amount',parent=s1)
        if (int(funpd.get())<= (int(ftamt.get()))):
            messagebox.showerror('','Enter amount less than or equal to Unpaid Fees.',parent=s1)
        else:
            cursor.execute("update student set Fees_unpaid=(Fees_unpaid - %s) where Id=%s",(int(ftamt.get()), int(fsid.get()) ))
            cursor.execute("update student set Fees_paid=(Fees_paid+%s) where Id=%s",(int(ftamt.get()), int(fsid.get()) ))
            db.commit()
            cursor.execute("select * from student where ID=%s", (int(fsid.get() )))
            resl=cursor.fetchall()
            for row in resl:
                es5.delete(0,END)
                es5.insert(0,row[13])
                es6.delete(0,END)
                es6.insert(0,row[14])
    
    
    s0=Label(s1,text="Student ID :",style='BW1.TLabel')
    s0.grid(column=0,row=1,padx=15,pady=5,sticky='w')
    es1=Entry(s1,width=20,textvariable=fsid)
    es1.grid(column=1,row=1,padx=15,pady=10,sticky='w',ipadx=3,ipady=3)

    ss0=Label(s1,text="Total Fees :",style='BW1.TLabel')
    ss0.grid(column=0,row=2,padx=15,pady=5,sticky='w')
    ess1=Entry(s1,width=20,textvariable=fttl,state='Readonly')
    ess1.grid(column=1,row=2,padx=15,pady=10,sticky='w',ipadx=3,ipady=3)
    ess1.delete(0,END)
    ess1.insert(0,40000)
    
    bs1=Button(s1,text="OK",command=f_ok,width=10,style='W.TButton')
    bs1.grid(column=1,row=3,padx=0,pady=20,sticky='')
    

    s5=Label(s1,text="Paid :",style='BW1.TLabel',state='readonly')
    s5.grid(column=0,row=4,padx=15,pady=5,sticky='w')
    es5=Entry(s1,width=20,textvariable=fpd)
    es5.grid(column=1,row=4,padx=15 ,pady=5,sticky='w',ipadx=3,ipady=3)

    s6=Label(s1,text="Unpaid :",style='BW1.TLabel',state='readonly')
    s6.grid(column=0,row=5,padx=15,pady=5,sticky='w')
    es6=Entry(s1,width=20,textvariable=funpd)
    es6.grid(column=1,row=5,padx=15 ,pady=5,sticky='w',ipadx=3,ipady=3)

    s4=Label(s1,text="Amount :",style='BW1.TLabel')
    s4.grid(column=0,row=6,padx=15,pady=5,sticky='w')
    es4=Entry(s1,width=20,textvariable=ftamt)
    es4.grid(column=1,row=6,padx=15,pady=5,sticky='w',ipadx=3,ipady=3)
    
    bs3=Button(s1,text="Pay  :",command=fees_pay ,width=10,style='W.TButton')
    bs3.grid(column=1,row=7,padx=15,pady=40,sticky='')

def result():
    re1=Toplevel()
    re1.title('RESULT')
    re1.geometry('900x900+0+0')
    style_r = Style()
    re1.resizable(0,0)
    style_r.configure('MY.TFrame' ,anchor='center')
    style_r.configure('W.TLabel', font =('helvetica', 16),anchor='w')
   
    style_r.configure('W.TButton', font =('helvetica', 18, 'bold'),anchor='center',background='black')
    
    fr1=Frame(re1, width=900, height=200,relief="groove",style='MY.TFrame')
    fr1.pack(fill=X)
    fr11=Frame(re1, width=900, height=700,relief="groove",style='MY.TFrame')
    fr11.pack(fill='both')
    
    l=Label(fr1,text="Exam code :", style='W.TLabel')
    l.grid(column=0,row=1,padx=15,pady=5,sticky='w')
    el=Entry(fr1,width=20,textvariable=ecode)
    el.grid(column=1,row=1,padx=0,sticky='w')
    
    lw0=Label(fr1,text="Student ID :", style='W.TLabel')
    lw0.grid(column=0,row=2,padx=15,pady=5,sticky='w')
    ew0=Entry(fr1,width=20,textvariable=rsid)
    ew0.grid(column=1,row=2,padx=0,sticky='w')

    lw=Label(fr1,text="Subject :          ", style='W.TLabel')
    lw.grid(column=0,row=4,padx=10,pady=5)
    cw2=Combobox(fr1,width=17,textvariable=subject,state='readonly')
    cw2['values']=("PCM","PCB","PCMB")
    cw2.current(0)
    cw2.grid(column=1,row=4,padx=0,sticky='w')

    def r_reset():
        phy.set("")
        chem.set("")
        eng.set("")
        maths.set("")
        bio.set("")
        mk.set("")
        tmks.set("")
        per.set("")

    def rExit():
        ans=messagebox.askyesno("Exit Window","Do you want to quit?",parent=re1)
        if (ans):
            re1.destroy()
    
    def insert_result():
        
        sql="""create table if not exists result(E_code varchar(10) not null, Id int(10) primary key,marks int(10) not null, english int(10) not null, physics int(10) not null, chemistry int(10) not null, maths int(10),biology int(10), total int(10), percentage float(10))"""
        cursor.execute(sql)
        sql1="insert into result(E_code,Id,marks,english,physics,chemistry,maths,biology, total, percentage)value('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(ecode.get(),sid.get(),tmks.get(),eng.get(),phy.get(),chem.get(),maths.get(),bio.get(),mk.get(),per.get())
        cursor.execute(sql1)
        db.commit()
        messagebox.showinfo('Success','Record inserted successfully...',parent=re1)
        db.close
    
        

    def sub():
        global tot
        global perc
        a=True
        while(a==True):
            if (rsid.get()=='' or ecode.get()=='' or subject.get()=='' ):
                    messagebox.showerror("Error","Please, Fill all fields",parent=re1)
                    break
        
            try:
                    x_sid=int(rsid.get())
            except:
                    messagebox.showerror('','Only digits are allowed in Student ID',parent=re1)
                    break
            cursor.execute( "SELECT Id, COUNT(*) FROM student WHERE Id = %s GROUP BY Id", (int(rsid.get())))
            if cursor.fetchone() is None:
                    messagebox.showerror('','Invalid Student ID.',parent=re1)
                    break
            else:
                    a=False
                
        if a==False:
                def res_cal_m():
                    tot = phy.get() + chem.get()+ eng.get() + maths.get()         
                    p=tmks.get()*4
                    perc=(((tot)/p)*100)
                    ew55.delete(0,END)
                    ew55.insert(0,tot)
                    ew66.delete(0,END)
                    ew66.insert(0,perc)
                def res_cal_b():
                    tot = phy.get() + chem.get()+ eng.get() + bio.get()         
                    p=tmks.get()*4
                    perc=(((tot)/p)*100)
                    ew55.delete(0,END)
                    ew55.insert(0,tot)
                    ew66.delete(0,END)
                    ew66.insert(0,perc)
                def res_cal_mb():
                    tot = phy.get() + chem.get()+ eng.get() + maths.get() + bio.get()      
                    p=tmks.get()*5
                    perc=(((tot)/p)*100)
                    ew55.delete(0,END)
                    ew55.insert(0,tot)
                    ew66.delete(0,END)
                    ew66.insert(0,perc)
                def res_display():
                    
                    p.destroy()
                    list = re1.grid_slaves()
                    for l in list:
                        l.destroy()

                
                    lw1=Label(fr11,text="Physics :", style='W.TLabel')
                    lw1.grid(column=0,row=9,padx=15,pady=10)
                    lw2=Label(fr11,text=phy.get(),font="times 16", anchor='w')
                    lw2.grid(column=1,row=9,padx=5,pady=20)

                    lw3=Label(fr11,text="Chemistry :", style='W.TLabel')
                    lw3.grid(column=0,row=10,padx=15,pady=10)
                    lw4=Label(fr11,text=chem.get(),font="times 16", anchor='w')
                    lw4.grid(column=1,row=10,padx=5,pady=10)

                    lw5=Label(fr11,text="Maths :", style='W.TLabel')
                    lw5.grid(column=0,row=11,padx=15,pady=10)
                    lw6=Label(fr11,text=maths.get(),font="times 16", anchor='w')
                    lw6.grid(column=1,row=11,padx=5,pady=10)

                    lw7=Label(fr11,text="Biology :", style='W.TLabel')
                    lw7.grid(column=0,row=12,padx=15,pady=10)
                    lw8=Label(fr11,text=bio.get(),font="times 16", anchor='w')
                    lw8.grid(column=1,row=12,padx=5,pady=10)

                    lw9=Label(fr11,text="English :", style='W.TLabel')
                    lw9.grid(column=0,row=13,padx=15,pady=10)
                    lw10=Label(fr11,text=eng.get(),font="times 16", anchor='w')
                    lw10.grid(column=1,row=13,padx=5,pady=10)

                    lw11=Label(fr11,text="total :", style='W.TLabel')
                    lw11.grid(column=0,row=14,padx=15,pady=10)
                    lw12=Label(fr11,text=mk.get() ,font="times 16", anchor='w')
                    lw12.grid(column=1,row=14,padx=5,pady=10)

                    lw13=Label(fr11,text="Percent :", style='W.TLabel')
                    lw13.grid(column=0,row=15,padx=15,pady=10)
                    lw14=Label(fr11,text=per.get(),font="times 16", anchor='w')
                    lw14.grid(column=1,row=15, padx=5,pady=10)

                    bw2=Button(fr11,text="Submit",command=insert_result,style='W.TButton',width=10)
                    bw2.grid(column=1,row=18,padx=0,pady=25,sticky='w')

                    bw6=Button(fr11,text="Exit",command=rExit,style='W.TButton',width=10)
                    bw6.grid(column=2,row=18,padx=10,pady=25,sticky='w')
            
                if subject.get() =="PCM":
                        p=Toplevel()
                        p.title('PCM')
                        p.geometry('500x500')
                        
                        l=Label(p,text="Marks :", style='W.TLabel')
                        l.grid(column=0,row=7,padx=15,pady=15,sticky='w')
                        e=Entry(p,width=15,textvariable=tmks)
                        e.grid(column=1,row=7,padx=15,pady=15,sticky='w')
                        e.delete(0,END)
                        e.insert(0,'100')
                        lw1=Label(p,text="Physics :", style='W.TLabel')
                        lw1.grid(column=0,row=9,padx=15,pady=10)
                        ew1=Entry(p,width=20,textvariable=phy)
                        ew1.grid(column=1,row=9,padx=0,sticky='w')

                        lw2=Label(p,text="    Chemistry :" , style='W.TLabel')
                        lw2.grid(column=0,row=10,padx=15,pady=5)
                        ew2=Entry(p,width=20,textvariable=chem)
                        ew2.grid(column=1,row=10,padx=0,sticky='w')

                        lw3=Label(p,text="English :", style='W.TLabel')
                        lw3.grid(column=0,row=11,padx=15,pady=5)
                        ew3=Entry(p,width=20,textvariable=eng)
                        ew3.grid(column=1,row=11,padx=0,sticky='w')
                    
                        lw4=Label(p,text="Maths :",font="Times 16")
                        lw4.grid(column=0,row=12,pady=5)
                        ew4=Entry(p,width=20,textvariable=maths)
                        ew4.grid(column=1,row=12,padx=0,sticky='w')
                        
                        bw2=Button(p,text="OK",command=res_cal_m,style='W.TButton',width=10)
                        bw2.grid(column=1,row=14,padx=10,pady=20,sticky='w')

                        lw6=Label(p,text="Total :", style='W.TLabel')
                        lw6.grid(column=0,row=15,padx=5,pady=5)
                        ew55=Entry(p,width=20,textvariable=mk)
                        ew55.grid(column=1,row=15,sticky='w')
                        
                        lw8=Label(p,text="Percentage : ", style='W.TLabel')
                        lw8.grid(column=0,row=17,padx=5,pady=5)
                        ew66=Entry(p,width=20,textvariable=per)
                        ew66.grid(column=1,row=17,sticky='w')
                        
                        bw3=Button(p,text='Confirm',command=res_display,style='W.TButton')
                        bw3.grid(column=1,row=19,padx=10,pady=25,sticky='w')

                        bw4=Button(p,text="Reset",command=r_reset,style='W.TButton',width=10)
                        bw4.grid(column=2,row=19,padx=10,pady=25,sticky='w')
                        
                elif subject.get() =="PCB":
                        p=Toplevel()
                        p.title('PCB')
                        p.geometry('500x500')
                        
                        l=Label(p,text="Marks :", style='W.TLabel')
                        l.grid(column=0,row=7,padx=15,pady=15,sticky='w')
                        e=Entry(p,width=15,textvariable=tmks)
                        e.grid(column=1,row=7,padx=15,pady=15,sticky='w')
                        e.delete(0,END)
                        e.insert(0,'100')
                        lw1=Label(p,text="Physics :", style='W.TLabel')
                        lw1.grid(column=0,row=9,padx=15,pady=10)
                        ew1=Entry(p,width=20,textvariable=phy)
                        ew1.grid(column=1,row=9,padx=0,sticky='w')

                        lw2=Label(p,text="    Chemistry :" , style='W.TLabel')
                        lw2.grid(column=0,row=10,padx=15,pady=5)
                        ew2=Entry(p,width=20,textvariable=chem)
                        ew2.grid(column=1,row=10,padx=0,sticky='w')

                        lw3=Label(p,text="English :", style='W.TLabel')
                        lw3.grid(column=0,row=11,padx=15,pady=5)
                        ew3=Entry(p,width=20,textvariable=eng)
                        ew3.grid(column=1,row=11,padx=0,sticky='w')
                        lw4=Label(p,text="  Biology  :", style='W.TLabel')
                        lw4.grid(column=0,row=12,padx=15,pady=5)
                        ew4=Entry(p,width=20,textvariable=bio)
                        ew4.grid(column=1,row=12,padx=0,sticky='w')
                        
                        bw3=Button(p,text="OK",command=res_cal_b,style='W.TButton',width=10)
                        bw3.grid(column=1,row=14,padx=10,pady=20,sticky='w')

                        lw6=Label(p,text="Total :", style='W.TLabel')
                        lw6.grid(column=0,row=15,padx=5,pady=5)
                        ew55=Entry(p,width=20,textvariable=mk)
                        ew55.grid(column=1,row=15,padx=15,pady=15,sticky='w')
                        
                        lw8=Label(p,text="Percentage : ", style='W.TLabel')
                        lw8.grid(column=0,row=17,padx=5,pady=5)
                        ew66=Entry(p,width=20,textvariable=per)
                        ew66.grid(column=1,row=17,padx=15,pady=15,sticky='w')

                        bw3=Button(p,text='Confirm',command=res_display,style='W.TButton')
                        bw3.grid(column=1,row=19,padx=10,pady=25,sticky='w')

                        bw4=Button(p,text="Reset",command=r_reset,style='W.TButton',width=10)
                        bw4.grid(column=2,row=19,padx=10,pady=25,sticky='w')
                        
                elif subject.get() =="PCMB":
                        p=Toplevel()
                        p.title('PCMB')
                        p.geometry('500x500')
                        
                       
                        l=Label(p,text="Marks :", style='W.TLabel')
                        l.grid(column=0,row=7,padx=15,pady=15,sticky='w')
                        e=Entry(p,width=15,textvariable=tmks)
                        e.grid(column=1,row=7,padx=15,pady=15,sticky='w')
                        e.delete(0,END)
                        e.insert(0,'100')
                        lw1=Label(p,text="Physics :", style='W.TLabel')
                        lw1.grid(column=0,row=9,padx=15,pady=10)
                        ew1=Entry(p,width=20,textvariable=phy)
                        ew1.grid(column=1,row=9,padx=0,sticky='w')

                        lw2=Label(p,text="    Chemistry :" , style='W.TLabel')
                        lw2.grid(column=0,row=10,padx=15,pady=5)
                        ew2=Entry(p,width=20,textvariable=chem)
                        ew2.grid(column=1,row=10,padx=0,sticky='w')

                        lw3=Label(p,text="English :", style='W.TLabel')
                        lw3.grid(column=0,row=11,padx=15,pady=5)
                        ew3=Entry(p,width=20,textvariable=eng)
                        ew3.grid(column=1,row=11,padx=0,sticky='w')
                        
                        lw4=Label(p,text= "Maths :", style='W.TLabel')
                        lw4.grid(column=0,row=12,pady=5)
                        ew4=Entry(p,width=20,textvariable=maths)
                        ew4.grid(column=1,row=12,padx=0,sticky='w')
                        lw5=Label(p,text="  Biology  :", style='W.TLabel')
                        lw5.grid(column=0,row=13,padx=15,pady=5)
                        ew5=Entry(p,width=20,textvariable=bio)
                        ew5.grid(column=1,row=13,padx=0,sticky='w')
                        
                        bw4=Button(p,text="OK",command=res_cal_mb,style='W.TButton',width=10)
                        bw4.grid(column=1,row=14,padx=10,pady=20,sticky='w')
                        
                        lw6=Label(p,text="Total :", style='W.TLabel')
                        lw6.grid(column=0,row=15,padx=5,pady=5)
                        ew55=Entry(p,width=20,textvariable=mk)
                        ew55.grid(column=1,row=15,sticky='w')
                        
                        lw8=Label(p,text="Percentage : ", style='W.TLabel')
                        lw8.grid(column=0,row=17,padx=5,pady=5)
                        ew66=Entry(p,width=20,textvariable=per)
                        ew66.grid(column=1,row=17,sticky='w')

                        bw3=Button(p,text='Confirm',command=res_display,style='W.TButton' )
                        bw3.grid(column=1,row=19,padx=10,pady=25,sticky='w')

                        bw4=Button(p,text="Reset",command=r_reset,style='W.TButton',width=10)
                        bw4.grid(column=2,row=19,padx=10,pady=25,sticky='w')
                                       
                else:
                        lw5=Label(re1 ,text=" ",font="Times 16")
                        lw5.grid(column=0,row=13,padx=15,pady=5)
                                    

    bw1=Button(fr1,text="OK",command=sub,style='W.TButton',width=10)
    bw1.grid(column=1,row=5,padx=10,pady=20,sticky='w')
    
#----------------------------------------------------------------Student Details-----------------------------------------------------------------------

def s_info():
    w1=Toplevel()
    w1.title('Information')
    w1.geometry('1600x800+0+0')
    w1.resizable(0,0)
    style_s= Style()
    style_s.configure('W.TLabel', font =('helvetica', 16, 'bold'),anchor='w')
   
    style_s.configure('W.TButton', font =('Times New Roman', 20, 'bold'),relief="groove",anchor='center')
    lw1=Label(w1,text="      ")
    lw1.grid(column=0,row=1,padx=15,pady=30)

    

    lw2=Label(w1,text="Student ID :",style='W.TLabel')
    lw2.grid(column=0,row=2,padx=15,pady=5)

    ew1=Entry(w1,width=20,textvariable=sid)
    ew1.grid(column=1,row=2,padx=0,sticky='w')

    lw3=Label(w1,text="Last Name :" ,style='W.TLabel')
    lw3.grid(column=0,row=3,padx=15,pady=5)

    ew2=Entry(w1,width=20,textvariable=lname)
    ew2.grid(column=1,row=3,padx=0,sticky='w')

    lw4=Label(w1,text="First Name :",style='W.TLabel')
    lw4.grid(column=0,row=4,pady=5)
    ew3=Entry(w1,width=20,textvariable=fname)
    ew3.grid(column=1,row=4,padx=0,sticky='w')

    lw5=Label(w1,text="Class :          ",style='W.TLabel')
    lw5.grid(column=0,row=5,padx=10,pady=5)
    cw1=Combobox(w1,width=17,textvariable=clss,state='readonly')
    cw1['values']=('','XI','XII')
    cw1.current(0)
    cw1.grid(column=1,row=5,padx=0,sticky='w')


    lw6=Label(w1,text="    Date Of Birth :",style='W.TLabel')
    lw6.grid(column=0,row=6,padx=15,pady=5)
    s1=Spinbox(w1,from_=1, to=31,width=4,textvariable=day,state='readonly')
    s1.grid(column=1,row=6,padx=5,sticky='w')
    s2=Spinbox(w1,from_=1, to=12,width=4,textvariable=month,state='readonly')
    s2.grid(column=1,row=6,padx=50,sticky='w')
    s3=Spinbox(w1,from_=(int(strftime("%Y"))-25), to=int(strftime("%Y")),width=6,textvariable=year,state='readonly')
    s3.grid(column=1,row=6,padx=96,sticky='w')
    

    lw7=Label(w1,text="Gender :        ",style='W.TLabel')
    lw7.grid(column=0,row=7,padx=15,pady=5)
    cw3=Combobox(w1,width=17,textvariable=gender,state='readonly')
    cw3['values']=('','Male','Female')
    cw3.current(0)
    cw3.grid(column=1,row=7,padx=0,sticky='w')

    lw8=Label(w1,text="    Father's Name :",style='W.TLabel')
    lw8.grid(column=0,row=8,padx=15,pady=5)
    ew5=Entry(w1,width=20,textvariable=pname)
    ew5.grid(column=1,row=8,padx=0,sticky='w')

    lw9=Label(w1,text="     Mother's Name :",style='W.TLabel')
    lw9.grid(column=0,row=9,padx=15,pady=5)
    ew6=Entry(w1,width=20,textvariable=mname)
    ew6.grid(column=1,row=9,padx=0,sticky='w')

    lw10=Label(w1,text="Contact No. :",style='W.TLabel')
    lw10.grid(column=0,row=10,padx=15,pady=5)
    ew7=Entry(w1,width=20,textvariable=mobno)
    ew7.grid(column=1,row=10,padx=0,sticky='w')

    lw11=Label(w1,text="Email ID :     ",style='W.TLabel')
    lw11.grid(column=0,row=11,padx=15,pady=5)
    ew8=Entry(w1,width=20,textvariable=emailid)
    ew8.grid(column=1,row=11,padx=0,sticky='w')

    lw12=Label(w1,text="Religion :      ",style='W.TLabel')
    lw12.grid(column=0,row=12,padx=15,pady=5)
    ew9=Entry(w1,width=20,textvariable=religion)
    ew9.grid(column=1,row=12,padx=0,sticky='w')

    lw13=Label(w1,text="Caste :           ",style='W.TLabel')
    lw13.grid(column=0,row=13,padx=15,pady=5)
    ew10=Entry(w1,width=20,textvariable=caste)
    ew10.grid(column=1,row=13,padx=0,sticky='w')

    lw14=Label(w1,text=" Blood group :",style='W.TLabel')
    lw14.grid(column=0,row=14,padx=15,pady=5)
    cw2=Combobox(w1,width=17,textvariable=bgrp,state='readonly')
    cw2['values']=('','A+','A-','B+','B-','AB+','AB-','O+','O-')
    cw2.current(0)
    cw2.grid(column=1,row=14,padx=0,sticky='w')

    
    def submit():
      sql="""create table if not exists student(Id int(10) primary key,F_name varchar(10) not null ,L_name varchar(10) not null,Class varchar(10) not null,Gender varchar(10) not null,DOB Date not null, Fathers_name varchar(10) not null,Mothers_name varchar(10) not null,
                                    Email_id varchar(20) not null,Mob_no bigint(20) not null,Caste varchar(10) not NULL,Religion varchar(10) not null,Blood_group Varchar(4) not null,Fees_paid int(10), Fees_unpaid int(10))"""
      cursor.execute(sql)
      global dob
      global x
      if (sid.get()=='' or lname.get()=='' or fname.get()=='' or clss.get()=='' or  gender.get()=='' or pname.get()=='' or mname.get()=='' or mobno.get()=='' or  emailid.get()=='' or religion.get()=='' or caste.get()=='' or bgrp.get()==''):
            messagebox.showerror("Error","Please, Fill all record",parent=w1)
      else:
        x=True
        while x==True :
            try:
                    x_sid=int(sid.get())
            except:
                    messagebox.showerror('','Only digits are allowed in Student ID',parent=w1)
                    break
            cursor.execute( "SELECT Id, COUNT(*) FROM student WHERE Id = %s GROUP BY Id", (int(sid.get())))
            if cursor.fetchone() is not None:
                    messagebox.showerror('','Student ID is already assigned.',parent=w1)
                    break
            
            try:
                if (type(int(lname.get()))) is int :
                    messagebox.showerror('','Only Alphabets are allowed in Last Name',parent=w1)
                    break
            except:
                pass
            try:
                if type(int(fname.get())) is int:
                    messagebox.showerror('','Only Alphabets are allowed in First Name',parent=w1)
                    break
            except:
                pass
            try :
                if type(int(pname.get())) is int:
                    messagebox.showerror('','Only Alphabets are allowed in Father\'s Name',parent=w1)
                    break
            except:
                pass
            try:
                if type(int(mname.get())) is int:
                    messagebox.showerror('','Only Alphabets are allowed in Mother\'s Name',parent=w1)
                    break
            except :
                pass
            try:
                    x_mob=int(mobno.get())
            except:
                    messagebox.showerror('','Only digits are allowed in Contact Number',parent=w1)
                    break
            try:
                if type(int(religion.get())) is int:
                    messagebox.showerror('','Only Alphabets are allowed in Religion name',parent=w1)
                    break
            except :
                pass
            try:
                if type(int(caste.get())) is int:
                    messagebox.showerror('','Only Alphabets are allowed in Caste name',parent=w1)
                    break
            except:
                pass
       
            if not re.search(r'(^\d{10}$)',str(mobno.get())):
                    messagebox.showerror("Error","Enter valid mobile number",parent=w1)
                    break   

            if not re.search(r'([\w.-]+)@([\w]+)\.(\w)', emailid.get()):
                    messagebox.showerror("Error","Enter valid email addressd",parent=w1)
                    break

            x=False
                        


      if x == False :
                            top=Toplevel()
                            top.title('Details')
                            top.geometry('900x5700+0+0')
                            top.resizable(0,0)
                            sty1 = Style()
                            sty1.configure('W.TButton', font =('Times New Roman', 25, 'bold'),relief="groove",anchor='center')
                            l11=Label(top,text="StudentId :",font =('Times New Roman', 18 ,'bold'))
                            l11.grid(column=1,row=1,sticky='w',pady=4)
                            l12=Label(top,text=sid.get(),font =('Times New Roman', 13))
                            l12.grid(column=2,row=1,sticky='w',columnspan=3)
                            
                            l13=Label(top,text="Last Name :",font =('Times New Roman', 16 ))
                            l13.grid(column=6,row=1,sticky='w')
                            l14=Label(top,text=lname.get(),font =('Times New Roman', 13))
                            l14.grid(column=7,row=1,sticky='w',columnspan=3)
                            
                            l15=Label(top,text="First Name :",font =('Times New Roman', 16))
                            l15.grid(column=1,row=2,sticky='w',pady=4)
                            l16=Label(top,text=fname.get(),font =('Times New Roman', 13))
                            l16.grid(column=2,row=2,sticky='w',columnspan=3)
                            
                            l17=Label(top,text="Class :",font =('Times New Roman', 16))
                            l17.grid(column=6,row=2,sticky='w')
                            l18=Label(top,text=clss.get(),font =('Times New Roman', 13))
                            l18.grid(column=7,row=2,sticky='w',columnspan=3)
                            
                            l19=Label(top,text="Date Of Birth :",font =('Times New Roman', 16))
                            l19.grid(column=1,row=3,sticky='w',pady=4)
                            dob=str(year.get())+"-"+str(month.get())+"-"+str(day.get())
                            l20=Label(top,text=dob,font =('Times New Roman', 13))
                            l20.grid(column=2,row=3,sticky='w',columnspan=3)
                            
                            l21=Label(top,text="Gender :",font =('Times New Roman', 16))
                            l21.grid(column=6,row=3,sticky='w')
                            l22=Label(top,text=gender.get(),font =('Times New Roman', 13))
                            l22.grid(column=7,row=3,sticky='w',columnspan=3)
                            
                            l23=Label(top,text="Father's Name :",font =('Times New Roman', 16))
                            l23.grid(column=1,row=4,sticky='w',pady=4)
                            l24=Label(top,text=pname.get(),font =('Times New Roman', 13))
                            l24.grid(column=2,row=4,sticky='w',columnspan=3)
                            
                            l25=Label(top,text="Mother's Name :",font =('Times New Roman', 16))
                            l25.grid(column=6,row=4,sticky='w')
                            l26=Label(top,text=mname.get(),font =('Times New Roman', 13))
                            l26.grid(column=7,row=4,sticky='w',columnspan=3)
                            
                            l27=Label(top,text="Contact No. :",font =('Times New Roman', 16))
                            l27.grid(column=1,row=5,sticky='w',pady=4)
                            l28=Label(top,text=mobno.get(),font =('Times New Roman', 13))
                            l28.grid(column=2,row=5,sticky='w',columnspan=3)
                            
                            l29=Label(top,text="Email ID :",font =('Times New Roman', 16))
                            l29.grid(column=6,row=5,sticky='w')
                            l30=Label(top,text=emailid.get(),font =('Times New Roman', 13))
                            l30.grid(column=7,row=5,sticky='w',columnspan=3)
            
                            l33=Label(top,text="Religion :",font =('Times New Roman', 16))
                            l33.grid(column=1,row=6,sticky='w')
                            l34=Label(top,text=religion.get(),font =('Times New Roman', 13))
                            l34.grid(column=2,row=6,sticky='w',columnspan=3)
            
                            l35=Label(top,text="Caste :",font =('Times New Roman', 16))
                            l35.grid(column=6,row=6,sticky='w',pady=4)
                            l36=Label(top,text=caste.get(),font =('Times New Roman', 13))
                            l36.grid(column=7,row=6,sticky='w',columnspan=3)
                            def top_exit():
                                    ans=messagebox.askyesno("Exit Window","Do you want to exit window?",parent=top)
                                    if (ans):
                                            top.destroy()
                            def insert_sinfo():
                                    sql1="insert into student(Id,F_name,L_name,Gender,Class,DOB,Fathers_name,Mothers_name,Email_id,Mob_no,Caste,Religion,Blood_group,Fees_paid,Fees_Unpaid)value('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(int(sid.get()),fname.get(),lname.get(),gender.get(),clss.get(),dob,pname.get(),mname.get(),emailid.get(),int(mobno.get()),caste.get(),religion.get(),bgrp.get(),0,40000)
                                    cursor.execute(sql1)
                                    db.commit()
                                    messagebox.showinfo('Success','Record inserted successfully...',parent=top)
                                    top.destroy()
                                    db.close
            
                            l37=Label(top,text="Blood Group :",font =('Times New Roman', 16))
                            l37.grid(column=1,row=7,sticky='w')
                            l38=Label(top,text=bgrp.get(),font =('Times New Roman', 13))
                            l38.grid(column=2,row=7,sticky='w',columnspan=3)
                            b11=Button(top,text="close", command=top_exit,style='W.TButton',width=15)
                            b11.grid(column=4,row=10,padx=5,pady=10)
                            b12=Button(top,text="Confirm",command=insert_sinfo,style='W.TButton',width=15)
                            b12.grid(column=2,row=10,padx=5,pady=10)
                          
    def wExit():
            ans=messagebox.askyesno("Exit Window","Do you want to quite?",parent=w1)
            if (ans):
                w1.destroy()
            
            
    bw1=Button(w1,text="Submit",command=submit,style='W.TButton',width=15)
    bw1.grid(column=1,row=15,padx=10,pady=90,sticky='w')

    bw2=Button(w1,text="Exit",command=wExit,width=15,style='W.TButton')
    bw2.grid(column=5,row=15,padx=10,pady=90,sticky='w')

#----------------------------------------------------------------Teacher Salary-----------------------------------------------------------------------

def t_salary():
    s1=Toplevel()
    s1.title('Salary')
    s1.geometry('900x600')
    s1.resizable(0,0)
    '''s1=tk.ThemedTk()
    s1.get_themes()
    s1.set_theme("radiance")'''
    style_ss = Style()
    style_ss.configure('W.TButton', font =('Helvetica', 16, 'bold'),relief="groove",anchor='center',foreground='green')
    style_ss.configure('BW.TLabel', font =('Helvetica', 14, 'bold'),anchor='center')
    
      
    def t_ok():
        try:
            xs_tsid=int(stid.get())
        except:
            messagebox.showerror('','Only digits are allowed in Student ID',parent=s2)
        cursor.execute( "SELECT Id, COUNT(*) FROM teacher WHERE Id = %s GROUP BY Id", (int(stid.get()) ))
        row_count = cursor.rowcount
    
        if row_count == 0:
            es5.delete(0,END)
            es6.delete(0,END)
            messagebox.showerror('',' Given Teacher ID doesn\'t exists. Enter valid ID.',parent=s2)
        else:
            cursor.execute("select * from teacher where ID=%s", (int(stid.get() )))
            resl=cursor.fetchall()
            for row in resl:
                es5.delete(0,END)
                es5.insert(0,row[8])
                es6.delete(0,END)
                es6.insert(0,row[9])
            
            
      
    def update():
        try:
            x_thrs=int(thrs.get())
            x_trs=int(trs.get())       
        except:
            messagebox.showerror('','Only digits are allowed in Hours',parent=s2)
        u1=int(trs.get())*int(thrs.get())
        #if int(unpd.get()) < int(u1)
        cursor.execute("update teacher set unpaid=(unpaid+%s) where id=%s",(int(u1), int(stid.get() )))
        db.commit()
        cursor.execute("select * from teacher where ID=%s", (int(stid.get() )))
        resl=cursor.fetchall()
        for row in resl:
                es5.delete(0,END)
                es5.insert(0,row[8])
                es6.delete(0,END)
                es6.insert(0,row[9])
            
    def pay():
        try:
            x_tamt=int(tamt.get())
                  
        except:
            messagebox.showerror('','Only digits are allowed in Amount',parent=s2)
       
        cursor.execute("update teacher set Unpaid=(unpaid-%s) where id=%s",(int(tamt.get()), int(stid.get()) ))
        db.commit()
        cursor.execute("select * from teacher where ID=%s", (int(stid.get() )))
        resl=cursor.fetchall()
        for row in resl:
                es5.delete(0,END)
                es5.insert(0,row[8])
                es6.delete(0,END)
                es6.insert(0,row[9])
        es5.delete(0,END)
        es5.insert(0,int(tamt.get()))
            
    s0=Label(s1,text="Teacher Id :",style='BW.TLabel')
    s0.grid(column=0,row=1,padx=15,pady=5,sticky='w')
    es1=Entry(s1,width=20,textvariable=stid)
    es1.grid(column=1,row=1,padx=15,pady=10,sticky='w',ipadx=3,ipady=3)
    
    
    bs1=Button(s1,text="OK",command=t_ok,width=10,style='W.TButton')
    bs1.grid(column=1,row=2,padx=0,pady=25,sticky='w')
    
    s2=Label(s1,text="Hours Completed :",style='BW.TLabel')
    s2.grid(column=0,row=3,padx=15,pady=5,sticky='w')
    es2=Entry(s1,width=20,textvariable=thrs)
    es2.grid(column=1,row=3,padx=15,pady=5,sticky='w',ipadx=3,ipady=3)
    
    s3=Label(s1,text="Per Hour(Rs) :",style='BW.TLabel')
    s3.grid(column=0,row=4,padx=15,pady=5,sticky='w')
    es3=Entry(s1,width=20,textvariable=trs)
    es3.grid(column=1,row=4,padx=15 ,pady=5,sticky='w',ipadx=3,ipady=3)
    
    bs2=Button(s1,text="Update",command=update ,width=10,style='W.TButton')
    bs2.grid(column=1,row=5,padx=15,pady=30,sticky='w')
    
    s4=Label(s1,text="Amount :",style='BW.TLabel')
    s4.grid(column=0,row=6,padx=15,pady=5,sticky='w')
    es4=Entry(s1,width=20,textvariable=tamt)
    es4.grid(column=1,row=6,padx=15,pady=5,sticky='w',ipadx=3,ipady=3)
    
    bs3=Button(s1,text="Pay  :",command=pay ,width=10,style='W.TButton')
    bs3.grid(column=1,row=7,padx=15,pady=30,sticky='w')

    s5=Label(s1,text="Paid :",style='BW.TLabel',state='readonly')
    s5.grid(column=0,row=8,padx=15,pady=5,sticky='w')
    es5=Entry(s1,width=20,textvariable=pd)
    es5.grid(column=1,row=8,padx=15 ,pady=5,sticky='w',ipadx=3,ipady=3)

    s6=Label(s1,text="Unpaid :",style='BW.TLabel',state='readonly')
    s6.grid(column=0,row=9,padx=15,pady=5,sticky='w')
    es6=Entry(s1,width=20,textvariable=unpd)
    es6.grid(column=1,row=9,padx=15 ,pady=5,sticky='w',ipadx=3,ipady=3)
    
#----------------------------------------------------------------Teacher's details-----------------------------------------------------------------------    

def t_info():
    w1=Toplevel()
    '''w1=tk.ThemedTk()
    w1.get_themes()
    w1.set_theme("clearlooks")'''
    w1.title('Information')
    w1.geometry('800x800+0+0')
    w1.resizable(0,0)
    w1.config(background='white smoke')
    style2 = Style()
    style2.configure('W.TButton', font =('Helvetica', 20, 'bold'),relief="groove",anchor='center',background='black')
    style2.configure('BW2.TLabel', font =('Helvetica', 16, 'bold'),anchor='w',background='white smoke')

    def t_submit():
      global tdob
      
      global y
      if (tid.get()=='' or tlname.get()=='' or tfname.get()=='' or tedu.get()=='' or  tgender.get()=='' or tmobno.get()=='' or  temailid.get()==''):
            messagebox.showerror("Error","Please, Fill all record",parent=w1)
      else:
        y=True
        while y==True :
            try:
                    x_tsid=int(tid.get())
            except:
                    messagebox.showerror('','Only digits are allowed in Teacher ID',parent=w1)
                    break
            cursor.execute( "SELECT Id, COUNT(*) FROM teacher WHERE Id = %s GROUP BY Id", (int(tid.get())))
            if cursor.fetchone() is not None:
                    messagebox.showerror('','Invalid Username.',parent=w1)
                    break
            try:
                if (type(int(tlname.get()))) is int :
                    messagebox.showerror('','Only Alphabets are allowed in Last Name',parent=w1)
                    break
            except:
                pass
            try:
                if type(int(tfname.get())) is int:
                    messagebox.showerror('','Only Alphabets are allowed in First Name',parent=w1)
                    break
            except:
                pass
            
            try:
                    x_mob=int(tmobno.get())
            except:
                    messagebox.showerror('','Only digits are allowed in Contact Number',parent=w1)
                    break
        
       
            if not re.search(r'(^\d{10}$)',str(tmobno.get())):
                    messagebox.showerror("Error","Enter valid mobile number",parent=w1)
                    break   

            if not re.search(r'([\w.-]+)@([\w]+)\.(\w)', temailid.get()):
                    messagebox.showerror("Error","Enter valid email addressd",parent=w1)
                    break

            y=False
                        


      if y == False :
                tdob=str(tyear.get())+"-"+str(tmonth.get())+"-"+str(tday.get())
                t1="""create table if not exists teacher(Id int(10) primary key,F_name varchar(10) not null ,L_name varchar(10) not null,Gender varchar(10) not null ,Education varchar(15) not null ,DOB Date not null, Email_id varchar(20) not null,Mob_no int(20) not null, Paid int(10), Unpaid int(10))"""
                cursor.execute(t1)

                t2="insert into teacher(Id,F_name,L_name,Gender,Education,DOB,Email_id,Mob_no,Paid,Unpaid)value('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(int(tid.get()),tfname.get(),tlname.get(),tgender.get(),tedu.get(),tdob,temailid.get(),int(tmobno.get()), 0,0)
                cursor.execute(t2)
                db.commit()
                messagebox.showinfo('Success','Record inserted successfully...',parent=w1)
                db.close
    
        
             
        
    def t_Exit():
        ans=messagebox.askyesno("Exit Window","Do you want to quit?",parent=w1)
        if (ans):
            w1.destroy()

            
    lw1=Label(w1,text="      ",style='BW2.TLabel')
    lw1.grid(column=0,row=1,padx=15,pady=20)

    lw2=Label(w1,text="Teacher ID :",style='BW2.TLabel')
    lw2.grid(column=0,row=2)
    ew1=Entry(w1,width=20,textvariable=tid )
    ew1.grid(column=1,row=2,padx=0,sticky='w',ipady=3,pady=8)

    lw3=Label(w1,text="Last Name :",style='BW2.TLabel')
    lw3.grid(column=0,row=3,pady=8)

    ew2=Entry(w1,width=20,textvariable=tlname)
    ew2.grid(column=1,row=3,padx=0,sticky='w',ipady=3)

    lw4=Label(w1,text="First Name :",style='BW2.TLabel')
    lw4.grid(column=0,row=4,pady=8)
    ew3=Entry(w1,width=20,textvariable=tfname)
    ew3.grid(column=1,row=4,padx=0,sticky='w',ipady=3)

    lw5=Label(w1,text="Education :  ",style='BW2.TLabel')
    lw5.grid(column=0,row=5,pady=8)
    ew4=Entry(w1,width=20,textvariable=tedu)
    ew4.grid(column=1,row=5,padx=0,sticky='w',ipady=3)


    lw6=Label(w1,text="  Date Of Birth :",style='BW2.TLabel')
    lw6.grid(column=0,row=6,padx=15,pady=8)
    s1=Spinbox(w1,from_=1, to=31,width=4,textvariable=tday,state='readonly')
    s1.grid(column=1,row=6,padx=5,sticky='w')
    s2=Spinbox(w1,from_=1, to=12,width=4,textvariable=tmonth,state='readonly')
    s2.grid(column=1,row=6,padx=50,sticky='w')
    s3=Spinbox(w1,from_=(int(strftime("%Y"))-100), to=int(strftime("%Y")),width=6,textvariable=tyear,state='readonly')
    s3.grid(column=1,row=6,padx=96,sticky='w')
 
    lw7=Label(w1,text="Gender :       ",style='BW2.TLabel')
    lw7.grid(column=0,row=7,pady=8)
    cw3=Combobox(w1,width=17,textvariable=tgender,state='readonly')
    cw3['values']=(" ","Male","Female")
    cw3.current(0)
    cw3.grid(column=1,row=7,padx=0,sticky='w',ipady=3)

    lw10=Label(w1,text="Contact No. :",style='BW2.TLabel')
    lw10.grid(column=0,row=10,pady=8)
    ew7=Entry(w1,width=20,textvariable=tmobno)
    ew7.grid(column=1,row=10,padx=0,sticky='w',ipady=3)

    lw11=Label(w1,text="Email ID :    ",style='BW2.TLabel')
    lw11.grid(column=0,row=11,pady=8)
    ew8=Entry(w1,width=20,textvariable=temailid)
    ew8.grid(column=1,row=11,padx=0,sticky='w',ipady=3)
    
    bw1=Button(w1,text="Submit",command=t_submit,style='W.TButton',width=13)
    bw1.grid(column=0,row=15,padx=50,pady=90,sticky='w')

    bw2=Button(w1,text="Exit",command=t_Exit,width=13,style='W.TButton')
    bw2.grid(column=1,row=15,padx=50,pady=90,sticky='w')

    
#----------------------------------------------------------------Student & Teacher-----------------------------------------------------------------------


def stud():
    top=Toplevel()
    top.title('Student')
    top.geometry('900x500+0+0')
    top.resizable(0,0)
    style3 = Style()
    top.configure(background='ivory3')
    style3.configure('BW.TLabel', font =('Helvetica', 22, 'bold'),relief='sunken',anchor='center',activeforeground='red',activebackground='red',background="black",foreground='gray98')
    bt1=Button(top,text="Student_Details",style="BW.TLabel", command=s_info,width=13)
    bt1.grid(row=2,column=1,sticky='w',padx=30,pady=100,ipadx=15,ipady=15)
    bt2=Button(top,text="Attendence",style="BW.TLabel",command=attendence,width=12)
    bt2.grid(row=2,column=2,sticky='w',padx=30,pady=100,ipadx=15,ipady=15)
    bt3=Button(top,text="Result",style="BW.TLabel",command=result,width=11)
    bt3.grid(row=2,column=3,sticky='w',padx=30,pady=100,ipadx=15,ipady=15)
    bt4=Button(top,text="Fees",style="BW.TLabel",width=11,command=Fees)
    bt4.grid(row=3,column=1,padx=40,sticky='e',pady=30,ipadx=15,ipady=15)
    bt5=Button(top,text="Class",style="BW.TLabel",command=cls,width=11)
    bt5.grid(row=3,column=2,padx=40,sticky='e',pady=30,ipadx=15,ipady=15)

def teach():
    top=Toplevel()
    top.title('Teacher')
    top.geometry('500x450')
    top.resizable(0,0)
    style2 = Style()
    top.configure(background='ivory3')
    style2.configure('BW.TLabel', font =('Helvetica', 22, 'bold'),relief='sunken',anchor='center',background="black",foreground='gray98')
    
    bt1=Button(top,text="Details",style="BW.TLabel",command=t_info,width=11)
    bt1.grid(row=1,column=1,padx=110,sticky='e',pady=33,ipadx=15,ipady=15)

    bt3=Button(top,text="Payment",style="BW.TLabel",width=11,command=t_salary)
    bt3.grid(row=3,column=1,padx=110,sticky='e',pady=33,ipadx=15,ipady=15)
    
#-------------------------------------------------------------------Main Window-----------------------------------------------------------------------
def new_win():

    w=Toplevel()
    w.geometry('1550x850+0+0')
    w.title("Excellence tutorial")
    style1 = Style()
    w.resizable(0,0)
    a1=Label(w,text="   Excellence Education Tutorial   ",font="Times 40 bold",background="Blue",borderwidth=2, relief="groove",width=58,anchor="center")
    a1.grid(column=0,row=0,ipadx=0,ipady=0,columnspan=5)


    lbl = Label(w, font = ('calibri',23, 'bold'), background = 'gray', foreground = 'white',anchor="center", relief="sunken")
    lbl.grid(column=4,row=5,padx=100,ipadx=8,sticky='E')
    def time(): 
        string = strftime('%H:%M:%S %p') 
        lbl.config(text = string) 
        lbl.after(1, time)
    time()
    style1.configure('W.TButton', font =('Times New Roman', 20, 'bold'),relief="groove")

    
    canvas = Canvas(root,  width=1500, height=830)
    canvas.grid()
    img = PhotoImage(file="std.png")
    b1=Button(w,text="Student", image=img ,compound="top",width=25, style='W.TButton', command=stud)
    
    b1.image=img
   
    b1.grid(row=7,column=0,padx=65,pady=100,columnspan=2,rowspan=2)
    img1 = PhotoImage(file="teach.png")
   
    b2=Button(w,text="Teacher",image=img1,compound="top",style='W.TButton',width =25,command=teach)
    b2.image=img1
    b2.grid(row=7,column=4,padx=60,pady=20,columnspan=2,rowspan=2,sticky='W')

    img2 = PhotoImage(file="cls.png")
    
    l1=Label(w, image=img2,relief="flat")
    l1.image=img2
    l1.grid(row=10,column=2,padx=50,pady=20,columnspan=2,rowspan=2)

#-------------------------------------------------------------------------------------------------------------------------------------------

def register():
    
    top=Toplevel(root)
    top.title('Registration')
    top.geometry('450x400')
    top.resizable(0,0)
    style5 = Style()
    style5.configure('W.TButton', font =('helvetica', 15, 'bold'),relief="groove",anchor='center',foreground='green')
    RegisterFrame = Frame(top)
    RegisterFrame.grid()

    lbl_firstname = Label(RegisterFrame, text="Enter Firstname:", font=('helvetica', 15), borderwidth=18)
    lbl_firstname.grid(row=1,padx=25,pady=3,sticky="w")
    lbl_lastname = Label(RegisterFrame, text="Enter Lastname:", font=('helvetica', 15), borderwidth=18)
    lbl_lastname.grid(row=2,padx=25,pady=3,sticky="w")
    lbl_username = Label(RegisterFrame, text="Enter Username:", font=('helvetica', 15), borderwidth=18)
    lbl_username.grid(row=3,padx=25,pady=3,sticky="w")
    lbl_password = Label(RegisterFrame, text="Enter Password:", font=('helvetica', 15), borderwidth=18)
    lbl_password.grid(row=4,padx=25,pady=3,sticky="w")
    lbl_password = Label(RegisterFrame, text="Confirm Password:", font=('helvetica', 15), borderwidth=18)
    lbl_password.grid(row=5,padx=25,pady=3,sticky="w")
    
    
    firstname = Entry(RegisterFrame, font=('helvetica', 13), textvariable=FIRSTNAME, width=15)
    firstname.grid(row=1, column=1,sticky="")
    lastname = Entry(RegisterFrame, font=('helvetica', 13), textvariable=LASTNAME, width=15)
    lastname.grid(row=2, column=1,sticky="")
    username = Entry(RegisterFrame, font=('helvetica', 13), textvariable=USERNAME, width=15)
    username.grid(row=3, column=1,sticky="")
    password1 = Entry(RegisterFrame, font=('helvetica', 13), textvariable=PASSWORD1, width=15, show="*")
    password1.grid(row=4, column=1,sticky="")
    password2= Entry(RegisterFrame, font=('helvetica', 13), textvariable=PASSWORD2, width=15, show="*")
    password2.grid(row=5, column=1,sticky="")
    
    
    def ToggleToLogin(event=None):
        top.destroy()
    def c_register():
       
        sql="""create table if not exists Users(F_name varchar(15) not null ,L_name varchar(15) not null, user_name varchar(18) primary key, Password varchar(15) not null)"""
        cursor.execute(sql)
        z=True
        while z==True:
            if (PASSWORD1.get()=='' or PASSWORD2.get()=='' or FIRSTNAME.get()=='' or LASTNAME.get()=='' or  USERNAME.get()=='' ):
                messagebox.showerror("Error","Please, Fill all record",parent=top)
                break
            
            
            if (str(PASSWORD1.get()) != str(PASSWORD2.get())):
                messagebox.showerror('','Password doesn\'t match.',parent=top)
                break
            if len(str(PASSWORD2.get())) <= 5:
                messagebox.showwarning('','Password is too small.',parent=top)
                break
            cursor.execute( "SELECT user_name, COUNT(*) FROM users WHERE user_name = %s GROUP BY user_name", (str(USERNAME.get())))
            if cursor.fetchone() is not None:
                messagebox.showerror('','Invalid Username.',parent=top)
                break
            else:
                z=False
            if z==False:
                sql1="insert into Users(user_name,F_name,L_name,Password)value('{}','{}','{}','{}')".format(str(USERNAME.get()), str(FIRSTNAME.get()),str(LASTNAME.get()), str(PASSWORD2.get()))
                cursor.execute(sql1)
                db.commit()
                messagebox.showinfo('Success','Registered successfully...',parent=top)
                                    
            db.close
    
    btn_login = Button(RegisterFrame, text="Register", width=35, command=c_register, style='W.TButton')
    btn_login.grid(row=6, columnspan=2, pady=20,padx=20)
    lbl_login = Label(RegisterFrame, text="Login",  style='W.TButton')
    lbl_login.grid(row=0, sticky=W,pady=10)
    lbl_login.bind('<Button-1>', ToggleToLogin)
def login():
    
    if uname.get == "" or pwd.get() == "" or uname.get == "Enter Username" or pwd.get() == "Enter Password" :
        messagebox.showwarning('','Fill All Records',parent=root)
    else:
        cursor.execute("SELECT * FROM Users WHERE user_name = %s and password = %s", (str(uname.get()), str(pwd.get())))
        if cursor.fetchone() is not None:
            messagebox.showinfo('Success','successfully login...',parent=root)
            new_win()
        else:
            messagebox.showerror('Error','Invalid Username Or password',parent=root)


def entry_click(ent_nm,status):
    global nm_l, ps_l
    if status=="nm":
        if nm_l is True:
            ent_nm.config(foreground="black")
            ent_nm.delete(0,END)
            nm_l=False
    elif status=="ps":
        if ps_l is True:
            ent_ps.config(foreground="black")
            ent_ps.config( show="*")
            ent_ps.delete(0,END)
            ps_l=False

nm_l=True
ps_l=True

style1.configure('W.TButton', font =('Helvetica', 20, 'bold'),relief="groove",anchor='center')
label=Label(root,text="")
label.grid(row = 0,column = 0,pady=10)
ent_nm=Entry(root,textvariable=uname,width=20)
ent_nm.config(foreground='gray',font=('Helvetica', 15))
ent_nm.grid(row = 2,column = 0,padx=230,pady=20,ipady=3,ipadx=3,sticky='w')
ent_nm.insert(0,"Enter Username")
ent_nm.bind('<FocusIn>',lambda eff: entry_click(ent_nm,"nm"))

ent_ps=Entry(root,textvariable=pwd,width=20)
ent_ps.config(foreground='gray',font=('Helvetica', 15))
ent_ps.grid(row = 3,column = 0,padx=230,pady=10,ipady=3,ipadx=3,sticky='w')
ent_ps.insert(0,"Enter Password")

ent_ps.bind('<FocusIn>',lambda eff: entry_click(ent_ps,"ps"))

bt1=Button(root,text="Login",style="W.TButton",command=login,width=13)
bt1.grid(row=4,column=0,padx=90,sticky='w',pady=37,ipadx=5,ipady=5)

bt3=Button(root,text="Register",style="W.TButton",width=13,command=register)
bt3.grid(row=4,column=0,padx=400,sticky='e',pady=37,ipadx=5,ipady=5)


root.mainloop()
