from currency_converter import CurrencyConverter
import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.geometry("650x450")
window.title("Currency Converter")


# Currency code list
currencies = [
    "USD",  # US Dollar
    "INR",  # Indian Rupee
    "EUR",  # Euro
    "GBP",  # British Pound
    "JPY",  # Japanese Yen
    "AUD",  # Australian Dollar
    "CAD",  # Canadian Dollar
    "CHF",  # Swiss Franc
    "CNY",  # Chinese Yuan
    "AED",  # UAE Dirham
    "SAR",  # Saudi Riyal
    "SGD",  # Singapore Dollar
    "NZD",  # New Zealand Dollar
    "KRW",  # South Korean Won
    "THB",  # Thai Baht
    "MYR",  # Malaysian Ringgit
]


def clicked():
    try:
        amount = float(amount_entry.get())

        from_currency = from_currency_box.get()
        to_currency = to_currency_box.get()

        if not from_currency or not to_currency:
            result_label.config(
                text="Please select both currencies!",
                fg="red"
            )
            return

        c = CurrencyConverter()

        converted_amount = c.convert(
            amount,
            from_currency,
            to_currency
        )

        result_label.config(
            text=f"{amount} {from_currency} = "
                 f"{converted_amount:.2f} {to_currency}",
            fg="green"
        )

    except ValueError:
        result_label.config(
            text="Please enter a valid amount!",
            fg="red"
        )

    except Exception as error:
        result_label.config(
            text=f"Error: {error}",
            fg="red"
        )


# ---------------- TITLE ----------------

title_label = tk.Label(
    window,
    text="Currency Converter",
    font=("Arial", 20, "bold")
)
title_label.place(x=220, y=30)


# ---------------- AMOUNT ----------------

amount_label = tk.Label(
    window,
    text="Enter Amount:",
    font=("Arial", 16)
)
amount_label.place(x=50, y=100)

amount_entry = tk.Entry(
    window,
    font=("Arial", 16)
)
amount_entry.place(x=300, y=100)


# ---------------- FROM CURRENCY ----------------

from_currency_label = tk.Label(
    window,
    text="From Currency:",
    font=("Arial", 16)
)
from_currency_label.place(x=50, y=150)

from_currency_box = ttk.Combobox(
    window,
    values=currencies,
    font=("Arial", 16),
    state="readonly"
)
from_currency_box.place(x=300, y=150)

# Default value
from_currency_box.set("USD")


# ---------------- TO CURRENCY ----------------

to_currency_label = tk.Label(
    window,
    text="To Currency:",
    font=("Arial", 16)
)
to_currency_label.place(x=50, y=200)

to_currency_box = ttk.Combobox(
    window,
    values=currencies,
    font=("Arial", 16),
    state="readonly"
)
to_currency_box.place(x=300, y=200)

# Default value
to_currency_box.set("INR")


# ---------------- BUTTON ----------------

convert_button = tk.Button(
    window,
    text="Convert",
    font=("Arial", 14),
    command=clicked
)
convert_button.place(x=270, y=260)


# ---------------- RESULT ----------------

result_label = tk.Label(
    window,
    text="",
    font=("Arial", 14)
)
result_label.place(x=100, y=330)


window.mainloop()