#!/usr/bin/env python3
import queue
import shutil
import subprocess
import threading
import tkinter as tk
from tkinter import scrolledtext

# name -> (availability check, install command). {p} is replaced by the package.
MANAGERS = {
    "apt": (["apt-cache", "show", "{p}"],
            ["pkexec", "apt-get", "install", "-y", "{p}"]),
    "dnf": (["dnf", "-q", "info", "{p}"],
            ["pkexec", "dnf", "install", "-y", "{p}"]),
    "pacman": (["pacman", "-Si", "{p}"],
               ["pkexec", "pacman", "-S", "--noconfirm", "{p}"]),
    "zypper": (["zypper", "--non-interactive", "se", "-x", "{p}"],
               ["pkexec", "zypper", "--non-interactive", "install", "{p}"]),
}

msgs = queue.Queue()


def log(text):
    msgs.put(text)


def fill(cmd, pkg):
    return [pkg if part == "{p}" else part for part in cmd]


def run(cmd, stream=False):
    """Run a command (no shell). Returns (returncode, output)."""
    try:
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, text=True)
    except FileNotFoundError:
        return 127, ""
    out = []
    for line in proc.stdout:
        out.append(line)
        if stream:
            log(line.rstrip())
    proc.wait()
    return proc.returncode, "".join(out)


def detect_manager():
    for name in MANAGERS:
        if shutil.which(name):
            return name
    return None


def flatpak_find(pkg):
    """Return the Flatpak app ID of the best match, or None."""
    rc, out = run(["flatpak", "search", "--columns=application", pkg])
    if rc != 0:
        return None
    ids = [l.strip() for l in out.splitlines() if "." in l.strip()]
    if not ids:
        return None
    # Prefer an ID whose last segment matches the name exactly
    for app_id in ids:
        if app_id.split(".")[-1].lower() == pkg.lower():
            return app_id
    return ids[0]


def install_worker(pkg):
    try:
        mgr = detect_manager()
        if mgr:
            check, install = MANAGERS[mgr]
            log(f"Searching {mgr} for '{pkg}'...")
            rc, _ = run(fill(check, pkg))
            if rc == 0:
                log(f"Found in {mgr}. Installing...")
                rc, _ = run(fill(install, pkg), stream=True)
                log("Done." if rc == 0 else f"{mgr} install failed (code {rc}).")
                return
            log(f"Not found in {mgr}.")
        else:
            log("No supported package manager found.")

        if not shutil.which("flatpak"):
            log("Flatpak isn't installed, so there's nowhere else to look.")
            return

        log("Searching Flatpak...")
        app_id = flatpak_find(pkg)
        if not app_id:
            log(f"'{pkg}' not found in Flatpak either.")
            return
        log(f"Found {app_id}. Installing...")
        rc, _ = run(["flatpak", "install", "-y", "--user", "flathub", app_id],
                    stream=True)
        log("Done." if rc == 0 else f"Flatpak install failed (code {rc}).")
    finally:
        msgs.put(None)  # signals "finished"


def submit(event=None):
    pkg = entry.get().strip()
    if not pkg:
        return
    button.config(state="disabled")
    entry.config(state="disabled")
    output.config(state="normal")
    output.delete("1.0", "end")
    output.config(state="disabled")
    threading.Thread(target=install_worker, args=(pkg,), daemon=True).start()
    root.after(100, poll)


def poll():
    finished = False
    try:
        while True:
            m = msgs.get_nowait()
            if m is None:
                finished = True
                break
            output.config(state="normal")
            output.insert("end", m + "\n")
            output.see("end")
            output.config(state="disabled")
    except queue.Empty:
        pass
    if finished:
        button.config(state="normal")
        entry.config(state="normal")
        entry.focus()
    else:
        root.after(100, poll)


root = tk.Tk()
root.title("Package Finder")

tk.Label(root, text="Package name:").pack(padx=10, pady=(10, 0))
entry = tk.Entry(root, width=40)
entry.pack(padx=10, pady=5)
entry.focus()
entry.bind("<Return>", submit)

button = tk.Button(root, text="Install", command=submit)
button.pack(pady=(0, 5))

output = scrolledtext.ScrolledText(root, width=60, height=12, state="disabled")
output.pack(padx=10, pady=(0, 10))

root.mainloop()
