from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student


class Face_Recongnition_Sytem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x7900+0+0")
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
            bg_img, text="Face Recognition Attendance System Software", font=("time new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

    # student Button
        img5 = Image.open(
            r"C:\Users\Vignesh\Desktop\Face-Recognition-System\images\icon.png")
        img5 = img5.resize((220, 220), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5,
                    command=self.student_details, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2", font=(
            "time new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)

    # Detect Face Button
        img6 = Image.open(
            r"C:\Users\Vignesh\Desktop\Face-Recognition-System\images\icon.png")
        img6 = img6.resize((220, 220), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2")
        b1.place(x=500, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Face Detector", cursor="hand2", font=(
            "time new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=500, y=300, width=220, height=40)

    # Attendance Face Button
        img7 = Image.open(
            r"C:\Users\Vignesh\Desktop\Face-Recognition-System\images\icon.png")
        img7 = img7.resize((220, 220), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2")
        b1.place(x=800, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Attendance", cursor="hand2", font=(
            "time new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=800, y=300, width=220, height=40)

    # Help Button
        img8 = Image.open(
            r"C:\Users\Vignesh\Desktop\Face-Recognition-System\images\icon.png")
        img8 = img8.resize((220, 220), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2")
        b1.place(x=1100, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Help Desk", cursor="hand2", font=(
            "time new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1100, y=300, width=220, height=40)

    # Train Button
        img9 = Image.open(
            r"C:\Users\Vignesh\Desktop\Face-Recognition-System\images\icon.png")
        img9 = img9.resize((220, 220), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9, cursor="hand2")
        b1.place(x=200, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Train Data", cursor="hand2", font=(
            "time new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=580, width=220, height=40)

    # Photos Button
        img10 = Image.open(
            r"C:\Users\Vignesh\Desktop\Face-Recognition-System\images\icon.png")
        img10 = img10.resize((220, 220), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10, cursor="hand2")
        b1.place(x=500, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Photos Data", cursor="hand2", font=(
            "time new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=500, y=580, width=220, height=40)

    # Developer Button
        img11 = Image.open(
            r"C:\Users\Vignesh\Desktop\Face-Recognition-System\images\icon.png")
        img11 = img11.resize((220, 220), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11, cursor="hand2")
        b1.place(x=800, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Developer", cursor="hand2", font=(
            "time new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=800, y=580, width=220, height=40)

    # Exit Button
        img12 = Image.open(
            r"C:\Users\Vignesh\Desktop\Face-Recognition-System\images\icon.png")
        img12 = img12.resize((220, 220), Image.LANCZOS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        b1 = Button(bg_img, image=self.photoimg12, cursor="hand2")
        b1.place(x=1100, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Exit", cursor="hand2", font=(
            "time new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1100, y=580, width=220, height=40)

    # ============ function buttons ============
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recongnition_Sytem(root)
    root.mainloop()
