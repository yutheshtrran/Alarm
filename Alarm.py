import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
import time
import threading

class AlarmClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Clock")
        self.root.geometry("400x300")
        self.root.configure(bg="black")

        self.time_label = tk.Label(root, font=('digital-7', 48), background='black', foreground='red')
        self.time_label.pack(pady=20)

        self.set_alarm_frame = ttk.Frame(root, style="TFrame")
        self.set_alarm_frame.pack(pady=20)

        ttk.Label(self.set_alarm_frame, text="Set Alarm (HH:MM:SS)", style="TLabel").grid(row=0, column=0, columnspan=3)

        self.hour_var = tk.StringVar(value='00')
        self.minute_var = tk.StringVar(value='00')
        self.second_var = tk.StringVar(value='00')

        self.hour_entry = ttk.Entry(self.set_alarm_frame, textvariable=self.hour_var, width=3, font=('digital-7', 20))
        self.minute_entry = ttk.Entry(self.set_alarm_frame, textvariable=self.minute_var, width=3, font=('digital-7', 20))
        self.second_entry = ttk.Entry(self.set_alarm_frame, textvariable=self.second_var, width=3, font=('digital-7', 20))

        self.hour_entry.grid(row=1, column=0)
        self.minute_entry.grid(row=1, column=1)
        self.second_entry.grid(row=1, column=2)

        self.set_alarm_button = ttk.Button(root, text="Set Alarm", command=self.set_alarm)
        self.set_alarm_button.pack(pady=20)

        self.alarm_time = None
        self.update_time()

    def update_time(self):
        now = datetime.now().strftime('%H:%M:%S')
        self.time_label.config(text=now)
        self.root.after(1000, self.update_time)

    def set_alarm(self):
        hours = int(self.hour_var.get())
        minutes = int(self.minute_var.get())
        seconds = int(self.second_var.get())
        self.alarm_time = datetime.now() + timedelta(hours=hours, minutes=minutes, seconds=seconds)
        threading.Thread(target=self.alarm_thread).start()

    def alarm_thread(self):
        while True:
            if datetime.now() >= self.alarm_time:
                self.show_alarm_message()
                break
            time.sleep(1)

    def show_alarm_message(self):
        alarm_popup = tk.Toplevel(self.root)
        alarm_popup.title("Alarm")
        alarm_popup.geometry("200x100")
        alarm_popup.configure(bg="black")
        tk.Label(alarm_popup, text="Time's up!", font=('digital-7', 20), bg='black', fg='red').pack(pady=20)
        tk.Button(alarm_popup, text="OK", command=alarm_popup.destroy).pack(pady=10)

root = tk.Tk()
style = ttk.Style()
style.configure("TFrame", background="black")
style.configure("TLabel", background="black", foreground="red", font=('digital-7', 12))
style.configure("TButton", background="black", foreground="red", font=('digital-7', 12))

alarm_clock = AlarmClock(root)
root.mainloop()
