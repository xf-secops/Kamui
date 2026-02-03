import os
import sys
import time
import subprocess
import random

# KAMUI DASHBOARD v1.0
# ---------------------------------

# Colors
R = '\033[91m'
G = '\033[92m'
C = '\033[36m'
W = '\033[0m'
Y = '\033[93m'
GY = '\033[90m' # Grey

# These hold your current settings so they don't disappear
cfg = {
    "target": "",
    "mode": "-sS",
    "mode_name": "Stealth (Default)",
    "ports": "Top 1000",
    "port_flag": "",
    "adv": "",
    "adv_name": "None",
    "ghost": False,
    "decoy": "",
    "spoof": "",
    "mtu": "",
    "sport": "",
    "frag": False,
    "badsum": False,
    "noping": False,
    "os_det": False
}

def clear():
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')

def banner():
    clear()
    print(f"{C}")
    print(r"""
    __ __   ____  ___ ___  __ __  ____ 
   |  |  | /    ||   |   ||  |  ||    |
   |  |  ||  o  || _   _ ||  |  | |  | 
   |  _  ||     ||  \_/  ||  |  | |  | 
   |  |  ||  _  ||   |   ||  :  | |  | 
   |  |  ||  |  ||   |   ||     | |  | 
   |__|__||__|__||___|___| \__,_||____|
             GHOST PROTOCOL v8.0
             
      [ made by atsukiiii01 ]
    """)
    print("-" * 60)

def show_dashboard():
    # This acts as the "Main Menu"
    banner()
    
    # Target Status
    t_col = R if cfg['target'] == "" else G
    t_val = "NOT SET" if cfg['target'] == "" else cfg['target']
    
    print(f" {W}TARGET SYSTEM:{W}")
    print(f" {Y}[1]{W} IP / Domain    : {t_col}{t_val}{W}")
    print("-" * 60)
    
    print(f" {W}ATTACK CONFIG:{W}")
    print(f" {Y}[2]{W} Scan Mode      : {C}{cfg['mode_name']}{W}")
    print(f" {Y}[3]{W} Port Selection : {C}{cfg['ports']}{W}")
    print(f" {Y}[4]{W} Advanced       : {C}{cfg['adv_name']}{W}")
    
    # Evasion Status logic
    e_stat = f"{R}DISABLED{W}"
    if cfg['ghost']: e_stat = f"{G}ENABLED{W} (Decoy, Spoof, Frag...)"
    
    print(f" {Y}[5]{W} Ghost Evasion  : {e_stat}")
    print(f" {Y}[6]{W} Discovery      : Ping={not cfg['noping']}, OS={cfg['os_det']}")
    print("-" * 60)
    
    if cfg['target'] != "":
        print(f" {G}[0] >> EXECUTE ATTACK <<{W}")
    else:
        print(f" {GY}[0] (Set Target First){W}")
    
    print(f" {R}[x] Exit{W}")
    print("-" * 60)

def menu_target():
    print(f"\n{Y}>> CURRENT TARGET: {W}{cfg['target']}")
    new_t = input(f"{C}>> Enter New IP (Enter to cancel): {W}")
    if len(new_t) > 0:
        cfg['target'] = new_t

def menu_mode():
    print(f"\n{Y}:: SELECT SCAN MODE ::{W}")
    print(f"{G}[1]{W} Stealth (-sS)")
    print(f"{G}[2]{W} Connect (-sT)")
    print(f"{G}[3]{W} UDP (-sU)")
    print(f"{G}[4]{W} Aggressive (-A)")
    
    c = input(f"{C}>> Choice (Enter to keep '{cfg['mode_name']}'): {W}")
    if c == "1": cfg['mode'] = "-sS"; cfg['mode_name'] = "Stealth"
    elif c == "2": cfg['mode'] = "-sT"; cfg['mode_name'] = "Connect"
    elif c == "3": cfg['mode'] = "-sU"; cfg['mode_name'] = "UDP"
    elif c == "4": cfg['mode'] = "-A"; cfg['mode_name'] = "Aggressive"

def menu_ports():
    print(f"\n{Y}:: PORT CONFIG ::{W}")
    print(f"{G}[1]{W} Top 1000 (Default)")
    print(f"{G}[2]{W} All Ports (-p-)")
    print(f"{G}[3]{W} Fast (-F)")
    print(f"{G}[4]{W} Custom")
    
    c = input(f"{C}>> Choice (Enter to keep '{cfg['ports']}'): {W}")
    if c == "1": cfg['port_flag'] = ""; cfg['ports'] = "Top 1000"
    elif c == "2": cfg['port_flag'] = "-p-"; cfg['ports'] = "All Ports"
    elif c == "3": cfg['port_flag'] = "-F"; cfg['ports'] = "Fast"
    elif c == "4":
        cust = input(f"{Y}>> Enter Ports (e.g. 21,22,80): {W}")
        if cust:
            cfg['port_flag'] = f"-p {cust}"
            cfg['ports'] = f"Custom ({cust})"

