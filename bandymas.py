import tkinter as tk
from tkinter.ttk import *
from aruodas_namai import parser
from getlinks import get_links
from testine import testine
from tkinter import messagebox
from tkinter.ttk import Progressbar


def clicked():

    btn.config(text='Vykdoma')


    if namaiarbutai_pasirinkimas.get() == 'Namai':

            if miestas_pasirinkimas.get() == 'Vilnius':
                print(miestas_pasirinkimas.get())
                print(suma_pasirinkimas.get())
                parser()
                btn.config(text='Siunčiama')
                messagebox.showinfo('Pranešimas', "Siuntimas baigtas")
                btn.config(text='Pasirink')

        
            elif miestas_pasirinkimas.get() == 'Kaunas':
                testine(namaiarbutai_pasirinkimas.get())
                testine(miestas_pasirinkimas.get())
                testine(suma_pasirinkimas.get())
                testine(txt.get())
                btn.config(text='Pasirink')
                pradinis_linkas = 'https://www.aruodas.lt/butai/vilniuje/?FPriceMax=1500000'
                get_links(pradinis_linkas)
                res = messagebox.askquestion( 'Suktas Klausimas', 'Nori baigti  ?')
                if res == 'yes':
                    window.quit()
                elif res == 'no':
                    messagebox.showinfo('Pasirink')
                else:
                    messagebox.showwarning('error', 'Something went wrong!')

            elif miestas_pasirinkimas.get() == 'Klaipėda':
                print (miestas_pasirinkimas.get())


            elif miestas_pasirinkimas.get() == 'Šiauliai':
                print (miestas_pasirinkimas.get())


            elif miestas_pasirinkimas.get() == 'Panevežys':
                print (miestas_pasirinkimas.get())
                print (suma_pasirinkimas.get())

    elif namaiarbutai_pasirinkimas.get() == 'Butai':
        print (namaiarbutai_pasirinkimas.get())







window = tk.Tk()
window.title("Aruodas")

class Uzrasas(tk.Label):
    def __init__(self, master, *args, **kwargs):
        super(Uzrasas, self).__init__(master, *args, **kwargs)



namai_butai_uzrasas = Label(window, text="Pasirink namai ar butai", font=("Arial Bold", 10))
namai_butai_uzrasas.grid(column=2, row=2,pady = 3)

namaiarbutai_pasirinkimas = Combobox(window, width=30)
namaiarbutai_pasirinkimas['values'] = ('----','Namai', 'Butai')
namaiarbutai_pasirinkimas.current(0)  # set the selected item
namaiarbutai_pasirinkimas.grid(column=4, row=2)


miestas_uzrasas = Uzrasas(window, text="Pasirink miestą", font=("Arial Bold", 10))
miestas_uzrasas.grid(column=2, row=3, sticky="n")

miestas_pasirinkimas = Combobox(window, width=30)
miestas_pasirinkimas['values'] = ('----','Vilnius', 'Kaunas', 'Klaipėda', 'Šiauliai', "Panevežys")
miestas_pasirinkimas.current(0)  # set the selected item
miestas_pasirinkimas.grid(column=4, row=3)


suma_pasirinkimas = Combobox(window, width=30
          )
suma_pasirinkimas['values'] = ('----','Nuo 0 iki 100000', 'Nuo 100000 iki 150000', "150000 ir daugiau ... ",
               )

suma_pasirinkimas.current(0)  # set the selected item
suma_pasirinkimas.grid(column=4, row=6,pady = 3)


kainos_uzrasas = Uzrasas(window, text="Pasirink kainų intervalą", font=("Arial Bold", 10))
kainos_uzrasas.grid(column=2, row=6)


failo_uzrasas = Uzrasas(window, text="Pasirink failo pavadinimą", font=("Arial Bold", 10))
failo_uzrasas.grid(column=2, row=7)

txt = Entry(window, width=33)
txt.focus()
# txt = Entry(window,width=10, state='disabled')
txt.grid(column=4, row=7)


# bar = Progressbar(window, length=200)
# bar.grid(column=7, row=7)

# chk_state = BooleanVar()
# chk_state.set(True) #set check state
# chk = Checkbutton(window, text='Choose', var=chk_state)
# chk.grid(column=0, row=0)

window.geometry('400x200')
btn = Button(window, text='Pasirink', width=33, command=clicked)

btn.grid(column=4, row=8, pady = 10 )

window.mainloop()
