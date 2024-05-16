from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from sys import exit
import os
import sys

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


weight_units_to_kg = {"mg": "0.000001",
                      "g": "0.001",
                      "dkg": "0.01",
                      "kg": "1",
                      "t (metric ton)": "1000",
                      "pound (lbs)": "0.45359237",
                      "short ton (tn)": "907.18474",
                      "ounce(uncia)": "0.02834952"}
weight_units = {'mg': 1000000,
                'g': 1000,
                'dkg': 100,
                'kg': 1,
                't (metric ton)': 0.001,
                'pound (lbs)': 2.2046226,
                'short ton (tn)': 0.001102,
                'ounce(uncia)': 35.2739907}

length_units = {"mm": [0.001, 1000],
                "cm": [0.01, 100],
                "dm": [0.1, 10],
                "m": [1, 1],
                "km": [1000, 0.001],
                "Inch (in)": [0.0254, (1 / 0.0254)],
                "Foot (ft)": [0.3048, (1 / 0.3048)],
                "Yard (yd)": [0.9144, (1 / 0.9144)],
                "Mile (mi)": [1609.344, (1 / 1609.344)]}

volume_units = {"mm\u00b3": [0.000000001, 1000000000],
                "cm\u00b3": [0.000001, 1000000],
                "dm\u00b3": [0.001, 1000],
                "m\u00b3": [1, 1],
                "in\u00b3": [0.0000163871, (1 / 0.0000163871)],
                "ft\u00b3": [0.0283168466, (1 / 0.0283168466)],
                "yd\u00b3": [0.764554858, (1 / 0.764554858)],
                "mi\u00b3": [4168180000, (1 / 4168180000)],
                "l": [0.001, (1 / 0.001)]}


def l_calculate():
    global weight_units, weight_units_to_kg
    from_ = l_from.get()
    to = l_to.get()
    value = entry.get()
    try:
        value = float(value)

        l_eredmeny.set('')
        if (to != 'Select' and from_ != 'Select'):
            value_in_kg = round(value * float(weight_units_to_kg.get(from_)), 6)
            result = round(value_in_kg * float(weight_units.get(to)), 6)
            l_eredmeny.set("{} {}".format(str(result), to))
        else:
            l_eredmeny.set("Error")
    except ValueError:
        l_eredmeny.set("Error")

def temp():
    for i in range(2):
        t_calculate()
def t_calculate():
    from_ = t_from.get()
    to = t_to.get()
    value = temp_entry.get()
    try:
        value = float(value)
        t_eredmeny.set('')
    except:
        t_eredmeny.set("Error")

    if from_ == '℃':
        t_to.set('℉')
    elif from_ == '℉':
        t_to.set('℃')

    if from_ == '℃':

        t_to.set('℉')
        if value == '':
            t_eredmeny.set('Error')
        else:
            result = round(((9 / 5) * value) + 32, 3)
            t_eredmeny.set("{} {}".format(str(result), to))
    elif from_ == '℉':
        t_to.set('℃')
        if value == '':
            t_eredmeny.set('Error')
        else:
            result = round((value - 32) * (5 / 9), 3)
            t_eredmeny.set("{} {}".format(str(result), to))
    elif (from_ == 'Select' and to == 'Select'):
        t_eredmeny.set("Error")


def w_calculate():
    from_ = w_from.get()
    to = w_to.get()
    value = w_entry.get()
    try:
        value = float(value)
        w_eredmeny.set('')
        if (to != 'Select' and from_ != 'Select'):
            value_in_m = round(value * float(length_units.get(from_)[0]), 6)
            result = round(value_in_m * float(length_units.get(to)[1]), 6)
            w_eredmeny.set("{} {}".format(str(result), to))
        else:
            w_eredmeny.set("Error")
    except ValueError:
        w_eredmeny.set("Error")


