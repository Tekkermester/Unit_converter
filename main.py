from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from sys import exit


weight_units = {'mg': [0.000001,1000000],
                'g': [0.001, 1000],
                'dkg': [0.01,10],
                'kg': [1,1],
                't (metric ton)': [1000, 0.001],
                'pound (lbs)': [2.2046226, (1/2.2046226)],
                'short ton (tn)': [0.001102, (1/0.001102)],
                'ounce(uncia)': [35.2739907, (1/35.2739907)]}

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
temp_units = {"℃":[],
              "℉":[]}

def info():
    messagebox.showinfo('Info', 'This is a Unit converter program.\n      Version 1.1')

def reset():
    length_tab.reset()
    tempertaure_tab.reset()
    weight_tab.reset()
    volume_tab.reset()

def help():
    messagebox.showerror('Help', "          Help:\n https://github.com/Tekkermester/Unit_converter")


#------------------------------------------------
window = Tk()
window.title("Unit converter")
window.geometry("600x400")

icon = PhotoImage(file="appicon.png")
window.iconphoto(True, icon)

#menu -------------------------------------
menubar = Menu(window)
window.config(menu=menubar)
editMenu = Menu(menubar, tearoff=0)
aboutMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='About', menu=aboutMenu)
menubar.add_cascade(label='Edit', menu=editMenu)
aboutMenu.add_command(label="Info", command=info)
aboutMenu.add_command(label='Help', command=help)
editMenu.add_command(label='Reset', command=reset)
editMenu.add_separator()
editMenu.add_command(label='Exit', command=quit)

notebook = ttk.Notebook(window)
notebook.pack(expand=True, fill='both')


class Tabs:
    global notebook
    def __init__(self, name: str, units,calc_mode: str):
        self.name = name
        self.units = units
        self.calc_mode = calc_mode
        self.current_tab = Frame(notebook)
        self.current_entry = None
        self.current_from = StringVar()
        self.current_to = StringVar()
        self.result = StringVar()
    def calculate(self):
        if self.calc_mode == 'normal':
            value = self.current_entry.get()
            try:
                value = float(value)
                self.result.set("")
                if (self.current_to != "Select" and self.current_from != "Select"):
                    value_back = round(value * float(self.units.get(self.current_from.get())[0]),6)
                    final_result = round(value_back * float(self.units.get(self.current_to.get())[1]),6)
                    self.result.set("{} {}".format(str(final_result), self.current_to.get()))
                else:
                    self.result.set("Error")
            except ValueError:
                self.result.set("Error")
        elif self.calc_mode == 'temperature':
            value = self.current_entry.get()
            try:
                value = float(value)
                self.result.set('')
            except:
                self.result.set("Error")

            if self.current_from.get() == '℃':
                self.current_to.set('℉')
                if value == '':
                    self.result.set('Error')
                else:
                    result = round(((9 / 5) * value) + 32, 3)
                    self.result.set("{} {}".format(str(result), self.current_to.get()))
            elif self.current_from.get() == '℉':
                self.current_to.set('℃')
                if value == '':
                    self.result.set('Error')
                else:
                    result = round((value - 32) * (5 / 9), 3)
                    self.result.set("{} {}".format(str(result), self.current_to.get()))
            elif (self.current_from.get() == 'Select' and self.current_to.get() == 'Select'):
                self.result.set("Error")

    def reset(self):
        self.current_entry.delete(0,END)
        self.current_from.set("Select")
        self.current_to.set("Select")
        self.result.set('')

    def create_frame(self):
        notebook.add(self.current_tab, text=self.name)
        Label(self.current_tab, text=self.name, font=("Arial", 30, "bold"), pady=20, padx=60).grid(row=0, column=1, columnspan=3)
        Label(self.current_tab, text="From: ", font=("Arial", 18, "bold")).grid(row=1, column=0)
        self.current_entry = Entry(self.current_tab, font="arial")
        self.current_entry.grid(row=1, column=2)
        self.current_from.set("Select")
        OptionMenu(self.current_tab,self.current_from,*self.units.keys()).grid(row=1, column=3)
        Label(self.current_tab, text="To: ", font=("Arial", 18, "bold")).grid(row=2, column=0)
        self.current_to.set("Select")
        OptionMenu(self.current_tab, self.current_to, *self.units.keys()).grid(row=2, column=2)
        Label(self.current_tab, text="Result: ", font=("Arial", 18, "bold", "italic"), width=10).grid(row=4,column=0)
        self.result.set("")
        print_result = Label(self.current_tab, textvariable=self.result, font=("Arial", 28, "bold"))
        print_result.grid(row=4, column=2)
        Button(self.current_tab, text="Calculate", font=("Arial", 18, "italic"), pady=4, command=self.calculate).grid(row=3,column=2)


def main():
    tempertaure_tab = Tabs("Temperature", temp_units, "temperature")
    tempertaure_tab.create_frame()
    length_tab = Tabs("Length", length_units, "normal")
    length_tab.create_frame()
    weight_tab = Tabs("Weight", weight_units, "normal")
    weight_tab.create_frame()
    volume_tab = Tabs("Volume", volume_units, "normal")
    volume_tab.create_frame()

if __name__ == "__main__":
    main()
window.mainloop()
