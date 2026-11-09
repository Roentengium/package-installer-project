#Main
import tkinter as tk

result = ""

def submit():
    global result
    result = entry.get()
    root.destroy()

root = tk.Tk()
root.title("Input")

tk.Label(root, text="Enter something:").pack(padx=10, pady=(10, 0))
entry = tk.Entry(root, width=40)
entry.pack(padx=10, pady=5)
entry.focus()
entry.bind("<Return>", lambda e: submit())

tk.Button(root, text="OK", command=submit).pack(pady=(0, 10))

root.mainloop()

print(result)
