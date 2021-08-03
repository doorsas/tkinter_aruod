import tkinter as tk


def decrease():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value - 2}"

def increase():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value + 2}"

def iincrease():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value + 10}"

window = tk.Tk()





window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

btn_idecrease = tk.Button(master=window, text="+10", command=iincrease)
btn_idecrease.grid(row=1, column=1, sticky="nsew")


btn_decrease = tk.Button(master=window, text="-", command=decrease)
btn_decrease.grid(row=0, column=0, sticky="nsew")

lbl_value = tk.Label(master=window, text="0")
lbl_value.grid(row=0, column=1)

btn_increase = tk.Button(master=window, text="+", command=increase)
btn_increase.grid(row=0, column=2, sticky="nsew")

window.mainloop()