def v_calculate():
    from_ = v_from.get()
    to = v_to.get()
    value = v_entry.get()
    try:
        value = float(value)
        v_eredmeny.set('')
        if (to != 'Select' and from_ != 'Select'):
            value_in_m = round(value * float(volume_units.get(from_)[0]), 10)
            result = round(value_in_m * float(volume_units.get(to)[1]), 10)
            v_eredmeny.set("{} {}".format(str(result), to))
        else:
            v_eredmeny.set('Error')
    except ValueError:
        v_eredmeny.set('Error')

def info():
    messagebox.showinfo('Info','This is a Unit converter program.\n      Version 1.0')

def reset():
    temp_entry.delete(0,END)
    entry.delete(0,END)
    entry.delete(0, END)
    w_entry.delete(0, END)
    v_entry.delete(0, END)

    l_eredmeny.set('')
    w_eredmeny.set('')
    v_eredmeny.set('')
    t_eredmeny.set('')

    l_from.set('Select')
    l_to.set('Select')
    w_from.set('Select')
    w_to.set('Select')
    v_from.set('Select')
    v_to.set('Select')
    t_from.set('Select')
    t_to.set('Select')

def help_():
    messagebox.showerror('Help', "          Help:\n https://github.com/Tekkermester/Unit_converter")
def quit_():
    window.destroy()
#------------------------------------------------
window = Tk()
window.title("Unit converter")
window.geometry("540x400")

icon = PhotoImage(file=resource_path("appicon.png"))
window.iconphoto(True, icon)

#tabs ----------------------------------
notebook = ttk.Notebook(window)
length_tab = Frame(notebook)
temperature_tab = Frame(notebook)
volume_tab = Frame(notebook)
weight_tab = Frame(notebook)
notebook.add(length_tab, text="Weight")
notebook.add(weight_tab, text="Length")
notebook.add(temperature_tab, text="Temperature")
notebook.add(volume_tab, text="Volume")
notebook.pack(expand=True, fill='both')

#menu -------------------------------------
menubar = Menu(window)
window.config(menu= menubar)
editMenu = Menu(menubar, tearoff=0)
aboutMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='About', menu=aboutMenu)
menubar.add_cascade(label='Edit', menu=editMenu)
aboutMenu.add_command(label="Info", command=info)
aboutMenu.add_command(label='Help', command=help_)
editMenu.add_command(label='Reset', command=reset)
editMenu.add_separator()
editMenu.add_command(label='Exit', command=quit_)


#distance tab----------------------------
length_label = Label(length_tab, text="Weight", font=("Arial", 30, "bold"), pady=20).grid(row=0, column=1, columnspan=3)
length_label_from = Label(length_tab, text="From: ", font=("Arial", 18, "bold")).grid(row=1, column=0)
entry = Entry(length_tab, font="arial")
entry.grid(row=1, column=2)

l_from = StringVar()
l_from.set("Select")
l_values = ["mg", "g", "dkg", "kg", "t (metric ton)", "pound (lbs)", "short ton (tn)", "ounce(uncia)"]

length_from = OptionMenu(length_tab, l_from, *l_values).grid(row=1, column=3)

length_label_to = Label(length_tab, text="To: ", font=("Arial", 18, "bold")).grid(row=2, column=0)

l_to = StringVar(window)
l_to.set("Select")
length_to = OptionMenu(length_tab, l_to, *l_values).grid(row=2, column=2)

length_label_result = Label(length_tab, text="Result: ", font=("Arial", 18, "bold", "italic"), width=10).grid(row=4,
                                                                                                              column=0)
l_eredmeny = StringVar()
l_eredmeny.set("")
length_result = Label(length_tab, textvariable=l_eredmeny, font=("Arial", 28, "bold"))
length_result.grid(row=4, column=2)
l_submit = Button(length_tab, text="Calculate", font=("Arial", 18, "italic"), pady=4, command=l_calculate).grid(row=3,
                                                                                                                column=2)

#temperature tap----------------------------------------
temp_label = Label(temperature_tab, text="Temperature", font=("Arial", 30, "bold"), pady=20).grid(row=0, column=1,
                                                                                                  columnspan=3)
temp_label_from = Label(temperature_tab, text="From: ", font=("Arial", 18, "bold")).grid(row=1, column=0)
temp_entry = Entry(temperature_tab, font="arial")
temp_entry.grid(row=1, column=2)

