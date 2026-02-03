# USED AI TO MAKE THIS... I WANTED TO TRY OUT TKINTER, SO I MADE THIS....

import sys, os
import tkinter as tk
from tkinter import messagebox as msg
from threading import Thread

import subprocess

# colors for that 'matrix' vibe
BG_COLOR = "#0f0f0f"      # almost black
TXT_COLOR = "#00ff41"     # hacker green
ACCENT = "#008F11"        # darker green
ERR_COLOR = "#ff0000"     # red

# checking nmap path 
nmap_path = "nmap"

def run_scan():
    # clear previous output
    out_box.delete(1.0, tk.END)
    out_box.insert(tk.END, "[*] Initializing Kamui...\n")
    
    t = target_entry.get()
    if not t:
        out_box.insert(tk.END, "[!] Error: No target specified.\n")
        return

    # building the command string manually
    cmd = [nmap_path]
    
    # 1. scan mode logic
    mode = mode_var.get()
    if mode == 1:   # stealth
        cmd.extend(["-sS", "-T4"])
    elif mode == 2: # connect
        cmd.extend(["-sT", "-T4"])
    elif mode == 3: # ghost
        out_box.insert(tk.END, "[*] Ghost Protocol Active...\n")
        # specific evasion flags
        cmd.extend(["-sS", "-T1", "-f", "-n", "-Pn"])
        # check decoy
        d = decoy_entry.get()
        if len(d) > 5:
            cmd.extend(["-D", d])
    elif mode == 4: # loud
        cmd.extend(["-A", "-T4"])
        
    # 2. ports logic
    p = port_var.get()
    if p == 2: cmd.append("-p-")
    elif p == 3: cmd.append("-F")
    
    # target last
    cmd.append(t)
    
    # save file logic
    if save_var.get() == 1:
        fname = "scan_results" 
        cmd.extend(["-oN", fname + ".txt"])
        out_box.insert(tk.END, f"[*] Saving to {fname}.txt\n")

    # show command
    final_cmd = " ".join(cmd)
    out_box.insert(tk.END, f"[*] Executing: {final_cmd}\n")
    out_box.insert(tk.END, "-"*40 + "\n")
    
    # run in thread so gui doesnt freeze
    def execute():
        try:
            process = subprocess.Popen(
                cmd, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE,
                text=True
            )
            
            # stream output line by line
            for line in process.stdout:
                out_box.insert(tk.END, line)
                out_box.see(tk.END) # auto scroll
                
            out_box.insert(tk.END, "\n[+] Scan Complete.")
        except Exception as e:
            out_box.insert(tk.END, f"\n[!] Error: {str(e)}")
            out_box.insert(tk.END, "\n[!] Is Nmap installed?")

    Thread(target=execute).start()


# --- GUI LAYOUT ---
root = tk.Tk()
root.title("KAMUI v1.0 // GHOST PROTOCOL")
root.geometry("600x550")
root.configure(bg=BG_COLOR)

# custom hacker font
hack_font = ("Consolas", 10)
bold_font = ("Consolas", 12, "bold")

# header
lbl_title = tk.Label(root, text=":: KAMUI INTERFACE ::", bg=BG_COLOR, fg=TXT_COLOR, font=("Consolas", 16, "bold"))
lbl_title.pack(pady=10)

# input frame
frame_top = tk.Frame(root, bg=BG_COLOR)
frame_top.pack(pady=5)

tk.Label(frame_top, text="TARGET IP:", bg=BG_COLOR, fg=TXT_COLOR, font=bold_font).grid(row=0, column=0, padx=5)
target_entry = tk.Entry(frame_top, bg="#202020", fg="white", insertbackground="white", font=hack_font, width=30)
target_entry.grid(row=0, column=1, padx=5)

# options frame
frame_mid = tk.LabelFrame(root, text="SCAN CONFIG", bg=BG_COLOR, fg=ACCENT, font=bold_font)
frame_mid.pack(pady=10, padx=20, fill="x")

# scan modes
mode_var = tk.IntVar(value=1)
tk.Radiobutton(frame_mid, text="Stealth (-sS)", variable=mode_var, value=1, bg=BG_COLOR, fg=TXT_COLOR, selectcolor="#202020", font=hack_font).grid(row=0, column=0, sticky="w")
tk.Radiobutton(frame_mid, text="Connect (-sT)", variable=mode_var, value=2, bg=BG_COLOR, fg=TXT_COLOR, selectcolor="#202020", font=hack_font).grid(row=1, column=0, sticky="w")
tk.Radiobutton(frame_mid, text="Ghost (Evasion)", variable=mode_var, value=3, bg=BG_COLOR, fg="#00ffff", selectcolor="#202020", font=hack_font).grid(row=0, column=1, sticky="w")
tk.Radiobutton(frame_mid, text="Loud Audit (-A)", variable=mode_var, value=4, bg=BG_COLOR, fg="#ff9900", selectcolor="#202020", font=hack_font).grid(row=1, column=1, sticky="w")

# decoy input for ghost mode
tk.Label(frame_mid, text="Decoy IP (Ghost):", bg=BG_COLOR, fg="grey", font=("Consolas", 8)).grid(row=2, column=0, pady=5)
decoy_entry = tk.Entry(frame_mid, bg="#202020", fg="grey", insertbackground="white", width=15)
decoy_entry.grid(row=2, column=1, sticky="w")

# ports
port_var = tk.IntVar(value=1)
tk.Radiobutton(frame_mid, text="Top 1000", variable=port_var, value=1, bg=BG_COLOR, fg=TXT_COLOR, selectcolor="#202020", font=hack_font).grid(row=3, column=0, sticky="w")
tk.Radiobutton(frame_mid, text="All Ports", variable=port_var, value=2, bg=BG_COLOR, fg=TXT_COLOR, selectcolor="#202020", font=hack_font).grid(row=3, column=1, sticky="w")

# save option
save_var = tk.IntVar()
tk.Checkbutton(frame_mid, text="Save Result (scan_results.txt)", variable=save_var, bg=BG_COLOR, fg="white", selectcolor="#202020", font=hack_font).grid(row=4, column=0, columnspan=2, pady=5)

# execute button
btn_run = tk.Button(root, text="INITIATE SCAN", bg=ACCENT, fg="white", font=bold_font, command=run_scan, relief="flat")
btn_run.pack(pady=5, fill="x", padx=40)

# output area
out_box = tk.Text(root, bg="#111", fg=TXT_COLOR, font=("Consolas", 9), height=15, relief="flat")
out_box.pack(pady=10, padx=20, fill="both", expand=True)

# credits
tk.Label(root, text="System Ready...", bg=BG_COLOR, fg="#444", font=("Consolas", 8)).pack(side="bottom", anchor="e", padx=10)

# start app
root.mainloop()