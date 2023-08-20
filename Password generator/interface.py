from tkinter import messagebox
import pickle
from tkinter import *
from logic import generate

def on_click(alpha, special, upper, complexity, max_len):
    password = generate(alpha, special, upper, complexity, max_len)
    label_password.config(text=password)

root = Tk()
root.title("Password Generator")
entry_len = Entry(root, width=50)
entry_len.pack()
special = IntVar()  
upper = IntVar()  
complexity = IntVar()
digits = IntVar()

Button1 = Checkbutton(root, text = "Include special characters", 
                      variable = special,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 20)
  
Button2 = Checkbutton(root, text = "Include uppercase letters",
                      variable = upper,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 20)
  
Button3 = Checkbutton(root, text = "High complexity password",
                      variable = complexity,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 20)  
    
Button4 = Checkbutton(root, text = "Digits only",
                      variable = digits,
                      onvalue = 0,
                      offvalue = 1,
                      height = 2,
                      width = 20)  

Button1.pack()  
Button2.pack()  
Button3.pack()
Button4.pack()

label_password = Label(root, text="")
label_password.pack()

print(special)
button_generate = Button(root, text="Generate password", 
                         width=48, command=lambda : on_click(alpha=digits.get(), special=special.get(), upper=upper.get(), complexity=complexity.get(), max_len=int(entry_len.get())))

button_generate.pack()
root.mainloop()