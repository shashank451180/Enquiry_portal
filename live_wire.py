from tkinter import *                       #tkinter library
from datetime import *                      #Datetime library
import sqlite3
from tkinter import messagebox
db=sqlite3.connect("live_wire.db")
c=db.cursor()


date=datetime.now().date()                  #object for date
date=str(date)

class Application(object):                      #object is used here as arbitary argument
    def __init__(self, master):
        self.master=master

        #frames
        self.top=Frame(master, height=150, bg="white")          #top frame
        self.top.pack(fill=X)

        self.bottom=Frame(master, height=500, bg="#34baeb")     #bottom frame
        self.bottom.pack(fill=X)

        #top frame design
        self.top_image=PhotoImage(file="img/LWR.png")   #image
        self.top_image_label=Label(self.top, image=self.top_image, bg="white")
        self.top_image_label.place(x=170, y=10)

        self.date_lbl=Label(self.top, text=date, font="verdana 12", bg="white")
        self.date_lbl.place(x=700,y=120)

        #bottom frame design

        #button1=Feedback
        self.photo_fb = PhotoImage(file=r"img\fb.png")
        self.fb_button = Button(self.bottom, text="   Feedback form    ",bg="white", fg="#34baeb" , font="verdana 15 bold", image=self.photo_fb,compound=LEFT ,command=self.feedback)
        self.fb_button.place(x=270, y=70)

        #button2=Enquiry
        self.photo_en = PhotoImage(file=r"img\enquiry.png")
        self.en_button = Button(self.bottom, text="     Enquiry form     ", bg="white",fg="#34baeb",font="verdana 15 bold",image=self.photo_en,compound=LEFT ,command=self.enquiry)
        self.en_button.place(x=270, y=200)


        #button3=Course details
        self.photo_cd = PhotoImage(file=r"img\cd.png")
        self.cd_button = Button(self.bottom, text="    Course details    ", bg="white",fg="#34baeb",font="verdana 15 bold",image=self.photo_cd,compound=LEFT ,command=self.course)
        self.cd_button.place(x=270, y=330)



    def feedback(self):
        fb_form=Feedback()

    def enquiry(self):
        enq=Enquiry()

    def course(self):
        cd=Course_details()

        



