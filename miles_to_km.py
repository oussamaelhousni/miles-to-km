import tkinter as tk
from ttkbootstrap import ttk

# window
window = tk.Tk()
window.title("miles to km")
window.geometry("300x150")


def convert():
    mile = entry_int.get()
    output_var.set(mile * 1.61)


# widgets
# 1 - label
label = ttk.Label(master=window, text="Miles to Kilometers", font="Calibri 24 bold")
label.pack()

# 2 - frame
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
input_field = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame, text="Convert", command=convert)
input_field.pack(side="left", padx=4)
button.pack(side="left")
input_frame.pack(pady=10)

# output
output_var = tk.StringVar()
output_label = ttk.Label(
    master=window, text="Output", font="Calibri 24", textvariable=output_var
)
output_label.pack()

# run
window.mainloop()
