import tkinter as tk

window = tk.Tk()
window.title("Elevator")
window.geometry("200x400")

# Create elevator buttons
for floor in range(5, -1, -1):
    button = tk.Button(
        window,
        text=str(floor),
        width=8,
        height=2,
        font=("Arial", 14)
    )
    button.pack(pady=3)

window.mainloop()