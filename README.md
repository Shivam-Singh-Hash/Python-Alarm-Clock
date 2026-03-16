<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,9,24&height=200&section=header&text=NEXUS%20Alarm%20Clock&fontSize=52&fontColor=fff&animation=twinkling&fontAlignY=35&desc=Cyberpunk%20%C2%B7%20Neon%20%C2%B7%20Holographic%20%E2%80%94%20A%20stunning%20desktop%20alarm%20built%20with%20Python%20%26%20Tkinter&descAlignY=58&descSize=17" width="100%"/>

<br/>

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-Built--in-FF6F00?style=for-the-badge&logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-Audio-00B140?style=for-the-badge&logo=python&logoColor=white)
![Single File](https://img.shields.io/badge/Single%20File-No%20Config-00C8D4?style=for-the-badge&logo=python&logoColor=white)

![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Mac%20%7C%20Linux-informational?style=for-the-badge&logo=windows&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge&logo=opensourceinitiative&logoColor=white)
![Stars](https://img.shields.io/github/stars/Shivam-Singh-Hash/nexus-alarm-clock?style=for-the-badge&color=gold&logo=github)

<br/>

**🌀 Particle Field · 🕐 Dual-Ring Analog · 🔊 Internet Audio · ⏰ Multi-Alarm Scheduler**

<br/>

[🚀 Quick Start](#-installation) &nbsp;·&nbsp; [✨ Features](#-features) &nbsp;·&nbsp; [🏗️ How It Works](#%EF%B8%8F-how-it-works) &nbsp;·&nbsp; [🗺️ Roadmap](#%EF%B8%8F-roadmap) &nbsp;·&nbsp; [🤝 Contribute](#-contributing)

<br/>

</div>

---

## 📖 Overview

**NEXUS Alarm Clock** is a single-file Python desktop application with a full cyberpunk neon aesthetic. It combines a live animated analog + digital clock, a multi-alarm scheduler with countdown timers, and auto-downloaded loud alarm audio — all in one `.py` file with zero configuration.

> 💡 Built for developers and power users who want a **visually stunning**, fully local alarm system they can run, hack, and extend.

---

## ✨ Features

<div align="center">

| Feature | Description |
|---------|-------------|
| 🌀 **Animated Particle Field** | 60 glowing cyan & magenta particles drift continuously behind the clock |
| 🕐 **Dual-Ring Analog Clock** | Outer cyan arc tracks seconds; inner magenta arc tracks minutes |
| 🔢 **Large Digital Display** | 52pt Courier New readout with AM/PM indicator and full date |
| ⏰ **Unlimited Alarms** | Add, toggle on/off, and delete any number of alarms independently |
| ⏳ **Countdown Timer** | Each alarm row shows "in Xh Ym" until next trigger |
| 🔊 **Internet Alarm Audio** | Auto-downloads a loud MP3/OGG from 4 fallback URLs at startup |
| 😴 **Snooze Support** | 5-minute snooze automatically adds a new alarm |
| 💡 **Pulsing Popup** | Alarm popup border cycles cyan → magenta → yellow → green |
| 🖥️ **Cross-Platform** | Works on Windows, macOS, and Linux |
| 📄 **Zero Config** | One `.py` file — no database, no config file, no setup wizard |

</div>

---

## 📸 Screenshots

<div align="center">

<table>
  <tr>
    <td align="center">
      <img src="https://placehold.co/380x240/03040E/00F5FF?text=🌀+Particle+Clock&font=courier-prime" width="360" alt="Particle Clock View"/>
      <br/><sub><b>Animated Particle Field + Dual-Ring Analog Clock</b></sub>
    </td>
    <td align="center">
      <img src="https://placehold.co/380x240/03040E/FF00CC?text=⏰+Set+Alarm&font=courier-prime" width="360" alt="Set Alarm"/>
      <br/><sub><b>Alarm Scheduler — HH / MM / Label</b></sub>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="https://placehold.co/380x240/03040E/00FF88?text=📋+Active+Alarms&font=courier-prime" width="360" alt="Alarm List"/>
      <br/><sub><b>Active Alarms List with Countdown Timers</b></sub>
    </td>
    <td align="center">
      <img src="https://placehold.co/380x240/03040E/FFE030?text=🔔+Alarm+Firing!&font=courier-prime" width="360" alt="Alarm Popup"/>
      <br/><sub><b>Pulsing Neon Popup + Loud Audio Alert</b></sub>
    </td>
  </tr>
</table>

> 📷 Replace placeholders above with real screenshots from your app!

</div>

---

## 🏗️ How It Works

```
┌────────────────────────────────────────────────────────────┐
│                  TKINTER GUI  (Main Thread)                 │
│                                                            │
│   ┌──────────────────────────────────────────────────┐    │
│   │           CANVAS  (560 × 290 px)                 │    │
│   │                                                  │    │
│   │   🌀 60 Particles  (cyan + magenta, 38ms loop)   │    │
│   │   🕐 Dual-Ring Analog Clock  (redrawn every 1s)  │    │
│   │      · Outer cyan arc   = seconds progress       │    │
│   │      · Inner magenta arc = minutes progress      │    │
│   │      · Magenta dots     = scheduled alarm times  │    │
│   └──────────────────────────────────────────────────┘    │
│                                                            │
│   ┌──────────────────┐   ┌───────────────────────────┐   │
│   │  Digital Clock   │   │     SET ALARM CARD        │   │
│   │  52pt Courier New│   │  HH Spinner / MM Spinner  │   │
│   │  + AM/PM + Date  │   │  Label Entry (optional)   │   │
│   └──────────────────┘   │  ◈ ACTIVATE ALARM button  │   │
│                           └───────────────────────────┘   │
│                                                            │
│   ┌──────────────────────────────────────────────────┐    │
│   │         ACTIVE ALARMS  (scrollable list)         │    │
│   │  ● 07:30  MORNING RUN       in 8h 12m   ON ✕    │    │
│   │  ● 09:00  STAND-UP          in 9h 42m   ON ✕    │    │
│   └──────────────────────────────────────────────────┘    │
└──────────────────────────┬─────────────────────────────────┘
                           │
              (background daemon thread)
                           │
                           ▼
┌────────────────────────────────────────────────────────────┐
│              ALARM CHECKER  (Background Thread)             │
│                                                            │
│   Fires every second at :00 → compares h:m against        │
│   every active alarm in the list                           │
│                                                            │
│              Match found?                                  │
│                   ↓                                        │
│   ┌──────────────────────────────────────────────────┐    │
│   │  Audio Thread   → pygame plays downloaded MP3    │    │
│   │  Main Thread    → pulsing neon popup appears     │    │
│   │  SNOOZE clicked → +5 min alarm added to list     │    │
│   │  DISMISS clicked → sound stops, popup closes     │    │
│   └──────────────────────────────────────────────────┘    │
└────────────────────────────────────────────────────────────┘
                           │
              (startup background thread)
                           ↓
┌────────────────────────────────────────────────────────────┐
│              AUDIO PRE-FETCH  (Background Thread)           │
│                                                            │
│   Tries 4 public URLs in order                             │
│   → downloads first valid MP3 / OGG file                   │
│   → caches in system temp folder for entire session        │
│   → falls back to system beeps if all URLs fail (offline)  │
└────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

<div align="center">

### Core GUI & Clock
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-Built--in-FF6F00?style=for-the-badge&logo=python&logoColor=white)

### Audio Playback
![Pygame](https://img.shields.io/badge/Pygame-Mixer-00B140?style=for-the-badge&logo=python&logoColor=white)

### Asset Download
![urllib](https://img.shields.io/badge/urllib-Built--in-00C8D4?style=for-the-badge&logo=python&logoColor=white)

### Concurrency
![Threading](https://img.shields.io/badge/threading-Built--in-FF00CC?style=for-the-badge&logo=python&logoColor=white)

</div>

---

## 📁 Project Structure

```
📦 nexus-alarm-clock/
│
├── 🐍 alarm_clock.py        ← Entire application — UI + logic (single file)
├── 📄 requirements.txt      ← pip dependencies  (pygame only)
└── 📖 README.md             ← This file
```

> ✅ **No images, no config files, no database** — one Python file is everything.

---

## 🚀 Installation

### Prerequisites

```bash
# Confirm Python 3.10 or higher is installed
python --version
```

---

### Step 1 — Clone the repository

```bash
git clone https://github.com/Shivam-Singh-Hash/nexus-alarm-clock.git
cd nexus-alarm-clock
```

---

### Step 2 — Install dependencies

```bash
pip install pygame
```

Or use the requirements file:

```bash
pip install -r requirements.txt
```

> **Windows** — if `pip` is not recognised:
> ```bash
> python -m pip install pygame
> ```

> **Linux** — tkinter may need a separate install:
> ```bash
> sudo apt install python3-tk
> ```

---

### Step 3 — Run

```bash
python alarm_clock.py
```

> 🎵 On first launch the app **silently downloads** alarm audio in a background thread.
> The full UI is available immediately — the download does **not** block anything.

---

## 💻 Usage

**Step 1** — Launch with `python alarm_clock.py`

**Step 2** — Watch the live particle field + analog clock at the top

**Step 3** — In the **SET ALARM** card:
- Spin **HH** to set the hour (0 – 23, 24-hour format)
- Spin **MM** to set the minute (0 – 59)
- Optionally type a **LABEL** (e.g. `Morning run`, `Stand-up meeting`)

**Step 4** — Click **◈ ACTIVATE ALARM** → it appears in the list with a live countdown

**Step 5** — Manage alarms using the row buttons:

| Button | Action |
|--------|--------|
| **ON / OFF** | Toggle the alarm without deleting it |
| **✕** | Delete the alarm permanently |

**Step 6** — When the alarm fires, a pulsing neon popup appears:

| Button | Action |
|--------|--------|
| **SNOOZE 5m** | Stop sound + add a new alarm 5 minutes from now |
| **DISMISS** | Stop sound and close the popup |

---

## 🔊 Audio System

On startup a background thread tries these URLs in order, using the first that succeeds:

| Priority | Source | Format |
|----------|--------|--------|
| 1 — Primary | soundjay.com / bell-ringing-05 | MP3 |
| 2 — Fallback | actions.google.com / alarm_clock | OGG |
| 3 — Fallback | cdn.pixabay.com / audio | MP3 |
| 4 — Fallback | sounddogs.com / preview | MP3 |

If **all URLs fail** (offline mode), the app silently falls back to system beep tones — no error shown.

---

## 🎨 Customisation

All colours are constants at the top of the `NexusAlarm` class:

```python
CYAN   = "#00F5FF"   # primary accent — clock arc, digits, buttons
MAG    = "#FF00CC"   # secondary accent — minute arc, alarm markers
YELLOW = "#FFE030"   # countdown text colour
GREEN  = "#00FF88"   # ON indicator dot
RED    = "#FF2244"   # delete button colour
BG     = "#03040E"   # main window background
```

**Change snooze duration** — find `snooze()` inside `_show_popup()`:

```python
t = datetime.datetime.now() + datetime.timedelta(minutes=10)  # 10-min snooze
```

**Add custom alarm audio URLs** — edit near the top of the file:

```python
ALARM_URLS = [
    "https://example.com/your-loud-alarm.mp3",
    ...
]
```

---

## 🗺️ Roadmap

```
✅  v2.0  — Animated particle field (60 particles, 38 ms loop)
✅  v2.0  — Dual-ring analog clock (cyan seconds + magenta minutes)
✅  v2.0  — 52pt digital clock with AM/PM and full date
✅  v2.0  — Unlimited multi-alarm scheduler
✅  v2.0  — Per-alarm ON/OFF toggle and delete
✅  v2.0  — Countdown timer on each alarm row
✅  v2.0  — Auto-download loud alarm audio (4 fallback URLs)
✅  v2.0  — Pygame audio at full volume (5 loops)
✅  v2.0  — 5-minute snooze
✅  v2.0  — Pulsing neon popup (4-colour border cycle)
✅  v2.0  — Offline fallback to system beeps
```

```
🔜  v2.1  — Alarm label shown inside popup
🔜  v2.1  — Volume control slider
🔜  v2.2  — Custom ringtone — browse & load your own MP3
🔜  v2.2  — Repeat / recurring alarms (daily, weekday, custom)
🔜  v2.3  — Save alarms to JSON (persist across restarts)
🔜  v2.3  — System tray icon — minimize to tray, alarms keep running
🔜  v3.0  — Countdown timer mode
🔜  v3.0  — Light / Dark theme toggle
🔜  v3.0  — Alarm import / export
```

---

## 🤝 Contributing

All contributions are welcome — PRs are reviewed! 🙌

```bash
# 1. Fork the project on GitHub

# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/nexus-alarm-clock.git

# 3. Create a feature branch
git checkout -b feature/RepeatAlarms

# 4. Commit your changes
git commit -m "Add daily repeat scheduling"

# 5. Push to your fork
git push origin feature/RepeatAlarms

# 6. Open a Pull Request on GitHub
```

### Guidelines
- Keep code clean and well-commented
- Test on Windows before submitting
- One feature or fix per PR
- Update this README if your change affects usage

---

## ⚠️ Notes

- Alarms fire at exactly **:00 seconds** of the set hour and minute. If you set an alarm for a time already passed in the current minute, it fires at that time the **next day**.
- Audio playback requires `pygame` and a working audio output device.
- The alarm checker runs in a **background daemon thread** and stops automatically when the app closes.
- Downloaded audio is stored in your OS **temp folder** and reused for the whole session.

---

## ⭐ Support

If NEXUS helped you wake up on time, drop a star — it genuinely helps! 🙏

<div align="center">

[![Star this repo](https://img.shields.io/badge/⭐%20Star%20this%20repo-It%20means%20a%20lot!-gold?style=for-the-badge)](https://github.com/Shivam-Singh-Hash/nexus-alarm-clock)

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
