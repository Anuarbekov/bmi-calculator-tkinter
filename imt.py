import tkinter as tk
from turtle import width

clicks = 0
window = tk.Tk()


window.geometry("500x500")
window.title(string="BMI Caclculator")
welcome = tk.Label(text="This application requires your weight \n and height to find your Body Mass Index.\n First write your weight(in kilogramm),\n then height(in cm).",
                    font=("Courier", 12)
                    )
welcome.pack(pady=5)

ent_wei = tk.Entry(width=40, bg="white", fg="black")
ent_wei.pack(pady=10)

ent_hei = tk.Entry(width=40, bg="white", fg="black")
ent_hei.pack(pady=10)

def button_click():
    global clicks
    weight = int(ent_wei.get())
    height = int(ent_hei.get()) / 100
    bmiCalc = weight / (height**2)
    my_formatter = "{0:.1f}"
    bmiCalc = float(my_formatter.format(bmiCalc))
    if bmiCalc < 18.5:
        bmi = tk.Label(text=f"Your BMI is {bmiCalc}. You are underweighted.", font=("Times New Roman", 12))
    elif bmiCalc >= 18.5 and bmiCalc <= 24.9:
        bmi = tk.Label(text=f"Your BMI is {bmiCalc}. You are normal weighted.", font=("Times New Roman", 12))
    elif bmiCalc >= 25 and bmiCalc <= 29.9:
        bmi = tk.Label(text=f"Your BMI is {bmiCalc}. You are overweighted.", font=("Times New Roman", 12))
    else:
        bmi = tk.Label(text=f"Your BMI is {bmiCalc}. You have obesity.", font=("Times New Roman", 12)) 
    if clicks == 0:
        bmi.pack(pady=10)
        clicks += 1

btn_submit = tk.Button(text="View my BMI.", bg="Tomato", fg="white", width=20, height=2, bd=0, command=button_click, font=("Courier", 8)) 
btn_submit.pack(pady=20)
window.mainloop()

