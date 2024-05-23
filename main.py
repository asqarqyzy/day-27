from tkinter import *
window = Tk()
window.title("Mile to kilometer converter")
window.minsize(width=200, height=100)
window.config(padx=10,pady=10)

mile_input = Entry(width=10)
mile_input.grid(column=1, row=0)


miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

def calc_ml_km():
    result_label = Label(text=str(int(mile_input.get())*1.5))
    result_label.grid(column=1, row=1)

calc_button = Button(text="Calculate", command=calc_ml_km)
calc_button.grid(column=1, row=2)



window.mainloop()