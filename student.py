from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

    # Img 1
        img = Image.open(
            r"C:\Users\Vignesh\Desktop\Face-Recognition-System\images\face.png")
        img = img.resize((550, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

    # Img 2
        img1 = Image.open(
            r"C:\Users\Vignesh\Desktop\Face-Recognition-System\images\img.png")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=500, y=0, width=500, height=130)

    # Img 3
        img3 = Image.open(
            r"C:\Users\Vignesh\Desktop\Face-Recognition-System\images\face.png")
        img3 = img3.resize((500, 130), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=1000, y=0, width=550, height=130)

    # bg Image
        img4 = Image.open(
            r"C:\Users\Vignesh\Desktop\Face-Recognition-System\images\face.png")
        img4 = img4.resize((1530, 710), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(
            bg_img, text="Student Management System", font=("time new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=55, width=1480, height=600)

    # left Frame
        Left_frame = LabelFrame(
            main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=730, height=580)

        img_left = Image.open(
            r"C:\Users\Vignesh\Desktop\Face-Recognition-System\images\img.png")
        img_left = img_left.resize((720, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)

    # Current Course
        current_course_frame = LabelFrame(
            Left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=135, width=720, height=150)

    # Department
        dep_label = Label(current_course_frame, text="Department",
                          font=("times new roman", 13, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame,
                                 font=("times new roman", 13, "bold"), state="readonly", width=20)
        dep_combo["values"] = ("Select Department",
                               "Computer", "IT", "Civil", "Mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

    # Course
        course_label = Label(current_course_frame, text="Course",
                             font=("times new roman", 13, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame,
                                    font=("times new roman", 13, "bold"), state="readonly", width=20)
        course_combo["values"] = ("Select Course",
                                  "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

    # Year
        year_label = Label(current_course_frame, text="Year",
                           font=("times new roman", 13, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame,
                                  font=("times new roman", 13, "bold"), state="readonly", width=20)
        year_combo["values"] = ("Select Year",
                                "2022-23", "2023-24", "2024-25", "2025-26")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

    # Semester
        semester_label = Label(current_course_frame, text="Semester",
                               font=("times new roman", 13, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame,
                                      font=("times new roman", 13, "bold"), state="readonly", width=20)
        semester_combo["values"] = ("Select Semester",
                                    "Semester-1", "Semester-2", "Semester-3", "Semester-4")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

    # Class Student Information
        class_Studdent_frame = LabelFrame(
            Left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student  Information", font=("times new roman", 12, "bold"))
        class_Studdent_frame.place(x=5, y=250, width=720, height=300)

    # Student Id
        studentId_label = Label(class_Studdent_frame, text="StudentID: ",
                                font=("times new roman", 13, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        studentID_entry = ttk.Entry(class_Studdent_frame,
                                    width=20, font=("times new roman", 13, "bold"))
        studentID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

    # Right Frame
        Right_frame = LabelFrame(
            main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=750, y=10, width=720, height=580)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