class Feedback(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("1400x800+0+0")
        self.title("Feedback form")
        self.minsize(width=1400, height=800)

        self.top = Frame(self, height=150, bg="white")  # top frame
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=650, bg="#34baeb")  # bottom frame
        self.bottom.pack(fill=X)

        # top frame design
        self.top_image = PhotoImage(file="img/fb1.png")  # image
        self.top_image_label = Label(self.top, image=self.top_image, bg="white")
        self.top_image_label.place(x=350, y=10)

        self.heading = Label(self.top, text="Feedback Form", font="verdana 25 bold", bg="white",
                             fg="#34baeb")  # heading
        self.heading.place(x=550, y=60)

        # name
        self.label_name = Label(self.bottom, text="FULL NAME", font="verdana 13 bold", fg="white", bg="#34baeb")
        self.label_name.place(x=20, y=20)
        self.entry_name = Entry(self.bottom, width=40, bd=2)
        self.entry_name.place(x=230, y=20)

        # course
        self.label_course = Label(self.bottom, text="COURSE", font="verdana 13 bold", fg="white", bg="#34baeb")
        self.label_course.place(x=20, y=70)

        self.ds = StringVar(self.bottom)
        self.ds.set("            data-science                    ") # default value
        data_science = OptionMenu(self.bottom, self.ds, "Machine Learning", "Artificial Intelligence", "Data science using Python", "Data science using R, SAS, SPSS", "IOT")
        data_science.place(x=230, y=70)

        self.it = StringVar(self.bottom)
        self.it.set("                        IT                             ") # default value
        it = OptionMenu(self.bottom, self.it, "Linux Administrator", "Networking & Network Security", "Cloud Computing", "Ethical Hacking")
        it.place(x=480, y=70)

        self.pl = StringVar(self.bottom)
        self.pl.set("      Programming Languages    ") # default value
        pl = OptionMenu(self.bottom, self.pl, "Python+Django", "Core java+Advance Java", "Mean Stack Development","Python Programming")
        pl.place(x=730, y=70)

        self.eda = StringVar(self.bottom)
        self.eda.set("                        EDA                        ") # default value
        eda = OptionMenu(self.bottom, self.eda, "Embedded system+PCB design", "Embedded system+Python", "Embedded system+IOT", "Autocad Electrical", "Matlab Advance")
        eda.place(x=980, y=70)

      
        # Knowledge on technology before joining course(on the scale of 10)
        self.label_before = Label(self.bottom, text="Knowledge on technology before joining course", font="verdana 13 bold", fg="white", bg="#34baeb")
        self.label_before.place(x=20, y=120)
        self.scale_before= Scale(self.bottom, from_=0, to=10, orient=HORIZONTAL, fg="red")
        self.scale_before.place(x=500, y=120)
        
        # Knowledge on technology after joining course(on the scale of 10)
        self.label_after= Label(self.bottom, text="Knowledge on technology after joining course", font="verdana 13 bold", fg="white", bg="#34baeb")
        self.label_after.place(x=720, y=120)
        self.scale_after= Scale(self.bottom, from_=0, to=10, orient=HORIZONTAL, fg="red")
        self.scale_after.place(x=1200, y=120)

        #Instructor knowledge on the subject:
        self.f1=StringVar()
        self.l1=Label(self.bottom,text="Instructor knowledge on the subject:", font="verdana 13 bold", fg="white", bg="#34baeb")
        self.l1.place(x=20,y=170)

        self.r1=Radiobutton(self.bottom, text='Excellent', value="Excellent",variable=self.f1, font="verdana 13 bold", bg="#34baeb")
        self.r1.place(x=500,y=170)

        self.r2=Radiobutton(self.bottom, text='Very Good', value="Very Good",variable=self.f1, font="verdana 13 bold",  bg="#34baeb")
        self.r2.place(x=650,y=170)

        self.r3=Radiobutton(self.bottom, text='Good', value="Good",variable=self.f1, font="verdana 13 bold",  bg="#34baeb")
        self.r3.place(x=830,y=170)

        self.r4=Radiobutton(self.bottom, text='Average', value="Average",variable=self.f1, font="verdana 13 bold", bg="#34baeb")
        self.r4.place(x=950,y=170)

        #Handling of queries by the instructor:
        self.f2=StringVar()
        self.l2=Label(self.bottom,text="Handling of queries by the instructor:", font="verdana 13 bold", fg="white", bg="#34baeb")
        self.l2.place(x=20,y=220)

        self.r5=Radiobutton(self.bottom, text='Excellent', value="Excellent",variable=self.f2, font="verdana 13 bold", bg="#34baeb")
        self.r5.place(x=500,y=220)

        self.r6=Radiobutton(self.bottom, text='Very Good', value="Very Good",variable=self.f2, font="verdana 13 bold", bg="#34baeb")
        self.r6.place(x=650,y=220)

        self.r7=Radiobutton(self.bottom, text='Good', value="Good",variable=self.f2, font="verdana 13 bold", bg="#34baeb")
        self.r7.place(x=830,y=220)

        self.r8=Radiobutton(self.bottom, text='Average', value="Average",variable=self.f2, font="verdana 13 bold", bg="#34baeb")
        self.r8.place(x=950,y=220)

        #Effectiveness of communication:
        self.f3=StringVar()
        self.l3=Label(self.bottom,text="Effectiveness of communication:", font="verdana 13 bold", fg="white", bg="#34baeb")
        self.l3.place(x=20,y=270)

        self.r9=Radiobutton(self.bottom, text='Excellent', value="Excellent",variable=self.f3, font="verdana 13 bold", bg="#34baeb")
        self.r9.place(x=500,y=270)

        self.r10=Radiobutton(self.bottom, text='Very Good', value="Very Good",variable=self.f3, font="verdana 13 bold", bg="#34baeb")
        self.r10.place(x=650,y=270)

        self.r11=Radiobutton(self.bottom, text='Good', value="Good",variable=self.f3, font="verdana 13 bold", bg="#34baeb")
        self.r11.place(x=830,y=270)

        self.r12=Radiobutton(self.bottom, text='Average', value="Average",variable=self.f3, font="verdana 13 bold", bg="#34baeb")
        self.r12.place(x=950,y=270)

        #Courseware feedback:
        self.f4=StringVar()
        self.l4=Label(self.bottom,text="Courseware feedback:", font="verdana 13 bold", fg="white", bg="#34baeb")
        self.l4.place(x=20,y=320)

        self.r13=Radiobutton(self.bottom, text='Excellent', value="Excellent",variable=self.f4, font="verdana 13 bold", bg="#34baeb")
        self.r13.place(x=500,y=320)

        self.r14=Radiobutton(self.bottom, text='Very Good', value="Very Good",variable=self.f4, font="verdana 13 bold",bg="#34baeb")
        self.r14.place(x=650,y=320)

        self.r15=Radiobutton(self.bottom, text='Good', value="Good",variable=self.f4, font="verdana 13 bold", bg="#34baeb")
        self.r15.place(x=830,y=320)

        self.r16=Radiobutton(self.bottom, text='Average', value="Average",variable=self.f4, font="verdana 13 bold",  bg="#34baeb")
        self.r16.place(x=950,y=320)

        #Session coordination/timely completion:
        self.f5=StringVar()
        self.l1=Label(self.bottom,text="Session coordination/timely completion:", font="verdana 13 bold", fg="white", bg="#34baeb")
        self.l1.place(x=20,y=370)

        self.r17=Radiobutton(self.bottom, text='Excellent', value="Excellent",variable=self.f5, font="verdana 13 bold", bg="#34baeb")
        self.r17.place(x=500,y=370)

        self.r18=Radiobutton(self.bottom, text='Very Good', value="Very Good",variable=self.f5, font="verdana 13 bold", bg="#34baeb")
        self.r18.place(x=650,y=370)

        self.r19=Radiobutton(self.bottom, text='Good', value="Good",variable=self.f5, font="verdana 13 bold", bg="#34baeb")
        self.r19.place(x=830,y=370)

        self.r20=Radiobutton(self.bottom, text='Average', value="Average",variable=self.f5, font="verdana 13 bold", bg="#34baeb")
        self.r20.place(x=950,y=370)


        # Best thing about us:
        self.label_about = Label(self.bottom, text="Best thing about us:", font="verdana 13 bold", fg="white", bg="#34baeb")
        self.label_about.place(x=20, y=420)
        self.entry_about = Text(self.bottom, width=80, height=3)
        self.entry_about.place(x=500, y=420)

        # Things we should improve:
        self.label_improve = Label(self.bottom, text="Things we should improve:", font="verdana 13 bold", fg="white", bg="#34baeb")
        self.label_improve.place(x=20, y=500)
        self.entry_improve = Text(self.bottom, width=80, height=3)
        self.entry_improve.place(x=500, y=500)

        # button
        self.photo_sub = PhotoImage(file=r"img\submit.png")

        self.save_button = Button(self.bottom, text="      Submit      ", font="verdana 13 bold", bg="white", fg="#34baeb",
                                  bd=2, image=self.photo_sub,compound=LEFT , command=self.feed_back)
        self.save_button.place(x=600, y=580)
        
    def feed_back(self):
        name = self.entry_name.get()
        course_ds= self.ds.get()
        course_it= self.it.get()
        course_pl= self.pl.get()
        course_eda= self.eda.get()
        before= self.scale_before.get()
        after= self.scale_after.get()
        instructor=self.f1.get()
        handle=self.f2.get()
        communication=self.f3.get()
        courseware=self.f4.get()
        timely=self.f5.get()
        about = self.entry_about.get(1.0, 'end-1c')
        improve = self.entry_improve.get(1.0, 'end-1c')

        if name and about and improve != "":
            c.execute(
                "insert into 'feedback' (name, data_structure, it, prog_lang, eda, before, after, instructor, handle, communication, courseware, timely, about, improve) values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                    name, course_ds, course_it, course_pl, course_eda, before, after, instructor, handle, communication, courseware, timely, about, improve ))
            db.commit()
            self.bottom.destroy()
            messagebox.showinfo("success", "feedback sent")
        else:
            messagebox.showerror("error", "fill all the fields", icon="warning")






class Enquiry(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("1400x800+0+0")
        self.title("Enquiry form")
        self.minsize(width=1400, height=800)

        self.top = Frame(self, height=150, bg="white")  # top frame
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=650, bg="#34baeb")  # bottom frame
        self.bottom.pack(fill=X)

        # top frame design
        self.top_image = PhotoImage(file="img/en1.png")  # image
        self.top_image_label = Label(self.top, image=self.top_image, bg="white")
        self.top_image_label.place(x=350, y=10)

        self.heading = Label(self.top, text="Enquiry Form", font="verdana 25 bold", bg="white",
                             fg="#34baeb")  # heading
        self.heading.place(x=550, y=60)

        # name
        self.label_name = Label(self.bottom, text="FULL NAME", font="verdana 13 bold", fg="white", bg="#34baeb")
        self.label_name.place(x=20, y=20)
        self.entry_name = Entry(self.bottom, width=40, bd=2)
        self.entry_name.place(x=250, y=20)

        # email
        self.label_email = Label(self.bottom, text="EMAIL ID", font="verdana 13 bold", fg="white", bg="#34baeb")
        self.label_email.place(x=20, y=70)
        self.entry_email = Entry(self.bottom, width=40, bd=2)
        self.entry_email.place(x=250, y=70)

        # phone
        self.label_phone = Label(self.bottom, text="PHONE NO", font="verdana 13 bold", fg="white", bg="#34baeb")
        self.label_phone.place(x=20, y=120)
        self.entry_phone = Entry(self.bottom, width=40, bd=2)
        self.entry_phone.place(x=250, y=120)

        # course
        self.label_course = Label(self.bottom, text="COURSE INTERESTED", font="verdana 13 bold", fg="white", bg="#34baeb")
        self.label_course.place(x=20, y=170)

        self.ds = StringVar(self.bottom)
        self.ds.set("            data-science                    ") # default value
        data_science = OptionMenu(self.bottom, self.ds, "Machine Learning", "Artificial Intelligence", "Data science using Python", "Data science using R, SAS, SPSS", "IOT")
        data_science.place(x=250, y=170)

        self.it = StringVar(self.bottom)
        self.it.set("                        IT                             ") # default value
        it = OptionMenu(self.bottom, self.it, "Linux Administrator", "Networking & Network Security", "Cloud Computing", "Ethical Hacking")
        it.place(x=500, y=170)

        self.pl = StringVar(self.bottom)
        self.pl.set("      Programming Languages    ") # default value
        pl = OptionMenu(self.bottom, self.pl    , "Python+Django", "Core java+Advance Java", "Mean Stack Development","Python Programming")
        pl.place(x=750, y=170)

        self.eda = StringVar(self.bottom)
        self.eda.set("                        EDA                        ") # default value
        eda = OptionMenu(self.bottom, self.eda, "Embedded system+PCB design", "Embedded system+Python", "Embedded system+IOT", "Autocad Electrical", "Matlab Advance")
        eda.place(x=1000, y=170)

        # qualifications
        self.label_qualification = Label(self.bottom, text="QUALIFICATION", font="verdana 13 bold", fg="white", bg="#34baeb")
        self.label_qualification.place(x=20, y=220)
        self.entry_qualification = Entry(self.bottom, width=40, bd=2)
        self.entry_qualification.place(x=250, y=220)

        # college
        self.label_college = Label(self.bottom, text="COLLEGE NAME", font="verdana 13 bold", fg="white", bg="#34baeb")
        self.label_college.place(x=20, y=270)
        self.entry_college = Entry(self.bottom, width=40, bd=2)
        self.entry_college.place(x=250, y=270)


        # batch
        self.f1=StringVar()
        self.label_batch = Label(self.bottom, text="BATCH PREFERRENCE", font="verdana 13 bold", fg="white", bg="#34baeb")
        self.label_batch.place(x=20, y=320)

        self.r1=Radiobutton(self.bottom, text='Weekdays', value="Weekdays",variable=self.f1, font="verdana 13 bold", bg="#34baeb")
        self.r1.place(x=350,y=320)

        self.r2=Radiobutton(self.bottom, text='Weekend', value="Weekend",variable=self.f1, font="verdana 13 bold", bg="#34baeb")
        self.r2.place(x=550,y=320)


        #When you want to start:
        self.f2=StringVar()
        self.label_batch = Label(self.bottom, text="WHEN YOU WANT TO START", font="verdana 13 bold", fg="white", bg="#34baeb")
        self.label_batch.place(x=20, y=370)

        self.r1=Radiobutton(self.bottom, text='Within Week', value="Within_Week",variable=self.f2, font="verdana 13 bold", bg="#34baeb")
        self.r1.place(x=350,y=370)

        self.r2=Radiobutton(self.bottom, text='Within Month', value="Within_Month",variable=self.f2, font="verdana 13 bold", bg="#34baeb")
        self.r2.place(x=550,y=370)

        #From where you come to know about livewire:
        self.f3=StringVar()
        self.l2=Label(self.bottom,text="FROM WHERE YOU COME TO KNOW ABOUT LIVEWIRE", font="verdana 13 bold", fg="white", bg="#34baeb")
        self.l2.place(x=20,y=420)

        self.r3=Radiobutton(self.bottom, text='internet', value="internet",variable=self.f3, font="verdana 13 bold", bg="#34baeb")
        self.r3.place(x=700,y=420)

        self.r4=Radiobutton(self.bottom, text='Friends', value="Friends",variable=self.f3, font="verdana 13 bold", bg="#34baeb")
        self.r4.place(x=830,y=420)

        self.r5=Radiobutton(self.bottom, text='Advertise', value="Advertise",variable=self.f3, font="verdana 13 bold", bg="#34baeb")
        self.r5.place(x=950,y=420)

        self.r6=Radiobutton(self.bottom, text='Any other', value="Other",variable=self.f3, font="verdana 13 bold", bg="#34baeb")
        self.r6.place(x=1080,y=420)


        #What is the biggest concern which made you to take up this training?
        self.label_concern = Label(self.bottom, text="What is the biggest concern which made you to take up this training?", font="verdana 13 bold", fg="white", bg="#34baeb")
        self.label_concern.place(x=20, y=470)
        self.entry_concern = Text(self.bottom, width=80, height=3)
        self.entry_concern.place(x=700, y=460)

        #How do you think training program will help you achieve your goal?
        self.label_help = Label(self.bottom, text="How do you think training program will help you achieve your goal?", font="verdana 13 bold", fg="white", bg="#34baeb")
        self.label_help.place(x=20, y=530)
        self.entry_help = Text(self.bottom, width=80, height=3)
        self.entry_help.place(x=700, y=520)

        # button
        self.photo_sub = PhotoImage(file=r"img\submit.png")

        self.save_button = Button(self.bottom, text="      Submit      ", font="verdana 13 bold", bg="white", fg="#34baeb",
                                  bd=2, image=self.photo_sub,compound=LEFT , command=self.enquiry_form)
        self.save_button.place(x=600, y=580)

        
    def enquiry_form(self):
        name= self.entry_name.get()
        email= self.entry_email.get()
        phone= self.entry_phone.get()
        course_ds= self.ds.get()
        course_it= self.it.get()
        course_pl= self.pl.get()
        course_eda= self.eda.get()
        qualification= self.entry_qualification.get()
        college=self.entry_college.get()
        batch=self.f1.get()
        whenn=self.f2.get()
        wheree=self.f3.get()
        concern=self.entry_concern.get(1.0, 'end-1c')
        helpp=self.entry_help.get(1.0, 'end-1c')

        if name and email and phone != "":
            if len(phone) != 10:
                messagebox.showinfo("Error", "enter valid phone number", icon="warning")

            elif "@" not in email:
                messagebox.showinfo("Error", "enter valid email id", icon="warning")

            elif ".com" not in email:
                messagebox.showinfo("Error", "enter valid email id", icon="warning")

            else:
                c.execute(
                    "insert into 'enquiry' (name,email,phone,data_science, it, prog_lang, eda,qualification, college, batch, whenn, wheree, concern, help) values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                        name,email, phone,course_ds, course_it, course_pl, course_eda,qualification,college, batch, whenn, wheree, concern, helpp))
                db.commit()
                self.bottom.destroy()
                messagebox.showinfo("success", "Enquiry Submitted")
                
        else:
            messagebox.showerror("error", "fill all the fields", icon="warning")

        

def main():
    root=Tk()                                   #created object
    app=Application(root)                       #application class is called here and properties of root are passed
    root.title("LIVEWIRE")                     #title for window
    root.geometry("800x650+100+50")            #size of window
    root.resizable(False,False)                 #size should not vary

    root.mainloop()                             #to stop  this window on main window


main()
