from tkinter import*
root = Tk()
root.geometry("700x400")

def getvals():
    print("Accepted")

root.title("REGISTRATION FORM")

Label(root, text="Python Registration Form", font="arial 15 bold").grid(row=0, column=3)

#Field name
name =Label(root, text="Name", font="arial 14 italic")
phone =Label(root, text="Phone", font="arial 14 italic")
gender =Label(root, text="Gender", font="arial 14 italic")
rollno =Label(root, text="Rollno", font="arial 14 italic")
subject =Label(root, text="Subject",font="arial 14 italic")

#Packing field
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
rollno.grid(row=4, column=2)
subject.grid(row=5, column=2)

#variable for storing data
namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
rollnovalue = StringVar
subjectvalue = StringVar
checkvalue = IntVar

#creating entry field
nameentry = Entry(root, textvariable =namevalue)
phoneentry = Entry(root, textvariable =phonevalue)
genderentry = Entry(root, textvariable =gendervalue)
rollnoentry = Entry(root, textvariable =rollnovalue)
subjectentry = Entry(root, textvariable =subjectvalue)

#packing entry field
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
rollnoentry.grid(row=4, column=3)
subjectentry.grid(row=5, column=3)

# creating checkbox
checkbtn = Checkbutton(text="remember me?", variable = checkvalue)
checkbtn.grid(row=6,column=3)

# submit button
Button(text="submit", command=getvals).grid(row=7,column=3)




root.mainloop()