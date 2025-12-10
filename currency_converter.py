import customtkinter as ctk
from forex_python.converter import CurrencyRates

ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.geometry("400x500")
app.title("Currency Converter")
c = CurrencyRates()
currencies = ["USD", "EUR", "GBP", "JPY", "INR", "CAD", "AUD", "CHF", "CNY", "BTC"]
from_var = ctk.StringVar(value="USD")
to_var = ctk.StringVar(value="EUR")

def convert(*args):
    try:
        amount = float(entry.get() or 0)
        result = c.convert(from_var.get(), to_var.get(), amount)
        label.configure(text=f"{result:,.2f} {to_var.get()}")
    except:
        label.configure(text="Invalid")

# Fixed: Added .pack() to the title label
title_label = ctk.CTkLabel(app, text="Currency Converter", font=("Arial", 26))
title_label.pack(pady=20)

entry = ctk.CTkEntry(app, placeholder_text="Enter amount", font=("Arial",18), width=300)
entry.pack(pady=10)
entry.bind("<KeyRelease>", convert)

# From currency
ctk.CTkOptionMenu(app, values=currencies, variable=from_var).pack(pady=10)

# Arrow
ctk.CTkLabel(app, text="→", font=("Arial", 36)).pack(pady=5)

# To currency
ctk.CTkOptionMenu(app, values=currencies, variable=to_var).pack(pady=10)

# Trace variables to update on change
from_var.trace("w", convert)
to_var.trace("w", convert)

# Result label
label = ctk.CTkLabel(app, text="0.00 EUR", font=("Arial", 32), text_color="#00ff88")
label.pack(pady=30)

# Initial conversion
convert()

app.mainloop()
