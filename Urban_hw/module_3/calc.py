import tkinter as tk


def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2


def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)  # 0-индекс, куда вставить; res-что вставить


def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)


def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)


def multiple():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)

def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)


window = tk.Tk()
window.title('calculator') # nazvanie okna
window.geometry("350x350") # razmer okna
window.resizable(False, False) #izmenenie razmera okna
button_add = tk.Button(window, text="+", width=2, height=2, command=add) # dobavili knopky +
button_add.place(x=100, y=200) # raspolozhenie knopki
button_add = tk.Button(window, text="-", width=2, height=2, command=sub) # dobavili knopky -
button_add.place(x=150, y=200) # raspolozhenie knopki
button_add = tk.Button(window, text="x", width=2, height=2, command=multiple) # dobavili knopky ymnozhit'
button_add.place(x=200, y=200) # raspolozhenie knopki
button_add = tk.Button(window, text="/", width=2, height=2, command=div) # dobavili knopky deleniya
button_add.place(x=250, y=200) # raspolozhenie knopki
number1_entry = tk.Entry(window, width=28)
number1_entry.place(x=100, y=75)
number1 = tk.Label(window, text="Vvedite pervoe chislo")
number1.place(x=100, y=50)
number2_entry = tk.Entry(window, width=28)
number2_entry.place(x=100, y=150)
number2 = tk.Label(window, text="Vvedite vtoroe chislo")
number2.place(x=100, y=125)
answer_entry = tk.Entry(window, width=28)
answer_entry.place(x=100, y=300)
answer = tk.Label(window, text="Otvet")
answer.place(x=100, y=275)
window.mainloop()