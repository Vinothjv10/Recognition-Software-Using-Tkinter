from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Face_recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(
            self.root, text="FACE RECONGNITION", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # ========= Top ==========

        img_top = Image.open(
            r"images\face.png")
        img_top = img_top.resize((650, 700), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)

        # ========== Bottom ============

        img_bottom = Image.open(
            r"images\face.png")
        img_bottom = img_bottom.resize((950, 700), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=55, width=950, height=700)

        # ============ Buttton=====================

        b1_1 = Button(f_lbl, text="Face Recognition", command=self.face_recog, cursor="hand2", font=(
            "time new roman", 18, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=365, y=620, width=200, height=40)

        # =============face recognition ===============
    def face_recog(self):
        def draw_boundray(img, classifer, scaleFactor, minNeighbors, color, test, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifer.detectMultiScale(
                gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost",
                                               database="student_data",
                                               user="root",
                                               password="vinothJV10@")
                my_cursor = conn.cursor()

                my_cursor.execute(
                    "select Name from student where Student_id="+str(id))
                n = my_cursor.fetchone()
                n = str(n)
                # n = "+".join(n)

                my_cursor.execute(
                    "select Roll from student where Student_id="+str(id))
                r = my_cursor.fetchone()
                r = str(r)
                # r = "+".join(r)

                my_cursor.execute(
                    "select Dep from student where Student_id="+str(id))
                d = my_cursor.fetchone()
                d = str(d)
                # d = "+".join(d)

                # if n == "None" or r == "None" or d == "None":
                #     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)

                #     cv2.putText(img, "Unknown Face", (x, y-55),
                #                 cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                if confidence > 77:
                    cv2.putText(
                        img, f"Roll:{r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(
                        img, f"Name:{n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(
                        img, f"Department :{d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(
                        img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundray(
                img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier(
            "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To face Recognition", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition(root)
    root.mainloop()
