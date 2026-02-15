from tkinter import *
from tkinter import messagebox
import requests
import csv
import os

w = Tk()
w.title("Currency Converter")
w.geometry("650x500")

Label(w, text="Currency Converter", font=("Arial", 20)).grid(row=0, column=0, columnspan=2, pady=20)

currencies = ["USD", "INR", "EUR","IRR" ,"GBP","KWD", "JPY", "AUD", "CAD", "MXN", "CHF", "CNY", "SGD", "NZD", "ZAR", "AED", "USD", "INR", "EUR", "GBP", "JPY", "AUD", "CAD", "MXN", "CHF", "CNY", "SGD", "NZD", "ZAR", "AED"]

from_var = StringVar(value="USD")
to_var = StringVar(value="INR")


Label(w, text="From Currency:", font=("Roboto", 14, "bold")).grid(row=1, column=0, padx=10, pady=10, sticky="w")
from_menu = OptionMenu(w, from_var, *currencies)
from_menu.config(font=("Arial", 12), width=20)
from_menu.grid(row=1, column=1, padx=10, pady=10)


Label(w, text="To Currency:", font=("Roboto", 14, "bold")).grid(row=2, column=0, padx=10, pady=10, sticky="w")
to_menu = OptionMenu(w, to_var, *currencies)
to_menu.config(font=("Arial", 12), width=20)
to_menu.grid(row=2, column=1, padx=10, pady=10)

Label(w, text="Amount:", font=("Roboto", 14, "bold")).grid(row=3, column=0, padx=10, pady=10, sticky="w")
amount_entry = Entry(w, width=25, font=("Arial", 14))
amount_entry.grid(row=3, column=1, padx=10, pady=10)

Label(w, text="Converted Amount:", font=("Arial", 12, "bold")).grid(row=5, column=0, sticky="w", padx=10, pady=10)
result_label = Label(w, text="", font=("Arial", 14))
result_label.grid(row=5, column=1, sticky="w")


def clear_data():
    amount_entry.delete(0, END)
    result_label.config(text="")
    from_var.set("USD")
    to_var.set("INR")

def convert_currency():
    from_cur = from_var.get()
    to_cur = to_var.get()
    amount = amount_entry.get()

    if amount == "":
        messagebox.showerror("Error", "Please enter amount")
        return

    try:
        url = f"https://api.exchangerate-api.com/v4/latest/{from_cur}"
        data = requests.get(url).json()

        rate = data["rates"].get(to_cur)
        if rate is None:
            messagebox.showerror("Error", "Currency not supported")
            return

        converted = float(amount) * rate
        result_label.config(text=f"{converted:.2f} {to_cur}")

    except Exception as e:
        messagebox.showerror("Error", f"Conversion failed\n{e}")

def save_to_csv():
    if result_label.cget("text") == "":
        messagebox.showerror("Error", "No data to save")
        return

    file_exists = os.path.isfile("currency data.csv")
    with open("currency data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["From", "To", "Amount", "Converted"])
        writer.writerow([
            from_var.get(),
            to_var.get(),
            amount_entry.get(),
            result_label.cget("text")
        ])

    messagebox.showinfo("Saved", "Data saved to currency data.csv")


Button(w, text="Convert Currency", command=convert_currency, font=("Arial", 12, "bold")).grid(row=4, column=0, columnspan=2, pady=10)
Button(w, text="Clear Data", command=clear_data, font=("Arial", 12, "bold")).grid(row=6, column=0, columnspan=2, pady=10)
Button(w, text="Save to CSV", command=save_to_csv, font=("Arial", 12, "bold")).grid(row=7, column=0, columnspan=2, pady=10)

w.mainloop()
