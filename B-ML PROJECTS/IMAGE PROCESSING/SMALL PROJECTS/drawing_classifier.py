import pickle
import os.path

import tkinter.messagebox
from tkinter import *
from tkinter import simpledialog, filedialog

import numpy as np
import PIL
import PIL.Image, PIL.ImageDraw
import cv2 as cv

from sklearn.svm import LinearSVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

class DrawingClassifier:
    def __init__(self):
        self.class1, self.class2, self.class3 = None, None, None
        self.class1_counter, self.class2_counter, self.class3_counter = None, None, None
        self.clf = None
        self.proj_name = None
        self.root = None
        self.image1 = None

        self.status_label = None
        self.canvas = None
        self.draw = None

        self.brush_weight = 15
        self.classes_prompt()
        self.init_gui()

    def classes_prompt(self):
        msg = Tk()
        msg.withdraw()

        self.proj_name = simpledialog.askstring("Project Name", "Please enter your project name down below!", parent = msg)
        if os.path.exists(self.proj_name):
            with open(f"{self.proj_name}/{self.proj_name}_data.pickle", "rb") as f:
                data = pickle.load(f)
            self.class1 = data["c1"]
            self.class1 = data["c2"]
            self.class1 = data["c3"]

            self.class1_counter = data["c1c"]
            self.class2_counter = data["c2c"]
            self.class3_counter = data["c3c"]
            self.clf = data["clf"]
            self.proj_name = data["pname"]

        else:
            self.class1 = simpledialog.askstring("Class1", "What is the first class called", parent = msg)
            self.class2 = simpledialog.askstring("Class2", "What is the second class called", parent = msg)
            self.class3 = simpledialog.askstring("Class3", "What is the third class called", parent = msg)


            self.class1_counter = 1
            self.class2_counter = 1
            self.class3_counter = 1

            self.clf = LinearSVC()

            os.mkdir(self.proj_name)
            os.chdir(self.proj_name)
            os.mkdir(self.class1)
            os.mkdir(self.class2)
            os.mkdir(self.class3)
            os.chdir("..")

    def init_gui(self):
        WIDTH = 500
        HEIGHT = 500
        WHITE = (255, 255, 255)

        self.root = Tk()
        self.root.title(f"NixAI Drawing Classifier Gamma v0.4 - {self.proj_name}")

        self.canvas = Canvas(self.root, width=WIDTH-10, height=HEIGHT-10, bg="white")
        self.canvas.pack(expand=YES, fill=BOTH)
        self.canvas.bind("<B1-Motion>", self.paint)

        self.image1 = PIL.Image.new("RGB", (WIDTH, HEIGHT), WHITE)
        self.draw = PIL.ImageDraw.Draw(self.image1)

        btn_frame = tkinter.Frame(self.root)
        btn_frame.pack(fill=X, side=BOTTOM)
        btn_frame.columnconfigure(0, weight=1)
        btn_frame.columnconfigure(1, weight=1)
        btn_frame.columnconfigure(2, weight=1)

        class1_btn = Button(btn_frame, text = self.class1, command = lambda: self.save(1))
        class1_btn.grid(row=0, column=0, sticky=W + E)

        class2_btn = Button(btn_frame, text=self.class2, command=lambda: self.save(2))
        class2_btn.grid(row=0, column=1, sticky=W + E)

        class3_btn = Button(btn_frame, text=self.class3, command=lambda: self.save(3))
        class3_btn.grid(row=0, column=2, sticky=W + E)

        bm_btn = Button(btn_frame, text="Brush-", command=self.brushminus)
        bm_btn.grid(row=1, column=0, sticky=W+ E)

        clear_btn = Button(btn_frame, text="Clear", command=self.clear)
        clear_btn.grid(row=1, column=1, sticky=W + E)

        bp_btn = Button(btn_frame, text="Brush+", command=self.brushplus)
        bp_btn.grid(row=1, column=2, sticky=W + E)

        train_button = Button(btn_frame, text="Train", command=self.train)
        train_button.grid(row=2, column=0, sticky=W + E)

        save_button = Button(btn_frame, text="Save Model", command=self.save_model)
        save_button.grid(row=2, column=1, sticky=W + E)

        load_button = Button(btn_frame, text="Load Model", command=self.load_model)
        load_button.grid(row=2, column=2, sticky=W + E)

        change_button = Button(btn_frame, text="Change Model", command=self.rotate_model)
        change_button.grid(row=3, column=0, sticky=W + E)

        predict_button = Button(btn_frame, text="Predict", command=self.predict)
        predict_button.grid(row=3, column=1, sticky=W + E)

        save_everything_button = Button(btn_frame, text="Save Everything", command=self.save_everything)
        save_everything_button.grid(row=3, column=2, sticky=W + E)

        self.status_label = Label(btn_frame, text=f"Current Model: {type(self.clf).__name__}")
        self.status_label.config(font=("Arial", 10))
        self.status_label.grid(row=4, column=1, sticky=W + E)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.attributes("-topmost", True)
        self.root.mainloop()

    def paint(self, event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        self.canvas.create_rectangle(x1, y1, x2, y2, fill="black", width=self.brush_weight)
        self.draw.rectangle([x1, y2, x2 + self.brush_weight, y2 + self.brush_weight], fill="black", width=self.brush_weight)

    def save(self, class_num):
        self.image1.save("temp.png")
        img = PIL.Image.open("temp.png")
        img.thumbnail((50, 50), PIL.Image.ANTIALIAS)

        if class_num == 1:
            img.save(f"{self.proj_name}/{self.class1}/{self.class1_counter}.png", "PNG")
            self.class1_counter += 1
        elif class_num == 2:
            img.save(f"{self.proj_name}/{self.class2}/{self.class2_counter}.png", "PNG")
            self.class2_counter += 1
        elif class_num == 3:
            img.save(f"{self.proj_name}/{self.class3}/{self.class3_counter}.png", "PNG")
            self.class3_counter += 1

        self.clear()

    def brushminus(self):
        if self.brush_weight > 1:
            self.brush_weight -= 1

    def brushplus(self):
        pass

    def clear(self):
        self.canvas.delete("all")
        self.draw.rectangle([0, 0, 1000, 1000], fill="white")

    def train(self):
        img_list = np.array([])
        class_list = np.array([])

        for x in range(1, self.class1_counter):
            img = cv.imread(f"{self.proj_name}/{self.class1}/{x}.png")[:, :, 0]
            img = img.reshape(2500)
            img_list = np.append(img_list, [img])
            class_list = np.append(class_list, 1)

        for x in range(1, self.class2_counter):
            img = cv.imread(f"{self.proj_name}/{self.class2}/{x}.png")[:, :, 0]
            img = img.reshape(2500)
            img_list = np.append(img_list, [img])
            class_list = np.append(class_list, 2)

        for x in range(1, self.class3_counter):
            img = cv.imread(f"{self.proj_name}/{self.class3}/{x}.png")[:, :, 0]
            img = img.reshape(2500)
            img_list = np.append(img_list, [img])
            class_list = np.append(class_list, 3)

        img_list = img_list.reshape(self.class1_counter - 1 + self.class2_counter - 1 + self.class3_counter - 1, 2500)

        self.clf.fit(img_list, class_list)
        tkinter.messagebox.showinfo("NeuralNine Drawing Classifier", "Model successfully trained!", parent=self.root)

    def predict(self):
        self.image1.save("temp.png")
        img = PIL.Image.open("temp.png")
        img.thumbnail((50, 50), PIL.Image.ANTIALIAS)
        img.save("predictshape.png", "PNG")

        img = cv.imread("predictshape.png")[:, :, 0]
        img = img.reshape(2500)
        prediction = self.clf.predict([img])
        if prediction[0] == 1:
            tkinter.messagebox.showinfo("NixAI Drawing Classifier", f"The Drawing is Probably a {self.class1}", parent = self.root)
        elif prediction[0] == 2:
            tkinter.messagebox.showinfo("NixAI Drawing Classifier", f"The Drawing is Probably a {self.class2}", parent = self.root)
        elif prediction[0] == 3:
            tkinter.messagebox.showinfo("NixAI Drawing Classifier", f"The Drawing is Probably a {self.class3}", parent = self.root)

    def rotate_model(self):
        if isinstance(self.clf, LinearSVC):
            self.clf = KNeighborsClassifier()
        elif isinstance(self.clf, KNeighborsClassifier):
            self.clf = LogisticRegression()
        elif isinstance(self.clf, LogisticRegression):
            self.clf = DecisionTreeClassifier()
        elif isinstance(self.clf, DecisionTreeClassifier):
            self.clf = RandomForestClassifier()
        elif isinstance(self.clf, RandomForestClassifier):
            self.clf = GaussianNB()
        elif isinstance(self.clf, GaussianNB):
            self.clf = LinearSVC()

        self.status_label.config(text=f"Current Model: {type(self.clf).__name__}")
    def save_model(self):
        file_path = filedialog.asksaveasfilename(defaultextension="pickle")
        with open(file_path, "wb") as f:
            pickle.dumb(self.clf, f)
        tkinter.messagebox.showinfo("NixAI Drawing Classifier", "Model SuccesfulLy Saved", parent = self.root)

    def load_model(self):
        file_path = filedialog.askopenfilename()
        with open(file_path, "rb") as f:
            self.clf = pickle.load(f)
        tkinter.messagebox.showinfo("NixAI Drawing Classifier", "Model SuccesfulLy Saved", parent = self.root)

    def save_everything(self):
        data = {"c1": self.class1,
                "c2": self.class2,
                "c3": self.class3,
                "c1c": self.class1_counter,
                "c2c": self.class2_counter,
                "c3c": self.class3_counter,
                "clf": self.clf,
                "pname": self.proj_name,
                }
        with open(f"{self.proj_name}/{self.proj_name}_data.pickle", "wb") as f:
            pickle.dumb(data, f)
        tkinter.messagebox.showinfo("NixAI Drawing Classifier", "Project SuccesfulLy Saved", parent=self.root)


    def on_closing(self):
        answer = tkinter.messagebox.askyesnocancel("QUIT?", "Do You Want To Save Your Work?", parent=self.root)
        if answer is not None:
            if answer:
                self.save_everything()
            self.root.destroy()
            exit()

DrawingClassifier()