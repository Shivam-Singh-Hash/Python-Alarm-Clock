"""
╔══════════════════════════════════════════╗
║   N E X U S   A L A R M   C L O C K     ║
║   Cyberpunk · Neon · Holographic         ║
╚══════════════════════════════════════════╝

Run:    python alarm_clock.py
Needs:  pip install pygame        (for loud internet alarm sound)
        tkinter is built-in
"""

import tkinter as tk
from tkinter import messagebox
import datetime, math, threading, time, random, os, urllib.request, tempfile

# ── pygame for loud audio (optional) ────────────────────────────────────
try:
    import pygame
    PYGAME_OK = True
except ImportError:
    PYGAME_OK = False

# ── alarm sound URLs (loud, free) ────────────────────────────────────────
ALARM_URLS = [
    "https://www.soundjay.com/misc/sounds/bell-ringing-05.mp3",
    "https://actions.google.com/sounds/v1/alarms/alarm_clock.ogg",
    "https://cdn.pixabay.com/download/audio/2022/03/24/audio_805cb4d5b4.mp3",
    "https://www.sounddogs.com/previews/11/mp3/1113_1594662792.mp3",
]

_audio_path: str | None = None   # cached download

def _download_alarm() -> str | None:
    global _audio_path
    if _audio_path and os.path.exists(_audio_path):
        return _audio_path
    for url in ALARM_URLS:
        try:
            suffix = ".mp3" if ".mp3" in url else ".ogg"
            tmp = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
            urllib.request.urlretrieve(url, tmp.name)
            if os.path.getsize(tmp.name) > 5000:   # sanity check
                _audio_path = tmp.name
                return _audio_path
        except Exception:
            continue
    return None

def play_alarm_sound():
    if PYGAME_OK:
        try:
            path = _download_alarm()
            if path:
                pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
                pygame.mixer.music.load(path)
                pygame.mixer.music.set_volume(1.0)
                pygame.mixer.music.play(loops=5)
                return
        except Exception:
            pass
    # fallback
    import platform
    for _ in range(8):
        if platform.system() == "Windows":
            import winsound
            winsound.Beep(1047, 250); winsound.Beep(784, 120); winsound.Beep(1047, 250)
        elif platform.system() == "Darwin":
            os.system("afplay /System/Library/Sounds/Sosumi.aiff 2>/dev/null")
        else:
            os.system("paplay /usr/share/sounds/freedesktop/stereo/alarm-clock-elapsed.oga "
                      "2>/dev/null || echo -e '\a'")
        time.sleep(0.08)

def stop_alarm_sound():
    if PYGAME_OK:
        try: pygame.mixer.music.stop()
        except Exception: pass


