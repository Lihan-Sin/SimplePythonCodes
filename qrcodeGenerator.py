import tkinter as tk
from tkinter import messagebox
import qrcode

def generate_qr():
    url = entry.get().strip()

    if not url:
        messagebox.showerror("Error", "Please enter a URL")
        return

    file_path = "/home/whoami/Desktop/qrcode.png"

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_path)

    messagebox.showinfo("Success", "QR code generated!\nSaved on Desktop")

# ---------------- GUI ----------------
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("350x200")
root.resizable(False, False)

label = tk.Label(root, text="Enter URL:", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

button = tk.Button(
    root,
    text="Generate QR Code",
    font=("Arial", 11),
    command=generate_qr
)
button.pack(pady=20)

root.mainloop()

