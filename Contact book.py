# import tkinter as tk
# from tkinter import messagebox
# from tkinter import ttk

# # Main app class
# class ContactBook:
#     def _init_(self, root):
#         self.root = root
#         self.root.title("Contact Book")
#         self.root.geometry("500x500")
#         self.contacts = []

#         # Title
#         title = tk.Label(root, text="Contact Book", font=("Arial", 18, "bold"))
#         title.pack(pady=10)

#         # Input fields
#         self.name_var = tk.StringVar()
#         self.phone_var = tk.StringVar()
#         self.email_var = tk.StringVar()

#         frame = tk.Frame(root)
#         frame.pack(pady=10)

#         tk.Label(frame, text="Name:").grid(row=0, column=0, sticky="e")
#         tk.Entry(frame, textvariable=self.name_var).grid(row=0, column=1, padx=10)

#         tk.Label(frame, text="Phone:").grid(row=1, column=0, sticky="e")
#         tk.Entry(frame, textvariable=self.phone_var).grid(row=1, column=1, padx=10)

#         tk.Label(frame, text="Email:").grid(row=2, column=0, sticky="e")
#         tk.Entry(frame, textvariable=self.email_var).grid(row=2, column=1, padx=10)

#         # Buttons
#         button_frame = tk.Frame(root)
#         button_frame.pack(pady=10)

#         tk.Button(button_frame, text="Add Contact", command=self.add_contact, width=15).grid(row=0, column=0, padx=5)
#         tk.Button(button_frame, text="Delete Contact", command=self.delete_contact, width=15).grid(row=0, column=1, padx=5)
#         tk.Button(button_frame, text="Clear Fields", command=self.clear_fields, width=15).grid(row=0, column=2, padx=5)

#         # Contact list
#         self.contact_list = ttk.Treeview(root, columns=("Name", "Phone", "Email"), show="headings", height=10)
#         self.contact_list.heading("Name", text="Name")
#         self.contact_list.heading("Phone", text="Phone")
#         self.contact_list.heading("Email", text="Email")
#         self.contact_list.pack(pady=10)

#     def add_contact(self):
#         name = self.name_var.get().strip()
#         phone = self.phone_var.get().strip()
#         email = self.email_var.get().strip()

#         if not name or not phone:
#             messagebox.showwarning("Input Error", "Name and phone are required!")
#             return

#         self.contacts.append((name, phone, email))
#         self.contact_list.insert("", "end", values=(name, phone, email))
#         self.clear_fields()

#     def delete_contact(self):
#         selected = self.contact_list.selection()
#         if not selected:
#             messagebox.showwarning("Select Contact", "No contact selected!")
#             return
#         for item in selected:
#             self.contact_list.delete(item)

#     def clear_fields(self):
#         self.name_var.set("")
#         self.phone_var.set("")
#         self.email_var.set("")


# # Run the app
# if _name_ == "_main_":
#     root = tk.Tk()
#     app = ContactBook(root)
#     root.mainloop()