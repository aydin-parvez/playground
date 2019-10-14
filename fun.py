import tkinter, datetime

def onClick(event):
    year_birth = int(textBox1.get())
    year_now = datetime.date.today().year
    age = year_now - year_birth
    textBox2.delete(0, len(textBox2.get()))
    textBox2.insert(0, age)

window = tkinter.Tk()

textBox1 = tkinter.Entry()
textBox1.pack(padx=10, pady=10)

button = tkinter.Button(window, text="Calculate age")
button.pack(padx=10, pady=10)
button.bind("<ButtonRelease-1>", onClick)

textBox2 = tkinter.Entry()
textBox2.pack(padx=10, pady=10)

window.mainloop()