import tkinter as tk
from tkinter import ttk, messagebox
import random
import time
from datetime import datetime

class SoftwareBnBHacking:
    def __init__(self, master):
        self.master = master
        self.master.title("Software BnB Hacking")
        self.master.geometry("500x400")
        self.history_file = "activity_history.txt"

        # UI Components
        tk.Label(master, text="Enter Airbnb Account Email:", font=("Arial", 14)).pack(pady=10)
        self.email_entry = tk.Entry(master, font=("Arial", 12), width=40)
        self.email_entry.pack(pady=5)

        self.start_button = tk.Button(master, text="Start Hacking", command=self.start_hacking, bg="red", fg="white", font=("Arial", 12), width=15)
        self.start_button.pack(pady=10)

        self.status_label = tk.Label(master, text="", font=("Arial", 12))
        self.status_label.pack(pady=10)

        self.progress_bar = ttk.Progressbar(master, orient="horizontal", length=300, mode="determinate")
        self.progress_bar.pack(pady=5)

        tk.Label(master, text="Result Log:", font=("Arial", 12, "bold")).pack(pady=5)
        self.result_text = tk.Text(master, font=("Arial", 10), width=60, height=10, state="disabled")
        self.result_text.pack(pady=10)

    def start_hacking(self):
        """Start the hacking process and simulate generating account information."""
        email = self.email_entry.get()
        if not email.strip():
            messagebox.showerror("Error", "Please enter an email address.")
            return

        self.status_label.config(text="Scanning in progress...", fg="blue")
        self.progress_bar["value"] = 0
        self.master.update_idletasks()

        # Simulate progress and delay
        for _ in range(20):
            self.progress_bar["value"] += 5
            self.master.update_idletasks()
            time.sleep(0.1)

        # Generate fake account information
        details = self.generate_fake_account_info(email)
        self.log_activity(details)

        # Display results
        self.status_label.config(text="Scanning Complete.", fg="green")
        self.result_text.config(state="normal")
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, details)
        self.result_text.config(state="disabled")

    def generate_fake_account_info(self, email):
        """Generate fake account information for the given email."""
        fake_details = f"""
Account Email: {email}
Location: {random.choice(['New York, USA', 'London, UK', 'Berlin, Germany', 'Tokyo, Japan', 'Sydney, Australia'])}
IP Address: 192.168.1.{random.randint(1, 254)}
Account Status: Hacked and cannot be recovered with standard recovery software.
Recovery Info: Specialized software is required to recover this account.
Security Level: {random.choice(['High', 'Medium', 'Low'])}
Last Login: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """
        return fake_details

    def log_activity(self, details):
        """Log the generated details into a file."""
        with open(self.history_file, "a") as f:
            f.write(f"{datetime.now()} | {details.strip()}\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = SoftwareBnBHacking(root)
    root.mainloop()