# ════════════════════════════════════════════════════════════════════════
class NexusAlarm:

    # ── colour palette ───────────────────────────────────────────────────
    BG      = "#03040E"
    PANEL   = "#070B1A"
    CARD    = "#0B1022"
    BORDER  = "#172040"
    CYAN    = "#00F5FF"
    CYAND   = "#006878"
    MAG     = "#FF00CC"
    MAGD    = "#700060"
    YELLOW  = "#FFE030"
    GREEN   = "#00FF88"
    RED     = "#FF2244"
    TEXT    = "#C8E0FF"
    MUTED   = "#2E3C58"
    WHITE   = "#FFFFFF"

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("NEXUS ALARM")
        self.root.geometry("560x880")
        self.root.minsize(520, 820)
        self.root.configure(bg=self.BG)
        self.root.resizable(True, True)

        self.alarms: list[dict] = []
        self.alarm_triggered = False
        self._particles: list[dict] = []
        self._pulse = 0          # for glow pulsing

        self._init_particles()
        threading.Thread(target=_download_alarm, daemon=True).start()

        self._build_ui()
        self._tick()
        self._animate()

    # ── particles ────────────────────────────────────────────────────────
    def _init_particles(self):
        self._particles = []
        for _ in range(60):
            self._particles.append({
                "x":  random.uniform(0, 560),
                "y":  random.uniform(0, 290),
                "vx": random.uniform(-0.35, 0.35),
                "vy": random.uniform(-0.7, -0.15),
                "r":  random.uniform(1, 2.8),
                "c":  random.choice(["C","C","C","M"]),
            })

    def _animate(self):
        c = self.canvas
        c.delete("pt")
        self._pulse = (self._pulse + 3) % 360
        for p in self._particles:
            p["x"] += p["vx"]; p["y"] += p["vy"]
            if p["y"] < -4:
                p["y"] = 292; p["x"] = random.uniform(0, 560)
            if p["x"] < 0: p["x"] = 560
            if p["x"] > 560: p["x"] = 0
            col = self.CYAN if p["c"] == "C" else self.MAG
            r = p["r"]
            c.create_oval(p["x"]-r, p["y"]-r, p["x"]+r, p["y"]+r,
                           fill=col, outline="", tags="pt")
        self.root.after(38, self._animate)

    # ── UI construction ───────────────────────────────────────────────────
    def _build_ui(self):
        # ── top bar ─────────────────────────────
        top = tk.Frame(self.root, bg=self.BG)
        top.pack(fill="x", padx=24, pady=(16, 0))
        tk.Label(top, text="N E X U S", font=("Courier New", 10, "bold"),
                 fg=self.CYAN, bg=self.BG).pack(side="left")
        tk.Label(top, text="ALARM SYSTEM v2.0",
                 font=("Courier New", 8), fg=self.MUTED, bg=self.BG).pack(
            side="left", padx=10, pady=(1, 0))
        self.status_dot = tk.Label(top, text="◉ ONLINE",
                                    font=("Courier New", 8, "bold"),
                                    fg=self.GREEN, bg=self.BG)
        self.status_dot.pack(side="right")

        # ── canvas: particles + analog clock ────
        self.canvas = tk.Canvas(self.root, width=560, height=290,
                                bg=self.BG, highlightthickness=0)
        self.canvas.pack(fill="x")

        # ── neon triple-divider ──────────────────
        self._triple_divider()

        # ── digital time ────────────────────────
        digi = tk.Frame(self.root, bg=self.BG)
        digi.pack(fill="x")

        self.time_lbl = tk.Label(digi, text="00:00:00",
                                  font=("Courier New", 54, "bold"),
                                  fg=self.CYAN, bg=self.BG)
        self.time_lbl.pack()

        row = tk.Frame(digi, bg=self.BG)
        row.pack()
        self.ampm_lbl = tk.Label(row, text="AM",
                                  font=("Courier New", 13, "bold"),
                                  fg=self.MAG, bg=self.BG)
        self.ampm_lbl.pack(side="left", padx=(0, 20))
        self.date_lbl = tk.Label(row, text="",
                                  font=("Courier New", 10),
                                  fg=self.MUTED, bg=self.BG)
        self.date_lbl.pack(side="left")

        self._triple_divider()

        # ── SET ALARM section ────────────────────
        tk.Label(self.root, text="⌖  SCHEDULE ALARM",
                 font=("Courier New", 9, "bold"),
                 fg=self.CYAN, bg=self.BG).pack(
            anchor="w", padx=26, pady=(10, 0))

        card = tk.Frame(self.root, bg=self.CARD,
                         highlightbackground=self.BORDER, highlightthickness=1)
        card.pack(fill="x", padx=20, pady=(6, 0))
        card_in = tk.Frame(card, bg=self.CARD)
        card_in.pack(padx=18, pady=14, fill="x")

        # spinner row
        sp_row = tk.Frame(card_in, bg=self.CARD)
        sp_row.pack(fill="x")

        tk.Label(sp_row, text="HH", font=("Courier New", 7, "bold"),
                  fg=self.MUTED, bg=self.CARD).grid(row=0, column=0, sticky="w")
        self.h_spin = self._spin(sp_row, 0, 23)
        self.h_spin.grid(row=1, column=0)

        tk.Label(sp_row, text=":", font=("Courier New", 38, "bold"),
                  fg=self.CYAN, bg=self.CARD).grid(row=1, column=1, padx=10)

        tk.Label(sp_row, text="MM", font=("Courier New", 7, "bold"),
                  fg=self.MUTED, bg=self.CARD).grid(row=0, column=2, sticky="w")
        self.m_spin = self._spin(sp_row, 0, 59)
        self.m_spin.grid(row=1, column=2)

        # label
        tk.Label(card_in, text="LABEL  (optional)",
                  font=("Courier New", 7, "bold"),
                  fg=self.MUTED, bg=self.CARD).pack(anchor="w", pady=(12, 2))
        self.lbl_var = tk.StringVar()
        ent = tk.Entry(card_in, textvariable=self.lbl_var,
                        font=("Courier New", 12),
                        bg="#060810", fg=self.CYAN,
                        insertbackground=self.CYAN,
                        relief="flat",
                        highlightthickness=1,
                        highlightbackground=self.BORDER,
                        highlightcolor=self.CYAN)
        ent.pack(fill="x", ipady=7)

        # add button
        self.add_btn = tk.Button(card_in, text="◈   ACTIVATE ALARM",
                                  font=("Courier New", 11, "bold"),
                                  fg=self.BG, bg=self.CYAN,
                                  activeforeground=self.BG,
                                  activebackground=self.CYAND,
                                  relief="flat", bd=0, cursor="hand2",
                                  command=self._add_alarm)
        self.add_btn.pack(fill="x", pady=(14, 0), ipady=10)
        self.add_btn.bind("<Enter>", lambda e: self.add_btn.config(bg=self.CYAND))
        self.add_btn.bind("<Leave>", lambda e: self.add_btn.config(bg=self.CYAN))

        # ── ALARMS list header ───────────────────
        hdr = tk.Frame(self.root, bg=self.BG)
        hdr.pack(fill="x", padx=26, pady=(16, 4))
        tk.Label(hdr, text="◈  ACTIVE ALARMS",
                  font=("Courier New", 9, "bold"),
                  fg=self.CYAN, bg=self.BG).pack(side="left")
        self.count_lbl = tk.Label(hdr, text="",
                                   font=("Courier New", 9),
                                   fg=self.MUTED, bg=self.BG)
        self.count_lbl.pack(side="right")

        # scrollable area
        outer = tk.Frame(self.root, bg=self.BG)
        outer.pack(fill="both", expand=True, padx=20, pady=(0, 16))
        lc = tk.Canvas(outer, bg=self.BG, highlightthickness=0)
        sb = tk.Scrollbar(outer, orient="vertical", command=lc.yview)
        lc.configure(yscrollcommand=sb.set)
        sb.pack(side="right", fill="y")
        lc.pack(side="left", fill="both", expand=True)
        self.alarm_frame = tk.Frame(lc, bg=self.BG)
        lc.create_window((0, 0), window=self.alarm_frame, anchor="nw")
        self.alarm_frame.bind("<Configure>",
            lambda e: lc.configure(scrollregion=lc.bbox("all")))

        self._render_alarms()

    # ── widget helpers ────────────────────────────────────────────────────
    def _triple_divider(self):
        f = tk.Frame(self.root, bg=self.BG)
        f.pack(fill="x", padx=20, pady=(6, 0))
        tk.Frame(f, height=1, bg=self.CYAND).pack(fill="x")
        tk.Frame(f, height=2, bg=self.BG).pack(fill="x")
        tk.Frame(f, height=1, bg=self.MAGD).pack(fill="x")

    def _spin(self, parent, lo, hi):
        return tk.Spinbox(parent, from_=lo, to=hi, width=4, format="%02.0f",
                           font=("Courier New", 34, "bold"),
                           fg=self.CYAN, bg=self.CARD,
                           buttonbackground=self.CARD,
                           relief="flat",
                           highlightthickness=1,
                           highlightbackground=self.BORDER,
                           highlightcolor=self.CYAN,
                           insertbackground=self.CYAN,
                           wrap=True)

    # ── alarm list rendering ──────────────────────────────────────────────
    def _render_alarms(self):
        for w in self.alarm_frame.winfo_children():
            w.destroy()
        n = len(self.alarms)
        self.count_lbl.config(text=f"{n} scheduled")
        if n == 0:
            tk.Label(self.alarm_frame, text="— no alarms scheduled —",
                      font=("Courier New", 9), fg=self.MUTED,
                      bg=self.BG).pack(pady=12)
            return
        for i, a in enumerate(self.alarms):
            self._alarm_row(i, a)

    def _alarm_row(self, idx, alarm):
        active = alarm["active"]
        border = self.CYAND if active else self.BORDER
        row = tk.Frame(self.alarm_frame, bg=self.CARD,
                        highlightbackground=border, highlightthickness=1)
        row.pack(fill="x", pady=4)
        inner = tk.Frame(row, bg=self.CARD)
        inner.pack(fill="x", padx=14, pady=10)

        # status dot
        tk.Label(inner, text="●",
                  font=("Courier New", 9),
                  fg=self.GREEN if active else self.MUTED,
                  bg=self.CARD).pack(side="left", padx=(0, 10))

        # time + label
        left = tk.Frame(inner, bg=self.CARD)
        left.pack(side="left")
        tc = self.CYAN if active else self.MUTED
        tk.Label(left, text=f"{alarm['hour']:02d}:{alarm['minute']:02d}",
                  font=("Courier New", 26, "bold"),
                  fg=tc, bg=self.CARD).pack(anchor="w")
        lbl = (alarm["label"] or "alarm").upper()
        tk.Label(left, text=lbl, font=("Courier New", 7),
                  fg=self.MUTED, bg=self.CARD).pack(anchor="w")

        # countdown
        if active:
            now  = datetime.datetime.now()
            fire = now.replace(hour=alarm["hour"], minute=alarm["minute"],
                                second=0, microsecond=0)
            if fire <= now:
                fire += datetime.timedelta(days=1)
            d = fire - now
            hh = int(d.total_seconds() // 3600)
            mm = int((d.total_seconds() % 3600) // 60)
            cd = f"in {hh}h {mm}m" if hh else f"in {mm}m"
            tk.Label(inner, text=cd, font=("Courier New", 8),
                      fg=self.YELLOW, bg=self.CARD).pack(side="left", padx=(14, 0))

        # controls
        ctrl = tk.Frame(inner, bg=self.CARD)
        ctrl.pack(side="right")

        tcol = self.GREEN if active else self.MUTED
        tk.Button(ctrl, text="ON" if active else "OFF",
                   font=("Courier New", 8, "bold"),
                   fg=self.BG, bg=tcol,
                   relief="flat", bd=0, cursor="hand2", width=4,
                   command=lambda i=idx: self._toggle(i)).pack(
            side="left", padx=(0, 8), ipady=4)

        tk.Button(ctrl, text="✕",
                   font=("Courier New", 11),
                   fg=self.RED, bg=self.CARD,
                   activeforeground=self.BG,
                   activebackground=self.RED,
                   relief="flat", bd=0, cursor="hand2",
                   command=lambda i=idx: self._delete(i)).pack(
            side="left", ipady=3, ipadx=5)

    # ── alarm CRUD ────────────────────────────────────────────────────────
    def _add_alarm(self):
        try:
            h = int(self.h_spin.get())
            m = int(self.m_spin.get())
        except ValueError:
            messagebox.showerror("Input Error", "Invalid hour/minute.")
            return
        self.alarms.append({"hour": h, "minute": m,
                             "label": self.lbl_var.get().strip(),
                             "active": True})
        self.lbl_var.set("")
        self._render_alarms()

    def _toggle(self, idx):
        self.alarms[idx]["active"] = not self.alarms[idx]["active"]
        self._render_alarms()

    def _delete(self, idx):
        self.alarms.pop(idx)
        self._render_alarms()

    # ── clock tick ────────────────────────────────────────────────────────
    def _tick(self):
        now = datetime.datetime.now()
        h, m, s = now.hour, now.minute, now.second
        h12  = h % 12 or 12
        ampm = "AM" if h < 12 else "PM"
        self.time_lbl.config(text=f"{h12:02d}:{m:02d}:{s:02d}")
        self.ampm_lbl.config(text=ampm)
        self.date_lbl.config(text=now.strftime("%A,  %d %B %Y"))
        self._draw_clock(h, m, s)
        if s == 0:
            self._check_alarms(h, m)
        self.root.after(1000, self._tick)

    # ── analog clock drawing ──────────────────────────────────────────────
    def _draw_clock(self, h, m, s):
        c = self.canvas
        cx, cy, r = 280, 145, 112
        c.delete("clock")

        # outer atmosphere layers
        for rad, col in [(r+28,"#04060F"),(r+20,"#06091A"),
                          (r+12,"#090E22"),(r+5, "#0D132C")]:
            c.create_oval(cx-rad,cy-rad,cx+rad,cy+rad,
                           fill=col,outline="",tags="clock")

        # clock face
        c.create_oval(cx-r,cy-r,cx+r,cy+r,
                       fill="#060C1E",outline=self.CYAND,width=1,tags="clock")

        # second sweep arc (outer)
        ext_s = s * 6
        c.create_arc(cx-r-5,cy-r-5,cx+r+5,cy+r+5,
                      start=90,extent=-ext_s,
                      style="arc",outline=self.CYAN,width=3,tags="clock")
        # minute arc (inner ring)
        ext_m = (m + s/60) * 6
        c.create_arc(cx-(r-9),cy-(r-9),cx+(r-9),cy+(r-9),
                      start=90,extent=-ext_m,
                      style="arc",outline=self.MAG,width=2,tags="clock")

        # tick marks + hour numbers
        for i in range(60):
            ang = math.radians(i*6 - 90)
            if i % 5 == 0:
                r1, r2, w, col = r-18, r-2, 2, self.MUTED
                n = i//5 or 12
                nx = cx + (r-32)*math.cos(ang)
                ny = cy + (r-32)*math.sin(ang)
                c.create_text(nx, ny, text=str(n),
                               font=("Courier New", 7, "bold"),
                               fill=self.MUTED, tags="clock")
            else:
                r1, r2, w, col = r-9, r-2, 1, "#131C30"
            c.create_line(cx+r1*math.cos(ang),cy+r1*math.sin(ang),
                           cx+r2*math.cos(ang),cy+r2*math.sin(ang),
                           fill=col, width=w, tags="clock")

        # alarm position markers
        for alarm in self.alarms:
            if not alarm["active"]: continue
            ah  = alarm["hour"] % 12 + alarm["minute"]/60
            ang = math.radians(ah*30 - 90)
            ax  = cx + (r-7)*math.cos(ang)
            ay  = cy + (r-7)*math.sin(ang)
            c.create_oval(ax-5,ay-5,ax+5,ay+5,
                           fill=self.MAG,outline="",tags="clock")
            c.create_oval(ax-2,ay-2,ax+2,ay+2,
                           fill=self.BG,outline="",tags="clock")

        # hour hand
        ha = math.radians((h%12 + m/60)*30 - 90)
        self._draw_hand(c, cx, cy, ha, r-44, 4, self.TEXT)
        # minute hand
        ma = math.radians((m + s/60)*6 - 90)
        self._draw_hand(c, cx, cy, ma, r-24, 2, self.TEXT)
        # second hand
        sa = math.radians(s*6 - 90)
        c.create_line(cx,cy,
                       cx+(r-16)*math.cos(sa),
                       cy+(r-16)*math.sin(sa),
                       fill=self.CYAN,width=1,tags="clock")
        c.create_line(cx,cy,
                       cx-20*math.cos(sa),
                       cy-20*math.sin(sa),
                       fill=self.CYAND,width=1,tags="clock")

        # centre jewel
        c.create_oval(cx-8,cy-8,cx+8,cy+8,
                       fill=self.MAG,outline="",tags="clock")
        c.create_oval(cx-4,cy-4,cx+4,cy+4,
                       fill=self.CYAN,outline="",tags="clock")
        c.create_oval(cx-2,cy-2,cx+2,cy+2,
                       fill=self.BG,outline="",tags="clock")

    def _draw_hand(self, c, cx, cy, angle, length, width, color):
        ex = cx + length*math.cos(angle)
        ey = cy + length*math.sin(angle)
        c.create_line(cx, cy, ex, ey, fill=color,
                       width=width, capstyle="round", tags="clock")

    # ── alarm checker ─────────────────────────────────────────────────────
    def _check_alarms(self, h, m):
        for alarm in self.alarms:
            if alarm["active"] and alarm["hour"]==h and alarm["minute"]==m:
                if not self.alarm_triggered:
                    self.alarm_triggered = True
                    threading.Thread(target=play_alarm_sound, daemon=True).start()
                    self.root.after(0, lambda a=alarm: self._show_popup(a))

    # ── alarm popup ────────────────────────────────────────────────────────
    def _show_popup(self, alarm):
        label = alarm["label"] or "Alarm"
        pop = tk.Toplevel(self.root)
        pop.title("⏰  NEXUS ALARM")
        pop.configure(bg=self.BG)
        pop.geometry("420x280")
        pop.resizable(False, False)
        pop.grab_set()

        # animated neon border
        outer = tk.Frame(pop, bg=self.CYAN, padx=2, pady=2)
        outer.pack(fill="both", expand=True, padx=10, pady=10)
        inner = tk.Frame(outer, bg=self.BG)
        inner.pack(fill="both", expand=True, padx=2, pady=2)

        tk.Label(inner, text="⏰", font=("Segoe UI Emoji", 36),
                  bg=self.BG).pack(pady=(18, 0))
        tk.Label(inner, text="WAKE  UP  //  NEXUS",
                  font=("Courier New", 16, "bold"),
                  fg=self.CYAN, bg=self.BG).pack()
        tk.Label(inner, text=label.upper(),
                  font=("Courier New", 10),
                  fg=self.MAG, bg=self.BG).pack(pady=(4, 18))

        btns = tk.Frame(inner, bg=self.BG)
        btns.pack()

        def dismiss():
            stop_alarm_sound()
            self.alarm_triggered = False
            pop.destroy()

        def snooze():
            stop_alarm_sound()
            self.alarm_triggered = False
            pop.destroy()
            t = datetime.datetime.now() + datetime.timedelta(minutes=5)
            self.alarms.append({
                "hour": t.hour, "minute": t.minute,
                "label": f"↺ Snooze: {label}", "active": True})
            self._render_alarms()

        tk.Button(btns, text="  SNOOZE  5m  ",
                   font=("Courier New", 10, "bold"),
                   fg=self.BG, bg=self.MUTED,
                   activebackground=self.BORDER,
                   relief="flat", bd=0, cursor="hand2",
                   command=snooze).pack(side="left", ipadx=10, ipady=10, padx=(0, 12))

        tk.Button(btns, text="  DISMISS  ",
                   font=("Courier New", 10, "bold"),
                   fg=self.BG, bg=self.CYAN,
                   activebackground=self.CYAND,
                   relief="flat", bd=0, cursor="hand2",
                   command=dismiss).pack(side="left", ipadx=10, ipady=10)

        # pulse border colour
        pulse_cols = [self.CYAN, self.MAG, self.YELLOW, self.GREEN]
        ci = [0]
        def _pulse():
            if not pop.winfo_exists(): return
            outer.configure(bg=pulse_cols[ci[0] % len(pulse_cols)])
            ci[0] += 1
            pop.after(350, _pulse)
        _pulse()


# ════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    if not PYGAME_OK:
        print("─" * 52)
        print("  [NEXUS]  pygame not installed.")
        print("  Install it for loud internet alarm sound:")
        print("           pip install pygame")
        print("  Falling back to system beeps for now.")
        print("─" * 52)

    root = tk.Tk()
    app  = NexusAlarm(root)

    root.update_idletasks()
    w = root.winfo_width(); h = root.winfo_height()
    x = (root.winfo_screenwidth()  - w) // 2
    y = (root.winfo_screenheight() - h) // 2
    root.geometry(f"{w}x{h}+{x}+{y}")

    root.mainloop()
