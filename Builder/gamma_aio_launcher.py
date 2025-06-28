import os
import subprocess
import json
import sys
import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk
import tkinter.simpledialog

CONFIG_FILE = "GAMMA_AIO.cfg"


def main():
    cfg = get_cfg_file()
    run_gui(cfg)


def get_cfg_file():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            cfg = json.load(f)
        return cfg
    else:
        cfg = {}
        root = tk.Tk()
        root.withdraw()  # Hide main window
        messagebox.showinfo(
            "Config Missing",
            "Config file not found. Please enter the paths to the executables.",
        )
        cfg["gamma_mo2"] = filedialog.askopenfilename(
            title="Select GAMMA MO2 exe", filetypes=[("Executable files", "*.exe")]
        )
        cfg["talker"] = filedialog.askopenfilename(
            title="Select Talker exe (optional)",
            filetypes=[("Executable files", "*.exe")],
        )
        cfg["voicepet"] = filedialog.askopenfilename(
            title="Select VoicePet exe (optional)",
            filetypes=[("Executable files", "*.exe")],
        )
        cfg["crcr"] = filedialog.askopenfilename(
            title="Select PySAIC exe (optional)",
            filetypes=[("Executable files", "*.exe")],
        )
        with open(CONFIG_FILE, "w") as f:
            json.dump(cfg, f, indent=4)
        root.destroy()
        return cfg


def launch_exe(path, new_console=False, set_cwd=False):
    if not path or not path.strip():
        return
    kwargs = {}
    if new_console:
        kwargs["creationflags"] = subprocess.CREATE_NEW_CONSOLE
    if set_cwd:
        kwargs["cwd"] = os.path.dirname(path)
    try:
        subprocess.Popen(path, **kwargs)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to launch {path}: {e}")


def run_gui(cfg):
    root = tk.Tk()
    root.title("GAMMA AIO Launcher")  # Updated project title
    root.geometry("600x520")
    root.resizable(True, True)
    style = ttk.Style(root)
    style.theme_use("clam")
    root.configure(bg="#23272e")  # Set window background

    # Updated color scheme
    style.configure("TFrame", background="#23272e")
    style.configure("TLabel", background="#23272e", foreground="#e0e0e0")
    style.configure(
        "Title.TLabel",
        background="#23272e",
        foreground="#4CAF50",
        font=("Segoe UI", 14, "bold"),
    )
    style.configure(
        "TButton",
        background="#2c313c",
        foreground="#e0e0e0",
        font=("Segoe UI", 10),
        padding=6,
    )
    style.map(
        "TButton",
        background=[("active", "#4CAF50")],
        foreground=[("active", "#23272e")],
    )
    style.configure(
        "LaunchAll.TButton",
        font=("Segoe UI", 13, "bold"),
        background="#4CAF50",
        foreground="#23272e",
        padding=10,
    )
    style.map(
        "LaunchAll.TButton",
        background=[("active", "#388e3c")],
        foreground=[("active", "#ffffff")],
    )

    main_frame = ttk.Frame(root, padding=20)
    main_frame.pack(fill="both", expand=True)
    main_frame.columnconfigure(0, weight=1)
    main_frame.columnconfigure(1, weight=1)
    main_frame.rowconfigure(2, weight=1)

    left_frame = ttk.Frame(main_frame)
    left_frame.grid(row=2, column=0, rowspan=8, sticky="nswe", padx=(0, 20))
    left_frame.columnconfigure(1, weight=1)

    right_frame = ttk.Frame(main_frame)
    right_frame.grid(row=2, column=1, rowspan=8, sticky="nswe")
    right_frame.columnconfigure(0, weight=1)

    # Labels and browse buttons in left_frame
    labels = {}

    def update_cfg_and_save(key):
        file_path = filedialog.askopenfilename(
            title=f"Select {key} exe", filetypes=[("Executable files", "*.exe")]
        )
        if file_path:
            cfg[key] = file_path
            with open(CONFIG_FILE, "w") as f:
                json.dump(cfg, f, indent=4)
            labels[key].config(text=file_path)

    def launch_all():
        launch_exe(cfg.get("gamma_mo2"))
        launch_exe(cfg.get("talker"), new_console=True)
        launch_exe(cfg.get("voicepet"), new_console=True, set_cwd=True)
        launch_exe(cfg.get("crcr"), new_console=True, set_cwd=True)

    def clear_cfg():
        if messagebox.askyesno(
            "Clear Config",
            "Are you sure you want to clear all exe paths? This will remove all saved paths.",
        ):
            for key in labels:
                cfg[key] = ""
                labels[key].config(text="")
            with open(CONFIG_FILE, "w") as f:
                json.dump(cfg, f, indent=4)

    for i, (key, label_text) in enumerate(
        [
            ("gamma_mo2", "GAMMA MO2"),
            ("talker", "Talker"),
            ("voicepet", "VoicePet"),
            ("crcr", "CRCR / PySAIC"),
        ]
    ):
        ttk.Label(left_frame, text=label_text + ":").grid(
            row=i, column=0, sticky="e", padx=(0, 8), pady=6
        )
        labels[key] = ttk.Label(
            left_frame,
            text=cfg.get(key, ""),
            wraplength=180,
            anchor="w",
            justify="left",
        )
        labels[key].grid(row=i, column=1, sticky="w", pady=6)
        ttk.Button(
            left_frame,
            text="Browse",
            command=lambda k=key: update_cfg_and_save(k),
        ).grid(row=i, column=2, padx=(8, 0), pady=6)

    # Individual launch buttons in right_frame
    ttk.Label(right_frame, text="Quick Launch", style="Title.TLabel").grid(
        row=0, column=0, pady=(0, 12), sticky="n"
    )
    ttk.Button(
        right_frame,
        text="Launch GAMMA MO2",
        width=20,
        command=lambda: launch_exe(cfg.get("gamma_mo2")),
    ).grid(row=1, column=0, pady=6, sticky="ew")
    ttk.Button(
        right_frame,
        text="Launch Talker",
        width=20,
        command=lambda: launch_exe(cfg.get("talker"), new_console=True),
    ).grid(row=2, column=0, pady=6, sticky="ew")
    ttk.Button(
        right_frame,
        text="Launch VoicePet",
        width=20,
        command=lambda: launch_exe(cfg.get("voicepet"), new_console=True, set_cwd=True),
    ).grid(row=3, column=0, pady=6, sticky="ew")
    ttk.Button(
        right_frame,
        text="Launch CRCR / PySAIC",
        width=20,
        command=lambda: launch_exe(cfg.get("crcr"), new_console=True, set_cwd=True),
    ).grid(row=4, column=0, pady=6, sticky="ew")

    ttk.Separator(right_frame, orient="horizontal").grid(
        row=5, column=0, sticky="ew", pady=(12, 6)
    )
    ttk.Button(
        right_frame,
        text="LAUNCH ALL",
        style="LaunchAll.TButton",
        width=20,
        command=launch_all,
    ).grid(row=6, column=0, pady=10, sticky="ew")

    # Bottom buttons
    ttk.Separator(main_frame, orient="horizontal").grid(
        row=10, column=0, columnspan=2, sticky="ew", pady=(16, 10)
    )
    ttk.Button(main_frame, text="Close Launcher", command=root.destroy).grid(
        row=11, column=0, pady=10, sticky="ew"
    )
    ttk.Button(main_frame, text="Clear Config", command=clear_cfg).grid(
        row=11, column=1, pady=10, sticky="ew"
    )

    root.mainloop()


if __name__ == "__main__":
    main()
    sys.exit(0)