t_from = StringVar()
t_from.set("Select")
t_values = ["℃", "℉"]

temp_from = OptionMenu(temperature_tab, t_from, *t_values).grid(row=1, column=3)

temp_label_to = Label(temperature_tab, text="To: ", font=("Arial", 18, "bold")).grid(row=2, column=0)

t_to = StringVar(window)
t_to.set("Select")
temp_to = OptionMenu(temperature_tab, t_to, *t_values).grid(row=2, column=2)

temp_label_result = Label(temperature_tab, text="Result: ", font=("Arial", 18, "bold", "italic"), width=10).grid(row=4,
                                                                                                                 column=0)
t_eredmeny = StringVar()
t_eredmeny.set("")
temp_result = Label(temperature_tab, textvariable=t_eredmeny, font=("Arial", 28, "bold"))
temp_result.grid(row=4, column=2)
t_submit = Button(temperature_tab, text="Calculate", font=("Arial", 18, "italic"), pady=4, command=temp).grid(
    row=3, column=2)

#weight tab ------------------------------------------------------
Label(weight_tab, text="Length", font=("Arial", 30, "bold"), pady=20).grid(row=0, column=1, columnspan=3)
Label(weight_tab, text="From: ", font=("Arial", 18, "bold")).grid(row=1, column=0)
w_entry = Entry(weight_tab, font="arial")
w_entry.grid(row=1, column=2)

w_from = StringVar()
w_from.set("Select")
w_values = ["mm", "cm", "dm", "m", "km", "Inch (in)", "Foot (ft)", "Yard (yd)", "Mile (mi)"]

weight_from = OptionMenu(weight_tab, w_from, *w_values).grid(row=1, column=3)

w_to = StringVar(window)
w_to.set("Select")
weight_to = OptionMenu(weight_tab, w_to, *w_values).grid(row=2, column=2)

Label(weight_tab, text="Result: ", font=("Arial", 18, "bold", "italic"), width=10).grid(row=4, column=0)
w_eredmeny = StringVar()
w_eredmeny.set("")
weight_result = Label(weight_tab, textvariable=w_eredmeny, font=("Arial", 28, "bold"))
weight_result.grid(row=4, column=2)
w_submit = Button(weight_tab, text="Calculate", font=("Arial", 18, "italic"), pady=4, command=w_calculate).grid(row=3,
                                                                                                                column=2)

Label(weight_tab, text="To: ", font=("Arial", 18, "bold")).grid(row=2, column=0)

#volume tab ---------------------------------------------
Label(volume_tab, text="Volume", font=("Arial", 30, "bold"), pady=20).grid(row=0, column=1, columnspan=3)
Label(volume_tab, text="From: ", font=("Arial", 18, "bold")).grid(row=1, column=0)
v_entry = Entry(volume_tab, font="arial")
v_entry.grid(row=1, column=2)

v_from = StringVar()
v_from.set("Select")
v_values = ["mm\u00b3", "cm\u00b3", "dm\u00b3", "m\u00b3", "l", "in\u00b3", "ft\u00b3", "yd\u00b3", "mi\u00b3"]

volume_from = OptionMenu(volume_tab, v_from, *v_values).grid(row=1, column=3)

v_to = StringVar(window)
v_to.set("Select")
volume_to = OptionMenu(volume_tab, v_to, *v_values).grid(row=2, column=2)

Label(volume_tab, text="Result: ", font=("Arial", 18, "bold", "italic"), width=10).grid(row=4, column=0)
v_eredmeny = StringVar()
v_eredmeny.set("")
volume_result = Label(volume_tab, textvariable=v_eredmeny, font=("Arial", 28, "bold"))
volume_result.grid(row=4, column=2)
v_submit = Button(volume_tab, text="Calculate", font=("Arial", 18, "italic"), pady=4, command=v_calculate).grid(row=3,
                                                                                                                column=2)

Label(volume_tab, text="To: ", font=("Arial", 18, "bold")).grid(row=2, column=0)

window.mainloop()
