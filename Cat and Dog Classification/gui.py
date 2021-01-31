# Importing tkinter Python GUI Libs
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

# Importing Keras Model 
# to load  our classification model
from keras.models import load_model

# import numpy lib
import numpy as np

model = load_model("classifier1_cat&dog_10epochs.h5")

#dictionary to label all traffic signs class.
classes = {
    0: "it's a cat",
    1: "it's a dog"
}

# Initialize GUI
top = tk.Tk()
top.geometry('800x600')
top.title('Cats and Dogs Classification')
top.configure(background='#CDCDCD')
label = Label(top, background='#CDCDCD', font=('arial', 15, 'bold'))
sign_image = Label(top)

def classify(file_path):
    """
    This function will classify 
    the image that user has inputted
    """
    global label_packed
    image = Image.open(file_path)
    image = image.resize((128, 128))
    image = np.expand_dims(image, axis=0)
    image = np.array(image)
    image = image/255
    pred = model.predict_classes([image])[0]
    sign = classes[pred]
    print(sign)
    label.configure(foreground='#011638', text=sign)

def show_classify_button(file_path):
    """
    This function is to create Button 
    that will show in the GUI
    """
    classify_btn = Button(top, text="Classify Image",
                        command=lambda: classify(file_path),
                        padx=10, pady=5)
    classify_btn.configure(background='#364156', foreground='white',
                         font=('arial', 10, 'bold'))
    classify_btn.place(relx=0.79, rely=0.46)

def upload_image():
    """
    This function will try to accept user input
    (Image Upload) with tkinter filedialog library
    """
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),
                            (top.winfo_height()/2.25)))
        im = ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image = im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass

upload = Button(top, text="Upload an image",
                command=upload_image, padx=10, pady=5)
upload.configure(background='#364156', foreground='white',
                 font=('arial', 10, 'bold'))
upload.pack(side=BOTTOM, pady=50)
sign_image.pack(side=BOTTOM, expand=True)
label.pack(side=BOTTOM, expand=True)
heading = Label(top, text="Cats and Dogs Classification",
                pady=20, font=('arial', 20, 'bold'))
heading.configure(background='#CDCDCD', foreground='#364156')
heading.pack()
top.mainloop()
