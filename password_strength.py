import ttkbootstrap as tkb

root = tkb.Window(themename="darkly") #you can get themename from ttkbootstrap website
root.title("TKB APP")
root.geometry("600x400")

def submit():
    cc = len(entry.get())

    if cc <= 4:
        pp = tkb.Progressbar(root, bootstyle="danger", maximum=100, length=300, value=25)
        pp.grid(column=1, row=2, pady=10)

        label_2.config(bootstyle="danger", text="Weak", font=("verdana", 12))

    elif 4 < cc < 8:
        pp = tkb.Progressbar(root, bootstyle="warning", maximum=100, length=300, value=50)
        pp.grid(column=1, row=2, pady=10)

        label_2.config(bootstyle="warning", text="Slightly strong", font=("verdana", 12))
    else:
        pp = tkb.Progressbar(root, bootstyle="success", maximum=100, length=300, value=100)
        pp.grid(column=1, row=2, pady=10)

        label_2.config(bootstyle="success", text="Strong", font=("verdana", 12))

label_1 = tkb.Label(root, bootstyle="light", text="password:", font=("verdana", 12))
label_1.grid(column=0, row=0, pady=20, padx=40)

entry = tkb.Entry(root, font=("verdana", 12))
entry.grid(column=1, row=0, pady=20)

button = tkb.Button(root, bootstyle="info", text="submit", command=submit)
button.grid(column=1, row=1)

label_2 = tkb.Label(root, bootstyle="success", text="")
label_2.grid(column=1, row=3, pady=10)

root.mainloop()
