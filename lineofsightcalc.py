import tkinter as tk
from tkinter import ttk
import math

k = 4/3

def calculate():
    try:
        h1 = float(entry_h1.get())
        h2 = float(entry_h2.get())

        d1 = 3.57 * math.sqrt(k * h1)
        d2 = 3.57 * math.sqrt(k * h2)
        total = d1 + d2

        result1.config(text=f"{d1:.2f} km")
        result2.config(text=f"{d2:.2f} km")
        result_total.config(text=f"{total:.2f} km")

    except:
        result_total.config(text="Invalid Input")

def clear():
    entry_h1.delete(0, tk.END)
    entry_h2.delete(0, tk.END)
    result1.config(text="")
    result2.config(text="")
    result_total.config(text="")

root = tk.Tk()
root.title("Line of Sight Calculator")
root.geometry("400x400")

title = tk.Label(root, text="Line of Sight Calculator", font=("arial", 22), fg="#0b3d91")
title.pack(pady=12)

frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="Antenna Height (1st Station):").grid(row=0, column=0)
entry_h1 = tk.Entry(frame)
entry_h1.grid(row=0, column=1)

tk.Label(frame, text="Antenna Height (2nd Station):").grid(row=1, column=0)
entry_h2 = tk.Entry(frame)
entry_h2.grid(row=1, column=1)

entry_h2.grid(row=1, column=1, pady=10)

tk.Button(root, text="Calculate", command=calculate).pack(pady=5)
tk.Button(root, text="Clear", command=clear).pack(pady=5)

results = tk.Frame(root)
results.pack(pady=10)

tk.Label(results, text="Radio Horizon (1st Station):").grid(row=0, column=0, sticky="w")
frame_r1 = tk.Frame(results, bd=2, relief="sunken", padx=5, pady=5)
frame_r1.grid(row=0, column=1, sticky="w", pady=2)
result1 = tk.Label(frame_r1, text="")
result1.pack()

tk.Label(results, text="Radio Horizon (2nd Station):").grid(row=1, column=0, sticky="w")
frame_r2 = tk.Frame(results, bd=2, relief="sunken", padx=5, pady=5)
frame_r2.grid(row=1, column=1, sticky="w", pady=2)
result2 = tk.Label(frame_r2, text="")
result2.pack()

tk.Label(results, text="Total Line Of Sight:").grid(row=2, column=0, sticky="w")
frame_total = tk.Frame(results, bd=2, relief="sunken", padx=5, pady=5)
frame_total.grid(row=2, column=1, sticky="w", pady=2)
result_total = tk.Label(frame_total, text="")
result_total.pack()

root.mainloop()