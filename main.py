from tkinter import *
from PIL import Image, ImageTk

# Initialize window
window = Tk()
window.title("Goodness Restaurant")
window.minsize(width=500, height=700)
window.configure(bg="tomato")


def button_clicked():
    # Correct multipliers based on displayed prices
    amala_total = int(amala_sb.get()) * 1
    beans_total = int(beans_sb.get()) * 0.5
    boli_total = int(boli_sb.get()) * 2
    jollof_total = int(jollof_sb.get()) * 1
    ofada_total = int(ofada_sb.get()) * 2
    py_total = int(py_sb.get()) * 1
    total_bill = amala_total + beans_total + boli_total + jollof_total + ofada_total + py_total
    bill = Label(window, text=f"Your Total bill is ${total_bill:.2f}", font=("Poppins", 18, "bold"), bg="tomato")
    bill.grid(column=0, row=12, columnspan=3, pady=10)


# Function to load and resize images
def load_image(path, size):
    img = Image.open(path)
    img = img.resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(img)


# Restaurant name and quote
resto_name = Label(window, text="WELCOME TO\nGOODNESS RESTAURANT", font=("Poppins", 20, "bold"), bg="tomato")
resto_name.grid(column=0, row=0, columnspan=3, pady=10)

quote = Label(window, text="We Serve What You Deserve", font=("Poppins", 18, "italic"), bg="tomato")
quote.grid(column=0, row=1, columnspan=3, pady=10)

# Food selection
food_label = Label(window, text="Choose Your Food", font=("Poppins", 12, "normal"), bg="tomato")
food_label.grid(column=0, row=2, columnspan=3, pady=10)

# Image sizes
image_size = (150, 120)

# Amala
amala = load_image("amala.gif", image_size)
amala_label = Label(window, image=amala, borderwidth=0)
amala_label.grid(column=0, row=3)
amala_info = Label(window, text="Amala and Ewedu\n$1", font=("Poppins", 10, "normal"), bg="tomato")
amala_info.grid(column=0, row=4)
amala_sb = Spinbox(window, from_=0, to=10, width=5)
amala_sb.grid(column=0, row=5)

# Beans
beans = load_image("beans.gif", image_size)
beans_label = Label(window, image=beans, borderwidth=0)
beans_label.grid(column=1, row=3)
beans_info = Label(window, text="Ewa Egonyi and Bread\n$0.5", font=("Poppins", 10, "normal"), bg="tomato")
beans_info.grid(column=1, row=4)
beans_sb = Spinbox(window, from_=0, to=10, width=5)
beans_sb.grid(column=1, row=5)

# Boli
boli = load_image("boli.gif", image_size)
boli_label = Label(window, image=boli, borderwidth=0)
boli_label.grid(column=2, row=3)
boli_info = Label(window, text="Boli and Groundnut\n$2", font=("Poppins", 10, "normal"), bg="tomato")
boli_info.grid(column=2, row=4)
boli_sb = Spinbox(window, from_=0, to=10, width=5)
boli_sb.grid(column=2, row=5)

# More food label
more_food_label = Label(window, text="Choose Your Food", font=("Poppins", 12, "normal"), bg="tomato")
more_food_label.grid(column=0, row=6, columnspan=3, pady=10)

# Jollof
jollof = load_image("jollof.gif", image_size)
jollof_label = Label(window, image=jollof, borderwidth=0)
jollof_label.grid(column=0, row=7)
jollof_info = Label(window, text="Jollof rice, Plantain and Chicken\n$1", font=("Poppins", 10, "normal"), bg="tomato")
jollof_info.grid(column=0, row=8)
jollof_sb = Spinbox(window, from_=0, to=10, width=5)
jollof_sb.grid(column=0, row=9)

# Ofada
ofada = load_image("ofada.gif", image_size)
ofada_label = Label(window, image=ofada, borderwidth=0)
ofada_label.grid(column=1, row=7)
ofada_info = Label(window, text="Ofada rice\n$2", font=("Poppins", 10, "normal"), bg="tomato")
ofada_info.grid(column=1, row=8)
ofada_sb = Spinbox(window, from_=0, to=10, width=5)
ofada_sb.grid(column=1, row=9)

# Pounded Yam
py = load_image("pounded-yam.gif", image_size)
py_label = Label(window, image=py, borderwidth=0)
py_label.grid(column=2, row=7)
py_info = Label(window, text="Pounded yam and Egusi soup\n$1", font=("Poppins", 10, "normal"), bg="tomato")
py_info.grid(column=2, row=8)
py_sb = Spinbox(window, from_=0, to=10, width=5)
py_sb.grid(column=2, row=9)

# Order button
finish = Button(window, text="Order", command=button_clicked)
finish.grid(column=1, row=10, pady=20)

window.mainloop()
