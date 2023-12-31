import tkinter as tk
from tkinter import messagebox
import time
import threading
import winsound


def set_alarm():
    alarm_time = entry.get()
    try:
        alarm_time = time.strptime(alarm_time, "%H:%M")
        alarm_thread = threading.Thread(target=check_alarm, args=(alarm_time,))
        alarm_thread.start()
        status_label.config(
            text=f"Alarm set for {time.strftime('%H:%M', alarm_time)}")
    except ValueError:
        messagebox.showerror("Error", "Invalid time format! Use HH:MM")


def check_alarm(alarm_time):
    while True:
        current_time = time.localtime()
        if current_time.tm_hour == alarm_time.tm_hour and current_time.tm_min == alarm_time.tm_min:
            messagebox.showinfo("Alarm", "Time's up!")
            play_alarm_sound()
            break
        time.sleep(1)


def play_alarm_sound():

    winsound.Beep(1000, 2000)


app = tk.Tk()
app.title("Alarm Clock")

frame = tk.Frame(app)
frame.pack(pady=10)

entry = tk.Entry(frame, font=("Helvetica", 24))
entry.pack(side=tk.LEFT, padx=10)

set_button = tk.Button(frame, text="Set Alarm", command=set_alarm)
set_button.pack(side=tk.LEFT)

status_label = tk.Label(
    app, text="Enter alarm time (HH:MM)", font=("Helvetica", 18))
status_label.pack(pady=10)

app.mainloop()
