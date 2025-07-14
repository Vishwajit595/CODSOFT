# import tkinter as tk

# def click(event):
#     text = event.widget.cget("text")
#     if text == "=":
#         try:
#             result = eval(str(entry.get()))
#             entry_var.set(result)
#         except Exception as e:
#             entry_var.set("Error")
#     elif text == "C":
#         entry_var.set("")
#     else:
#         entry_var.set(entry_var.get() + text)


# root = tk.Tk()
# root.geometry("300x400")
# root.title("Calculator")

# entry_var = tk.StringVar()
# entry = tk.Entry(root, textvar=entry_var, font="Arial 20", justify='right')
# entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)


# button_frame = tk.Frame(root)
# button_frame.pack()

# buttons = [
#     ["7", "8", "9", "/"],
#     ["4", "5", "6", "*"],
#     ["1", "2", "3", "-"],
#     ["C", "0", "=", "+"]
# ]

# for row in buttons:
#     frame = tk.Frame(button_frame)
#     frame.pack(fill="both", expand=True)
#     for btn in row:
#         b = tk.Button(frame, text=btn, font="Arial 18", height=2, width=4)
#         b.pack(side="left", expand=True, fill="both")
#         b.bind("<Button-1>", click)

# root.mainloop()