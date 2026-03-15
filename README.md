<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,9,24&height=200&section=header&text=Advanced%20Alarm%20Clock&fontSize=52&fontColor=fff&animation=twinkling&fontAlignY=35&desc=A%20feature-rich%20desktop%20alarm%20app%20built%20with%20Python%20%26%20Tkinter&descAlignY=58&descSize=17" width="100%"/>

<br/>

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-Built--in-FF6F00?style=for-the-badge&logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-Audio-00B140?style=for-the-badge&logo=python&logoColor=white)
![Pillow](https://img.shields.io/badge/Pillow-Imaging-4F8EF7?style=for-the-badge&logo=python&logoColor=white)

![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Mac%20%7C%20Linux-informational?style=for-the-badge&logo=windows&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge&logo=opensourceinitiative&logoColor=white)
![Stars](https://img.shields.io/github/stars/Shivam-Singh-Hash/advanced-alarm-clock?style=for-the-badge&color=gold&logo=github)

<br/>

**⏰ Real-time Clock · 🔔 Multi-Alarm · 🔁 Repeat Scheduling · 🎵 Audio Alerts**

<br/>

[🚀 Quick Start](#-installation) &nbsp;·&nbsp; [✨ Features](#-features) &nbsp;·&nbsp; [📸 Screenshots](#-screenshots) &nbsp;·&nbsp; [🗺️ Roadmap](#-roadmap) &nbsp;·&nbsp; [🤝 Contribute](#-contributing)

<br/>

</div>

---

## 📖 Overview

**Advanced Alarm Clock** is a fully-featured desktop application built entirely in Python. It combines a live digital clock, a multi-alarm scheduler with day-of-week repeat options, and audio alerts — all wrapped in a clean, native GUI powered by Tkinter. Whether you need a daily wake-up call or a weekly reminder, this app has you covered with zero external cloud dependencies.

> 💡 Built for developers who want a lightweight, fully customizable alarm system they can run and modify locally.

---

## ✨ Features

<div align="center">

| Feature | Description |
|--------|-------------|
| ⏰ **Live Digital Clock** | Real-time clock updating every second in a bold, readable display |
| ➕ **Multiple Alarms** | Add as many alarms as you need — all tracked in a clean table view |
| 🔁 **Repeat Scheduling** | Set alarms to ring Every Day or on a specific day of the week |
| 🎵 **Audio Alert** | Plays an MP3 alarm sound via Pygame mixer when triggered |
| 🖼️ **Clock Image** | Displays a clock image for a visual, polished look |
| 📋 **Alarm List View** | All active alarms shown in a Treeview table — Time + Repeat |
| 🔔 **Pop-up Notification** | A messagebox pops up when any alarm fires |
| 🌐 **Auto-download Assets** | Automatically fetches the clock image and sound if missing |
| 🧵 **Background Threading** | Alarm checking runs in a daemon thread — UI stays perfectly responsive |

</div>

---

## 📸 Screenshots

<div align="center">

<table>
  <tr>
    <td align="center">
      <img src="https://placehold.co/380x240/1a1a2e/e94560?text=⏰+Main+Clock+View&font=montserrat" width="360" alt="Main Clock View"/>
      <br/><sub><b>Live Digital Clock + Clock Image</b></sub>
    </td>
    <td align="center">
      <img src="https://placehold.co/380x240/1a1a2e/f5a623?text=➕+Add+Alarm+Form&font=montserrat" width="360" alt="Alarm Form"/>
      <br/><sub><b>Alarm Scheduler — Hour / Min / Sec / Repeat</b></sub>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="https://placehold.co/380x240/1a1a2e/00b140?text=📋+Alarm+List+View&font=montserrat" width="360" alt="Alarm List"/>
      <br/><sub><b>Active Alarms in Treeview Table</b></sub>
    </td>
    <td align="center">
      <img src="https://placehold.co/380x240/1a1a2e/4f8ef7?text=🔔+Alarm+Ringing!&font=montserrat" width="360" alt="Alarm Triggered"/>
      <br/><sub><b>Popup Notification + Audio Alert</b></sub>
    </td>
  </tr>
</table>

> 📷 Replace placeholders above with real screenshots from your app!

</div>

---

## 🏗️ How It Works

```
┌──────────────────────────────────────────────────────┐
│                  TKINTER GUI (Main Thread)            │
│                                                      │
│   ┌─────────────┐   ┌──────────────────────────┐    │
│   │  Live Clock │   │      Alarm Form          │    │
│   │  (Label)    │   │  Hour / Min / Sec /      │    │
│   │  Updates    │   │  AM-PM / Repeat Day      │    │
│   │  every 1s   │   │  → Add Alarm Button      │    │
│   └─────────────┘   └──────────────────────────┘    │
│                                                      │
│         ┌─────────────────────────────┐             │
│         │    Alarm Treeview Table     │             │
│         │  Time         │  Repeat     │             │
│         │  08:00:00 AM  │  Every Day  │             │
│         │  09:30:00 AM  │  Monday     │             │
│         └─────────────────────────────┘             │
└──────────────────────────┬───────────────────────────┘
                           │
                  (daemon Thread)
                           │
                           ▼
┌──────────────────────────────────────────────────────┐
│              ALARM CHECKER (Background Thread)        │
│                                                      │
│   Runs every second → compares current time          │
│   against all alarms in list                         │
│                                                      │
│   Match found?                                       │
│       ↓                                              │
│   ┌───────────────────────────────────┐             │
│   │  Pygame Mixer → plays alarm.mp3   │             │
│   │  Tkinter Messagebox → popup alert │             │
│   └───────────────────────────────────┘             │
└──────────────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

<div align="center">

### Core GUI
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-Built--in-FF6F00?style=for-the-badge&logo=python&logoColor=white)

### Audio & Image
![Pygame](https://img.shields.io/badge/Pygame-Mixer-00B140?style=for-the-badge&logo=python&logoColor=white)
![Pillow](https://img.shields.io/badge/Pillow-PIL-4F8EF7?style=for-the-badge&logo=python&logoColor=white)

### Networking (asset fetch)
![Requests](https://img.shields.io/badge/Requests-HTTP-FF4444?style=for-the-badge&logo=python&logoColor=white)

</div>

---

## 📁 Project Structure

```
📦 advanced-alarm-clock/
│
├── 🐍 alarm_clock.py        ← Main application (all logic + GUI)
├── 🔔 alarm.mp3             ← Alarm sound (auto-downloaded if missing)
├── 🖼️  clock.png             ← Clock icon (auto-downloaded if missing)
└── 📄 README.md
```

> ✅ **No complex folder structure needed** — everything runs from a single Python file.

---

## 🚀 Installation

### Prerequisites

```bash
# Check Python version (3.8+ required)
python --version
```

### Step 1 — Clone the repository

```bash
git clone https://github.com/Shivam-Singh-Hash/advanced-alarm-clock.git
cd advanced-alarm-clock
```

### Step 2 — Install dependencies

```bash
pip install pillow pygame requests
```

> Tkinter comes **built into Python** — no separate install needed.

### Step 3 — Run the app

```bash
python alarm_clock.py
```

> 🎵 The app will **automatically download** `alarm.mp3` and `clock.png` on first run if they're missing.

---

## 💻 Usage

**Step 1** — Launch the app with `python alarm_clock.py`

**Step 2** — Look at the live clock at the top to confirm current time

**Step 3** — Use the dropdown menus to set:
  - **Hour** (01–12)
  - **Minute** (00–59)
  - **Second** (00–59)
  - **AM / PM**
  - **Repeat** — Every Day, or a specific weekday

**Step 4** — Click **Add Alarm** — it appears in the alarm list instantly

**Step 5** — When the time matches, the alarm plays audio and shows a popup 🔔

**Step 6** — Add as many alarms as you need — they all run simultaneously in the background

---

## 🗺️ Roadmap

```
✅  v1.0  — Live digital clock (updates every second)
✅  v1.0  — Add / display multiple alarms
✅  v1.0  — Repeat by day of week
✅  v1.0  — MP3 audio alert via Pygame
✅  v1.0  — Popup notification on alarm trigger
✅  v1.0  — Auto-download missing assets
```

```
🔜  v1.1  — Delete / disable individual alarms from the list
🔜  v1.1  — Snooze button (5 / 10 min options)
🔜  v1.2  — Custom alarm label / name per alarm
🔜  v1.2  — Volume control slider
🔜  v1.3  — Custom ringtone — browse & upload your own MP3
🔜  v1.3  — Dark / Light mode toggle
🔜  v2.0  — Save alarms to a file (persist after app restarts)
🔜  v2.0  — System tray icon — minimize to tray, alarms keep running
🔜  v2.0  — Countdown timer mode
```

---

## 🤝 Contributing

Contributions make open-source amazing — all PRs are welcome! 🙌

```bash
# 1. Fork the project on GitHub

# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/advanced-alarm-clock.git

# 3. Create a feature branch
git checkout -b feature/SnoozeButton

# 4. Make your changes and commit
git commit -m "Add snooze button with 5-min delay"

# 5. Push to your fork
git push origin feature/SnoozeButton

# 6. Open a Pull Request on GitHub
```

### Contribution Guidelines
- Keep code clean and well-commented
- Test on Windows before submitting
- One feature or fix per PR
- Update the README if your change affects usage

---

## ⚠️ Notes

- The app uses a **local image path** by default (`C:\Users\shiva\AlarmItems\...`) — update line 28 in `alarm_clock.py` to your own path, or place `clock.png` in the same folder and it will use that automatically.
- Audio playback requires `pygame` and a working audio output device.
- The alarm checker runs in a **background thread** and stops automatically when the app is closed.

---

## ⭐ Support

If this project was useful or fun, please drop a star — it genuinely helps! 🙏

<div align="center">

[![Star this repo](https://img.shields.io/badge/⭐%20Star%20this%20repo-It%20means%20a%20lot!-gold?style=for-the-badge)](https://github.com/Shivam-Singh-Hash/advanced-alarm-clock)

</div>

---

## 👨‍💻 Author

<div align="center">

### **Shivam Singh**

*Building cool things, one commit at a time.*

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Shivam-Singh-Hash)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/contactshivamsingh/)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/theshivamsinghrathore/)

</div>

---

## 📄 License

```
MIT License  —  Copyright (c) 2025 Shivam Singh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.
```

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,9,24&height=120&section=footer" width="100%"/>

**Made with ❤️ by [Shivam Singh](https://github.com/Shivam-Singh-Hash)**

</div>
