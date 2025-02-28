import customtkinter as ctk
from tkinter import filedialog, Label, Toplevel
import pandas as pd
from datetime import datetime, timedelta
import pyperclip
import time

# Set Modern UI Theme
ctk.set_appearance_mode("System")  # Auto Light/Dark Mode
ctk.set_default_color_theme("blue")  # Modern Blue Theme

# Splash Screen
def show_splash():
    splash = Toplevel()
    splash.title("Loading...")
    splash.geometry("400x200")
    splash.configure(bg="#2C2F33")
    splash.overrideredirect(True)

    Label(splash, text="TC Birthday 2 Clipboard", font=("Arial", 18, "bold"), fg="white", bg="#2C2F33").pack(pady=30)
    Label(splash, text="Created by Jobin Bennykutty", font=("Arial", 12), fg="white", bg="#2C2F33").pack()

    # Show splash for 2 seconds
    splash.update()
    time.sleep(2)
    splash.destroy()

def get_past_week_birthdays(file_path):
    try:
        df = pd.read_csv(file_path)

        if "Name" not in df.columns or "Birthday" not in df.columns:
            return "Error: CSV must contain 'Name' and 'Birthday' columns."

        df["Birthday"] = pd.to_datetime(df["Birthday"], errors="coerce").dt.strftime("%m-%d")

        today = datetime.today()
        last_sunday = today - timedelta(days=today.weekday() + 1)
        last_monday = last_sunday - timedelta(days=6)

        past_week_dates = [(last_monday + timedelta(days=i)).strftime("%m-%d") for i in range(7)]

        past_week_birthdays = df[df["Birthday"].isin(past_week_dates)]

        if past_week_birthdays.empty:
            return "No birthdays found in the past week."

        # Only show names (no dates)
        result = "\n".join(f"{row['Name']}" for _, row in past_week_birthdays.iterrows())
        return result

    except Exception as e:
        return f"Error: {str(e)}"

def upload_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        result_text = get_past_week_birthdays(file_path)
        output_box.delete("0.0", "end")
        output_box.insert("0.0", result_text)

def copy_to_clipboard():
    text = output_box.get("0.0", "end").strip()
    if text:
        pyperclip.copy(text)

# Show Splash Screen Before Main App
show_splash()

# Create Main Window
root = ctk.CTk()
root.title("TC Birthday 2 Clipboard")
root.geometry("600x500")
root.resizable(False, False)  # Disable resizing for a clean UI

# Main Frame
frame = ctk.CTkFrame(root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Upload Button
upload_button = ctk.CTkButton(frame, text="📂 Upload CSV", command=upload_file, font=("Arial", 14), corner_radius=10)
upload_button.pack(pady=15)

# Output Box (Scrollable)
output_box = ctk.CTkTextbox(frame, height=15, width=55, font=("Arial", 12), wrap="word")
output_box.pack(pady=10, padx=10, fill="both", expand=True)

# Copy Button
copy_button = ctk.CTkButton(frame, text="📋 Copy to Clipboard", command=copy_to_clipboard, font=("Arial", 14), corner_radius=10)
copy_button.pack(pady=10)

# Run App
root.mainloop()
