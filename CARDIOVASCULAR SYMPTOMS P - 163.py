from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Fever Reoprt")
root.geometry("400x400")


Question1_radiobutton = StringVar(value = "0")

Question1 = Label(root, text = "Do you experience shortness of breath during routine activities ?")
Question1.pack()
Question1_Rb1 = Radiobutton(root, text = "yes", variable = Question1_radiobutton, value = "yes")
Question1_Rb1.pack()
Question1_Rb2 = Radiobutton(root, text = "no", variable = Question1_radiobutton, value = "no")
Question1_Rb2.pack()

Question2_radiobutton = StringVar(value = "0")

Question2 = Label(root, text = "Do you have swelling in the feet/ankle/legs(shoe feel tighter) or abdomen")
Question2.pack()
Question2_Rb1 = Radiobutton(root, text = "yes", variable = Question2_radiobutton, value = "yes")
Question2_Rb1.pack()
Question2_Rb2 = Radiobutton(root, text = "no", variable = Question2_radiobutton, value = "no")
Question2_Rb2.pack()

Question3_radiobutton = StringVar(value = "0")

Question3 = Label(root, text = "Do you feel these symptoms - confusion, disorientation or loss of memory ?")
Question3.pack()
Question3_Rb1 = Radiobutton(root, text = "yes", variable = Question3_radiobutton, value = "yes")
Question3_Rb1.pack()
Question3_Rb2 = Radiobutton(root, text = "no", variable = Question3_radiobutton, value = "no")
Question3_Rb2.pack()

Question4_radiobutton = StringVar(value = "0")

Question4 = Label(root, text = "Do you experience shortness of breath while at rest/lying down ?")
Question4.pack()
Question4_Rb1 = Radiobutton(root, text = "yes", variable = Question4_radiobutton, value = "yes")
Question4_Rb1.pack()
Question4_Rb2 = Radiobutton(root, text = "no", variable = Question4_radiobutton, value = "no")
Question4_Rb2.pack()

Question5_radiobutton = StringVar(value = "0")

Question5 = Label(root, text = "Do you experience persistent wheezing/coughing that produces white or pink blood tinged mucus ?")
Question5.pack()
Question5_Rb1 = Radiobutton(root, text = "yes", variable = Question5_radiobutton, value = "yes")
Question5_Rb1.pack()
Question5_Rb2 = Radiobutton(root, text = "no", variable = Question5_radiobutton, value = "no")
Question5_Rb2.pack()

def fever_score():
    score = 0
    if Question1_radiobutton.get() == "yes":
        score += 10
        print(score)
    if Question2_radiobutton.get() == "yes":
        score += 10
        print(score)
    if Question3_radiobutton.get() == "yes":
        score += 10
        print(score)
    if Question4_radiobutton.get() == "yes":
        score += 10
        print(score)
    if Question5_radiobutton.get() == "yes":
        score += 10
        print(score)    
        
    if score <= 10:
        messagebox.showinfo("Report", "You don't need to visit to a doctor")
    elif score > 10 and score <= 30:
        messagebox.showinfo("Report", "You might perhaps have to visit a doctor")
    else :
        messagebox.showinfo("Report", "I strongly advised you to vist a doctor")

button = Button(root, text = "Show report", command = fever_score)
button.pack()

root.mainloop()        
        