import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import webbrowser
import urllib.parse
import time


contacts = []


def upload_excel():

    global contacts

    file_path = filedialog.askopenfilename(
        title="Select Excel File",
        filetypes=[
            ("Excel Files", "*.xlsx"),
            ("Excel Files", "*.xls")
        ]
    )

    if not file_path:
        return

    try:

        df = pd.read_excel("D:\Book1.xlsx")

        if "phone_number" not in df.columns:

            messagebox.showerror(
                "Error",
                "Excel must contain a column named phone_number"
            )

            return

        contacts.clear()

        for number in df["phone_number"].dropna():

            number = str(number).strip()

            number = number.replace("+", "")
            number = number.replace(" ", "")

            if number.endswith(".0"):
                number = number[:-2]

            if number.isdigit():
                contacts.append(number)

        # Remove duplicates
        contacts[:] = list(dict.fromkeys(contacts))

        file_status.config(
            text=f"{len(contacts)} numbers loaded"
        )

        messagebox.showinfo(
            "Success",
            f"{len(contacts)} numbers loaded successfully."
        )

    except Exception as error:

        messagebox.showerror(
            "Excel Error",
            str(error)
        )


def open_whatsapp():

    webbrowser.open(
        "https://web.whatsapp.com"
    )

    messagebox.showinfo(
        "WhatsApp Web",
        "WhatsApp Web has been opened.\n\n"
        "Log in by scanning the QR code if required."
    )


def start_process():

    if not contacts:

        messagebox.showwarning(
            "No Contacts",
            "Please upload an Excel file first."
        )

        return

    message = message_box.get(
        "1.0",
        tk.END
    ).strip()

    if not message:

        messagebox.showwarning(
            "No Message",
            "Please enter a message."
        )

        return

    process_button.config(
        state=tk.DISABLED
    )

    process_contacts(
        message
    )


def process_contacts(message):

    for index, number in enumerate(contacts):

        encoded_message = urllib.parse.quote(
            message
        )

        url = (
            "https://web.whatsapp.com/send"
            f"?phone={number}"
            f"&text={encoded_message}"
        )

        webbrowser.open(
            url
        )

        status_label.config(
            text=f"Opened {index + 1} / {len(contacts)}"
        )

        root.update()

        # Give WhatsApp Web time to load.
        # The actual send should be confirmed manually.
        time.sleep(5)

        answer = messagebox.askyesno(
            "Send Message",
            f"WhatsApp chat opened for:\n\n"
            f"{number}\n\n"
            f"Click Yes after you have checked the message "
            f"and sent it."
        )

        if not answer:

            messagebox.showinfo(
                "Stopped",
                "Process stopped by user."
            )

            break

    else:

        messagebox.showinfo(
            "Completed",
            "All contacts have been processed."
        )

    process_button.config(
        state=tk.NORMAL
    )


# ------------------------------------------------
# GUI
# ------------------------------------------------

root = tk.Tk()

root.title(
    "WhatsApp Web Message Tool"
)

root.geometry(
    "650x550"
)

root.resizable(
    False,
    False
)


title = tk.Label(
    root,
    text="WhatsApp Web Message Tool",
    font=("Arial", 20, "bold")
)

title.pack(
    pady=20
)


# WhatsApp Web
whatsapp_button = tk.Button(
    root,
    text="OPEN WHATSAPP WEB",
    command=open_whatsapp,
    width=25,
    height=2
)

whatsapp_button.pack(
    pady=10
)


# Upload Excel
upload_button = tk.Button(
    root,
    text="UPLOAD EXCEL",
    command=upload_excel,
    width=25,
    height=2
)

upload_button.pack(
    pady=10
)


file_status = tk.Label(
    root,
    text="No contacts loaded",
    font=("Arial", 11)
)

file_status.pack(
    pady=5
)


# Message
message_title = tk.Label(
    root,
    text="Message",
    font=("Arial", 13, "bold")
)

message_title.pack(
    anchor="w",
    padx=50,
    pady=(20, 5)
)


message_box = tk.Text(
    root,
    width=65,
    height=7,
    font=("Arial", 11)
)

message_box.pack()


# Process
process_button = tk.Button(
    root,
    text="START",
    command=start_process,
    width=25,
    height=2,
    font=("Arial", 12, "bold")
)

process_button.pack(
    pady=20
)


status_label = tk.Label(
    root,
    text="Ready",
    font=("Arial", 11)
)

status_label.pack()


root.mainloop()