from time import strftime
from tkinter import Label, Tk

#window config for clock

window = Tk()
window.title("clock")
window.geometry("400x160")
window.configure(background = "blue")
window.resizable(False,False)

#clock label

clock_label = Label(window, font = ("Times", 30, "bold"), bg = "blue", fg = "white" , relief="flat")
clock_label.place(x = 20, y = 20)

def updating_label():
    current_time = strftime("%H: %M: %S")
    clock_label.configure(text = current_time)
    clock_label.after(80, updating_label)

updating_label()
window.mainloop()