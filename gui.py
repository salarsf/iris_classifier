from tkinter import *

from iris_classifier import IrisFlower

root = Tk()
root.title("Iris Flower Classifier")

title_label = Label(root, text="IRIS")
title_label.grid(row=0, column=0, columnspan=2)

sepal_len_label = Label(root, text="sepal length:")
sepal_len_label.grid(row=1, column=0)

sepal_wid_label = Label(root, text="sepal width:")
sepal_wid_label.grid(row=2, column=0)

petal_len_label = Label(root, text="petal length:")
petal_len_label.grid(row=3, column=0)

petal_wid_label = Label(root, text="petal width:")
petal_wid_label.grid(row=4, column=0)

sepal_len = StringVar()
sepal_len_entry = Entry(root, textvariable=sepal_len)
sepal_len_entry.grid(row=1,column=1)

sepal_wid = StringVar()
sepal_wid_entry = Entry(root, textvariable=sepal_wid)
sepal_wid_entry.grid(row=2,column=1)

petal_len = StringVar()
petal_len_entry = Entry(root, textvariable=petal_len)
petal_len_entry.grid(row=3,column=1)

petal_wid = StringVar()
petal_wid_entry = Entry(root, textvariable=petal_wid)
petal_wid_entry.grid(row=4,column=1)

def submit():
    sepal_len_float = float(sepal_len.get())
    sepal_wid_float = float(sepal_wid.get())
    petal_len_float = float(petal_len.get())
    petal_wid_float = float(petal_wid.get())

    new_flower = IrisFlower(sepal_len_float, sepal_wid_float, petal_len_float, petal_wid_float)
    print(new_flower.iris_type)

submit_button = Button(root, text="Submit", command=submit)
submit_button.grid(row=5, column=0, columnspan=2)

root.mainloop()
