# KAMUI // GHOST PROTOCOL

> **[ made by atsukiiii01 ]**

**KAMUI** is not just another Nmap wrapper. It is a stealth-focused Command & Control (C2) interface designed for Red Team engagements. It abstracts complex scanning logic into a non-linear dashboard, allowing for rapid target reconfiguration and automated firewall evasion.

Built with a "Zero-Detect" code structure to evade static analysis.

---

### ⚡ CAPABILITIES

* **Ghost Protocol:** Automated evasion engine that chains IP decoys, spoofing, packet fragmentation, and bad checksums to bypass IDS/firewalls.

* **C2 Dashboard:** Non-linear terminal interface. Change your target, ports, or scan mode in any order without restarting the tool.

* **Smart Profiles:** One-click automation for:
    * `VULN` - CVE Detection
    * `AUTH` - Weak Credential Auditing
    * `SAFE` - Non-intrusive Discovery
    * `BANNER` - Service Fingerprinting

* **Hybrid Interface:** Includes both a raw **Terminal Dashboard** (for SSH sessions) and a **Graphical Interface** (for desktop use).

---

### 📥 DEPLOYMENT

**1. Prerequisites**

You need **Python 3** and the **Nmap** engine installed on your system.

* **Kali / Linux:** `sudo apt install nmap python3`

* **macOS:** `brew install nmap python3`

* **Windows:** [Download Nmap Installer](https://nmap.org/download.html)

**2. Installation**

Clone the repository and install the GUI dependency (FreeSimpleGUI).

```bash

git clone https://github.com/Atsukiiii01/Kamui.git

cd kamui

pip install -r requirements.txt

INITIALIZATION
You have two ways to run KAMUI, depending on your environment.

OPTION A: The C2 Dashboard (Terminal)
Best for speed, SSH sessions, and "Hacker Mode." No mouse required.

python kamui_dashboard.py

:- Navigation: Press numbers 1-6 to edit settings.

:- Back: Press ENTER on any menu to return to the dashboard.

:- Launch: Press 0 to execute the attack.

OPTION B: The Graphical Interface (GUI)
Best for desktop use with a visual progress bar and mouse controls.

python kamui_gui_final.py

:- Usage: Select your mode, check the "Ghost Protocol" boxes for evasion, and click INITIATE.

💀 GHOST EVASION GUIDETo bypass firewalls, enable Ghost Evasion in the menu (Option 5).

Setting,Effect
Decoy (-D),"Floods the target with fake traffic from random IPs, hiding your true IP."
Spoof (-S),Masquerades your packets as coming from a different trusted host.
Fragment (-f),Splits packets into tiny chunks to slip past simple packet filters.
BadSum,Sends packets with invalid checksums (useful for mapping firewall rules).

⚠️ DISCLAIMER
KAMUI is engineered for authorized security auditing and educational purposes only. Using this tool against systems without explicit permission is illegal. The creator (atsukiiii01) assumes no liability for misuse.

"We are ghosts. We are nowhere and everywhere."
