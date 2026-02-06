import tkinter as tk
from tkinter import messagebox, scrolledtext
from Scanner import Scanner  
import ipaddress

class VulnScanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("VulnScan - By Nigesh Shrestha")
        self.root.geometry("600x450")
        self.root.resizable(False, False)
        self.scanner = Scanner()
      
        tk.Label(
            root,
            text="VulnScan",
            font=("Arial", 18, "bold")
        ).pack(pady=10)

        frame = tk.Frame(root)
        frame.pack(pady=5)
        
        tk.Label(frame, text="Target IP:").grid(row=0, column=0, padx=5)
        self.target_entry = tk.Entry(frame, width=30)
        self.target_entry.grid(row=0, column=1)
        self.target_entry.insert(0, "127.0.0.1")

        tk.Button(
            root,
            text="Start Scan",
            command=self.start_scan,
            bg="#2c7be5",
            fg="white",
            width=20
        ).pack(pady=10)
      
        self.output = scrolledtext.ScrolledText(
            root,
            width=70,
            height=15
        )
        self.output.pack(padx=10, pady=10)
        
        tk.Label(
            root,
            text="CW1 Project",
            font=("Arial", 9, "italic")
        ).pack(pady=5)
   
    def is_valid_ip(self, ip):
        try:
            ipaddress.ip_address(ip)
            return True
        except ValueError:
            return False
 
    def start_scan(self):
        target = self.target_entry.get().strip()
        ports = [21, 22, 80, 443]

        if not target:
            messagebox.showerror("Error", "Please enter a target IP")
            return

        if not self.is_valid_ip(target):
            messagebox.showerror("Error", "Invalid IP Address")
            return

        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, "Scanning...\n\n")

        try:
            report = self.scanner.run_scan(target, ports)
            self.output.insert(tk.END, report)
        except Exception as e:
            messagebox.showerror("Scan Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = VulnScanGUI(root)
    root.mainloop()