def menu_adv():
    print(f"\n{Y}:: ADVANCED PROFILES ::{W}")
    print(f"{G}[1]{W} None")
    print(f"{G}[2]{W} Vuln Scan (--script=vuln)")
    print(f"{G}[3]{W} Weak Passwords (--script=auth)")
    print(f"{G}[4]{W} Safe Discovery (--script=safe)")
    print(f"{G}[5]{W} Banner Grab (--script=banner)")
    
    c = input(f"{C}>> Choice (Enter to keep '{cfg['adv_name']}'): {W}")
    if c == "1": cfg['adv'] = ""; cfg['adv_name'] = "None"
    elif c == "2": cfg['adv'] = "--script=vuln"; cfg['adv_name'] = "Vuln Scan"
    elif c == "3": cfg['adv'] = "--script=auth"; cfg['adv_name'] = "Auth Audit"
    elif c == "4": cfg['adv'] = "--script=safe"; cfg['adv_name'] = "Safe Disc"
    elif c == "5": cfg['adv'] = "--script=banner"; cfg['adv_name'] = "Banner Grab"

def menu_ghost():
    print(f"\n{Y}:: GHOST EVASION SETUP ::{W}")
    print(f"{GY}(Press Enter to skip any setting){W}")
    
    dec = input(f"{C}>> Decoy IP (-D) [{cfg['decoy']}]: {W}")
    if dec: cfg['decoy'] = dec
    
    spf = input(f"{C}>> Spoof IP (-S) [{cfg['spoof']}]: {W}")
    if spf: cfg['spoof'] = spf
    
    mtu = input(f"{C}>> MTU Size [{cfg['mtu']}]: {W}")
    if mtu: cfg['mtu'] = mtu
    
    sport = input(f"{C}>> Source Port [{cfg['sport']}]: {W}")
    if sport: cfg['sport'] = sport
    
    f = input(f"{C}>> Fragment (-f)? (y/n): {W}")
    if f.lower() == 'y': cfg['frag'] = True
    elif f.lower() == 'n': cfg['frag'] = False
    
    b = input(f"{C}>> Bad Checksum? (y/n): {W}")
    if b.lower() == 'y': cfg['badsum'] = True
    elif b.lower() == 'n': cfg['badsum'] = False
    
    # Enable logic
    if any([cfg['decoy'], cfg['spoof'], cfg['mtu'], cfg['sport'], cfg['frag'], cfg['badsum']]):
        cfg['ghost'] = True
    else:
        cfg['ghost'] = False

def menu_disc():
    print(f"\n{Y}:: DISCOVERY FLAGS ::{W}")
    
    np = input(f"{C}>> Disable Ping (-Pn)? (y/n) [Current: {cfg['noping']}]: {W}")
    if np.lower() == 'y': cfg['noping'] = True
    elif np.lower() == 'n': cfg['noping'] = False
    
    osd = input(f"{C}>> OS Detect (-O)? (y/n) [Current: {cfg['os_det']}]: {W}")
    if osd.lower() == 'y': cfg['os_det'] = True
    elif osd.lower() == 'n': cfg['os_det'] = False

def execute():
    # Build the massive command string based on current state
    z = ["nmap"]
    
    # Mode
    z.append(cfg['mode'])
    
    # Ports
    if cfg['port_flag']: z += cfg['port_flag'].split(" ")
    
    # Advanced
    if cfg['adv']: z.append(cfg['adv'])
    
    # Discovery
    if cfg['noping']: z.append("-Pn")
    if cfg['os_det']: z.append("-O")
    
    # Ghost
    if cfg['decoy']:
        z += ["-D", cfg['decoy'], "-T1"]
    else:
        z.append("-T4") # Default fast timing
        
    if cfg['spoof']: z += ["-S", cfg['spoof'], "-e", "eth0"]
    if cfg['mtu']: z += ["--mtu", cfg['mtu']]
    if cfg['sport']: z += ["--source-port", cfg['sport']]
    if cfg['frag']: z.append("-f")
    if cfg['badsum']: z.append("--badsum")
    
    # Target
    z.append(cfg['target'])
    
    # Final Confirm
    cmd_str = " ".join(z)
    print("\n" + "="*60)
    print(f"{G}FINAL COMMAND:{W}")
    print(f"{C}{cmd_str}{W}")
    print("="*60 + "\n")
    
    go = input(f"{Y}>> LAUNCH? (y/n): {W}")
    if go.lower() == "y":
        try:
            print(f"\n{G}[*] INITIALIZING ENGINE...{W}")
            subprocess.call(z)
            input(f"\n{Y}[PRESS ENTER TO RETURN TO MENU]{W}")
        except Exception as e:
            print(f"{R}ERROR: {e}{W}")
            input()

# MAIN LOOP
def main():
    while True:
        show_dashboard()
        ch = input(f"\n{C}>> SELECT OPTION: {W}")
        
        if ch == "1": menu_target()
        elif ch == "2": menu_mode()
        elif ch == "3": menu_ports()
        elif ch == "4": menu_adv()
        elif ch == "5": menu_ghost()
        elif ch == "6": menu_disc()
        elif ch == "0":
            if cfg['target'] == "":
                print(f"{R}[!] NO TARGET SET{W}")
                time.sleep(1)
            else:
                execute()
        elif ch.lower() == "x":
            print(f"{R}Exiting...{W}")
            sys.exit()
        else:
            pass # just refresh

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nForce Quit.")