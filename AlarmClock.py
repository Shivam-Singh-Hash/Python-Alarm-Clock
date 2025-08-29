import os
import requests
from threading import Thread
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
from datetime import datetime
from PIL import Image, ImageTk
from pygame import mixer
from time import sleep

# === AUTO-DOWNLOAD IMAGE AND SOUND IF MISSING ===
if not os.path.exists("clock.png"):
    url = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Clock_font_awesome.svg/1024px-Clock_font_awesome.svg.png"
    with open("clock.png", "wb") as f:
        f.write(requests.get(url).content)

if not os.path.exists("alarm.mp3"):
    sound_url = "https://www.soundjay.com/misc/sounds/bell-ringing-05.mp3"
    with open("alarm.mp3", "wb") as f:
        f.write(requests.get(sound_url).content)

# === WINDOW SETUP ===
window = Tk()
window.title("Advanced Alarm Clock")
window.geometry("600x550")
window.configure(bg="#f0f0f0")

# === MIXER SETUP ===
mixer.init()

# === LIVE CLOCK ===
def update_time():
    now = datetime.now().strftime("%I:%M:%S %p")
    clock_label.config(text=now)
    window.after(1000, update_time)

clock_label = Label(window, text="", font=('Arial', 28, 'bold'), bg="#f0f0f0", fg="#333")
clock_label.pack(pady=10)
update_time()
clock_img_path = r"C:\Users\shiva\AlarmItems\top-view-wall-clock-still-life.jpg"
if os.path.exists(clock_img_path):
    img = Image.open(clock_img_path)
else:
    img = Image.open("clock.png")  # fallback

# === CLOCK IMAGE ===
img = Image.open(r"C:\Users\shiva\AlarmItems\top-view-wall-clock-still-life.jpg")
img = img.resize((100, 100))
img = ImageTk.PhotoImage(img)
img_label = Label(window, image=img, bg="#f0f0f0")
img_label.pack()

# === ALARM FORM ===
form_frame = Frame(window, bg="#f0f0f0")
form_frame.pack(pady=10)

Label(form_frame, text="Hour", bg="#f0f0f0").grid(row=0, column=0)
Label(form_frame, text="Min", bg="#f0f0f0").grid(row=0, column=1)
Label(form_frame, text="Sec", bg="#f0f0f0").grid(row=0, column=2)
Label(form_frame, text="AM/PM", bg="#f0f0f0").grid(row=0, column=3)
Label(form_frame, text="Repeat", bg="#f0f0f0").grid(row=0, column=4)

c_hour = Combobox(form_frame, width=3, values=[f"{i:02}" for i in range(1, 13)])
c_hour.current(0)
c_hour.grid(row=1, column=0)

c_min = Combobox(form_frame, width=3, values=[f"{i:02}" for i in range(60)])
c_min.current(0)
c_min.grid(row=1, column=1)

c_sec = Combobox(form_frame, width=3, values=[f"{i:02}" for i in range(60)])
c_sec.current(0)
c_sec.grid(row=1, column=2)

c_period = Combobox(form_frame, width=4, values=["AM", "PM"])
c_period.current(0)
c_period.grid(row=1, column=3)

c_day = Combobox(form_frame, width=12, values=[
    "Every Day", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
c_day.current(0)
c_day.grid(row=1, column=4)

# === ALARM LIST ===
alarms = []

tree_frame = Frame(window, bg="#f0f0f0")
tree_frame.pack()

tree = Treeview(tree_frame, columns=("Time", "Repeat"), show='headings', height=5)
tree.heading("Time", text="Time")
tree.heading("Repeat", text="Repeat")
tree.column("Time", width=120, anchor=CENTER)
tree.column("Repeat", width=120, anchor=CENTER)
tree.pack(pady=10)

# === FUNCTIONS ===
def add_alarm():
    alarm = {
        "hour": c_hour.get(),
        "minute": c_min.get(),
        "second": c_sec.get(),
        "period": c_period.get(),
        "day": c_day.get()
    }
    alarms.append(alarm)
    time_str = f"{alarm['hour']}:{alarm['minute']}:{alarm['second']} {alarm['period']}"
    tree.insert('', END, values=(time_str, alarm['day']))
    print("Added:", alarm)

def sound_alarm(alarm):
    try:
        mixer.music.load("alarm.mp3")
        mixer.music.play()
        messagebox.showinfo("Alarm", f"Alarm is ringing!\n{alarm['hour']}:{alarm['minute']} {alarm['period']}")
    except Exception as e:
        print("Sound error:", e)

def check_alarms():
    while True:
        now = datetime.now()
        current = {
            "hour": now.strftime("%I"),
            "minute": now.strftime("%M"),
            "second": now.strftime("%S"),
            "period": now.strftime("%p"),
            "day": now.strftime("%A")
        }
        for alarm in alarms:
            if (alarm["hour"] == current["hour"] and
                alarm["minute"] == current["minute"] and
                alarm["second"] == current["second"] and
                alarm["period"] == current["period"]):

                if alarm["day"] == "Every Day" or alarm["day"] == current["day"]:
                    sound_alarm(alarm)
                    sleep(1)
        sleep(1)

# === THREAD FOR ALARMS ===
Thread(target=check_alarms, daemon=True).start()

# === BUTTON ===
Button(window, text="Add Alarm", command=add_alarm, font=('Arial', 12)).pack(pady=10)

# === MAIN LOOP ===
window.mainloop()
