from tkinter import *
from tkinter import messagebox
import requests

# ---------------- Window ----------------
w = Tk()
w.title("Commodity Price Converter")
w.geometry("600x400")

Label(w, text="Commodity Price Converter", font=("Arial", 20, "bold")).pack(pady=20)

# ---------------- Variables ----------------
commodity_var = StringVar(value="Gold")

# ---------------- Commodity List ----------------
commodities = ["Gold", "Silver", "Copper"]

Label(w, text="Select Commodity:", font=("Arial", 14)).pack()
OptionMenu(w, commodity_var, *commodities).pack(pady=5)

Label(w, text="Weight (in grams):", font=("Arial", 14)).pack()
weight_entry = Entry(w, font=("Arial", 14))
weight_entry.pack(pady=5)

result_label = Label(w, text="", font=("Arial", 16, "bold"))
result_label.pack(pady=20)

# ---------------- Functions ----------------
def calculate_price():
    try:
        weight = float(weight_entry.get())
        commodity = commodity_var.get().lower()

        # Live metals API
        url = "https://api.metals.live/v1/spot"
        response = requests.get(url).json()

        # Convert list → dictionary
        prices = {item[0]: item[1] for item in response}

        price_per_ounce = prices[commodity]
        price_per_gram = price_per_ounce / 31.1035  # ounce → gram

        usd_to_inr = 83  # approx conversion rate
        total_price = weight * price_per_gram * usd_to_inr

        result_label.config(text=f"Total Price: ₹ {total_price:.2f}")

    except:
        messagebox.showerror("Error", "Please enter valid weight")

def clear_data():
    weight_entry.delete(0, END)
    result_label.config(text="")

# ---------------- Buttons ----------------
Button(w, text="Calculate Price", font=("Arial", 12, "bold"), command=calculate_price).pack(pady=5)
Button(w, text="Clear", font=("Arial", 12), command=clear_data).pack(pady=5)

w.mainloop()
