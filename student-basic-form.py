from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk
window=Tk()
window.title("Student Details Submission")
window.geometry("1000x1000")
frame1=Frame(window,bg="grey",relief=SUNKEN,borderwidth=6)
frame1.pack(side=TOP,fill="x")
txt1=Label(frame1,text="Student details form",font="algerian 16 bold",fg="black",bg="white")
txt1.pack()
frame2=Frame(window,bg="green",relief=SUNKEN,borderwidth=7,height=37)
frame2.place(x=0,y=42)

course_list=Listbox(frame2,bg="grey",height=38)
course_list.insert(1, "Python")
course_list.insert(2, "Java")
course_list.insert(3, "C")
course_list.insert(4, "C++")
course_list.insert(5, "JavaScript")
course_list.insert(6, "HTML")
course_list.insert(7, "CSS")
course_list.insert(8, "SQL")
course_list.insert(9, "PHP")
course_list.insert(10, "C#")
course_list.insert(11, "Data Science")
course_list.insert(12, "Machine Learning")
course_list.insert(13, "Web Development")
course_list.insert(14, "App Development")
course_list.insert(15, "Cyber Security")
course_list.insert(16, "Cloud Computing")
course_list.insert(17, "Networking")
course_list.insert(18, "Database Management")
course_list.insert(19, "MS Office")
course_list.insert(20, "Graphic Designing")
course_list.insert(21, "R Programming")
course_list.insert(22, "Kotlin")
course_list.insert(23, "Swift")
course_list.insert(24, "Go")
course_list.insert(25, "Rust")
course_list.insert(26, "Ruby")
course_list.insert(27, "Django")
course_list.insert(28, "React.js")
course_list.insert(29, "Node.js")
course_list.insert(30, "Artificial Intelligence")
course_list.insert(31, "Deep Learning")
course_list.insert(32, "Ethical Hacking")
course_list.insert(33, "DevOps")
course_list.insert(34, "UI/UX Design")
course_list.insert(35, "Computer Hardware")
course_list.pack(pady=(32,0))
course=""

def select_course():
    global course
    selected=course_list.curselection()
    if selected:
        course=course_list.get(selected[0])
        messagebox.showinfo("Selected course",course)
    else:
        messagebox.showwarning("Warning","Select a course!")

button_frame2=Button(frame2,text="Select Course",command=select_course)
button_frame2.place(x=15,y=605)

txt_courses=Label(frame2,text="Courses",font="algerian 14 bold",bg="cyan",width=7)
txt_courses.place(x=13,y=0)
frame3=Frame(window,bg="green",relief=SUNKEN,borderwidth=6)
frame3.place(x=250,y=200,width=250,height=35)
name_lbl=Label(frame3,text="Name:",font="Arial,13,bold",bg="green",fg="black",anchor="w")
name_lbl.place(x=0,y=0)
name_widget=Entry(frame3,width=30)
name_widget.place(x=51,y=3)

frame4=Frame(window,bg="green",relief=SUNKEN,borderwidth=6)
frame4.place(x=700,y=200,width=240,height=35)
age_var=StringVar()
age_combobox=ttk.Combobox(frame4,textvariable=age_var,state="readonly")
age_combobox['values']=[str(i) for i in range(18,25)]
age_combobox.place(x=70,y=0)
age_lbl=Label(frame4,text="Age:",font="Arial,13,bold",bg="green",fg="black",anchor="w")
age_lbl.place(x=0,y=0)

frame5=Frame(window,bg="green",relief=SUNKEN,borderwidth=6)
frame5.place(x=210,y=400,width=320,height=35)
mob_num=Entry(frame5,width=30)
mob_num.place(x=115,y=3)
mob_num_lbl=Label(frame5,text="Phone Number:",font="Arial,13,bold",bg="green",fg="black",anchor="w")
mob_num_lbl.place(x=0,y=0)

frame6=Frame(window,bg="green",relief=SUNKEN,borderwidth=6)
frame6.place(x=620,y=400,width=340,height=130)
address_widget=Text(frame6,width=30,height=7)
address_widget.place(x=70,y=3)
address_lbl=Label(frame6,text="Address:",font="Arial,13,bold",bg="green",fg="black",anchor="w")
address_lbl.place(x=0,y=0)

image=Image.open("academy-logo.png")
image=image.resize((120,120))
photo=ImageTk.PhotoImage(image)
photo_lbl=Label(window,image=photo,bg="white")
photo_lbl.place(x=530,y=240)
def validate():
    name=name_widget.get().strip()
    age=age_var.get()
    num=mob_num.get().strip()
    address=address_widget.get("1.0",END).strip().replace("\n"," ")
    if name=="" and age=="" and num=="" and address=="" and course=="":
        messagebox.showwarning("Warning","Please fill all fields!")
    elif name=="":
        messagebox.showwarning("Warning","Name Field is empty!")
    elif age=="":
        messagebox.showwarning("Warning","Age Field is empty!")
    elif num=="":
        messagebox.showwarning("Warning","Phone Number Field is empty!")
    elif address=="":
        messagebox.showwarning("Warning","Address Field is empty!")    
    elif course=="":
        messagebox.showwarning("Warning","Select a course!")
    elif age not in [str(i) for i in range(18,25)]:
        messagebox.showwarning("Warning","Please enter a valid age!")
    else:
        with open("students.txt","a") as file:
            file.write(f"{name}\t{age}\t{course}\t{num}\t{address}\n")
        messagebox.showinfo("Success","Student Registered Successfully.")
        window.destroy()   

button2=Button(window,text="Submit",command=validate)
button2.place(x=600,y=600)
window.mainloop()